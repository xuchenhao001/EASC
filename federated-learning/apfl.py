#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import logging
import sys
import time
import numpy as np
import threading
from flask import Flask, request

import utils
from models.Fed import fed_avg
from utils.CentralStore import IPCount
from utils.ModelStore import APFLModelStore
from utils.Trainer import Trainer
from utils.util import model_loader, ColoredLogger

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("apfl")

# TO BE CHANGED
# federated learning server listen port
fed_listen_port = 8888
# TO BE CHANGED FINISHED

# NOT TO TOUCH VARIABLES BELOW
trainer = Trainer()
model_store = APFLModelStore()
ipCount = IPCount()


def init():
    trainer.parse_args()
    trainer.init_urls(fed_listen_port)
    logger.setLevel(trainer.args.log_level)

    load_result = trainer.init_dataset()
    if not load_result:
        sys.exit()

    load_result = trainer.init_model()
    if not load_result:
        sys.exit()

    # trained the initial local model, which will be treated as first global model.
    trainer.net_glob.train()
    # generate md5 hash from model, which is treated as global model of previous round.
    w = trainer.net_glob.state_dict()
    model_store.update_global_model(w, -1)  # -1 means the initial global model


def train(w_global_local_compressed=None):
    if trainer.uuid == -1:
        trainer.uuid = fetch_uuid()
    logger.debug('Train local model for user: %s, epoch: %s.' % (trainer.uuid, trainer.epoch))

    if trainer.is_first_epoch():
        trainer.init_time = time.time()
        # download initial global model
        body_data = {
            "message": "global_model",
            "epochs": -1,
        }
        detail = trainer.post_msg_trigger(body_data)
        global_model_compressed = detail.get("global_model")
        w_glob = utils.util.decompress_tensor(global_model_compressed)
        trainer.load_model(w_glob)
        trainer.evaluate_model_with_log(record_epoch=0, clean=True)
        # global model initialization
        w_glob = trainer.train()
        model_store.update_w_glob(w_glob)
        model_store.update_difference1(w_glob)
        model_store.update_difference2(w_glob)
        # for the first epoch, init user local parameters, w,v,v_bar,alpha
        model_store.update_w_glob_local(w_glob)
        model_store.update_w_locals(w_glob)
        model_store.update_w_locals_per(w_glob)
        trainer.hyper_para = trainer.args.apfl_hyper
    else:
        w_global_local = utils.util.decompress_tensor(w_global_local_compressed)
        model_store.update_w_glob_local(w_global_local)
        model_store.update_w_glob(w_global_local)

    # training for all epochs
    while trainer.epoch > 0:
        logger.info("Epoch [{}] train for user [{}]".format(trainer.epoch, trainer.uuid))
        trainer.round_start_time = time.time()
        train_start_time = time.time()
        # compute v_bar
        for j in model_store.w_glob.keys():
            model_store.w_locals_per[j] = trainer.hyper_para * model_store.w_locals[j] + \
                                          (1 - trainer.hyper_para) * model_store.w_glob_local[j]
            model_store.difference1[j] = model_store.w_locals[j] - model_store.w_glob_local[j]

        # train local global weight
        trainer.load_model(model_store.w_glob_local)
        w = trainer.train()
        model_store.update_w_glob_local(w)

        # train local model weight
        trainer.load_model(model_store.w_locals_per)
        w = trainer.train()
        model_store.update_w_locals(w)

        for j in model_store.w_glob.keys():
            model_store.difference2[j] = (w[j] - model_store.w_locals[j]) * 100.0

        correlation = 0.0
        for j in model_store.w_glob.keys():
            d = model_store.difference1[j].numpy()
            d1 = np.ndarray.flatten(d)
            d = model_store.difference2[j].numpy()
            d2 = np.ndarray.flatten(d)
            correlation = correlation + np.dot(d1, d2)
        correlation = correlation / len(model_store.w_glob.keys())
        trainer.hyper_para = round((trainer.hyper_para - trainer.args.lr * correlation), 2)
        if trainer.hyper_para > 1.0:
            trainer.hyper_para = 1.0

        # update local personalized weight
        for j in model_store.w_glob.keys():
            model_store.w_locals_per[j] = trainer.hyper_para * model_store.w_locals[j] + \
                                          (1 - trainer.hyper_para) * model_store.w_glob_local[j]
        trainer.round_train_duration = time.time() - train_start_time

        trainer.evaluate_model_with_log(record_communication_time=True)

        trainer.epoch -= 1
        # communicate with other nodes every 10 epochs
        if trainer.epoch % 10 == 0:
            from_ip = utils.util.get_ip(trainer.args.test_ip_addr)
            body_data = {
                "message": "upload_local_w",
                "uuid": trainer.uuid,
                "w_glob_local": model_store.w_glob_local_compressed,
                "from_ip": from_ip,
            }
            trainer.post_msg_trigger(body_data)
            return

    logger.info("########## ALL DONE! ##########")
    body_data = {
        "message": "shutdown_python",
        "uuid": trainer.uuid,
        "from_ip": trainer.from_ip,
    }
    trainer.post_msg_trigger(body_data)


def gather_local_w(local_uuid, from_ip, w_compressed):
    ipCount.set_map(local_uuid, from_ip)
    if model_store.local_models_add_count(local_uuid, utils.util.decompress_tensor(w_compressed),
                                          trainer.args.num_users):
        logger.debug("Gathered enough w, average and release them")
        w_glob = fed_avg(model_store.local_models, model_store.global_model)
        # reset local models after aggregation
        model_store.local_models_reset()
        # save global model
        model_store.update_global_model(w_glob, trainer.epoch)
        for uuid in ipCount.get_keys():
            body_data = {
                "message": "release_global_w",
                "w_compressed": model_store.global_model_compressed,
            }
            my_url = "http://" + ipCount.get_map(uuid) + ":" + str(fed_listen_port) + "/trigger"
            utils.util.http_client_post(my_url, body_data)


def fetch_uuid():
    body_data = {
        "message": "fetch_uuid",
    }
    detail = trainer.post_msg_trigger(body_data)
    uuid = detail.get("uuid")
    return uuid


def load_uuid():
    new_id = ipCount.get_new_id()
    detail = {"uuid": new_id}
    return detail


def load_global_model(epochs):
    print("epochs: {}, global model version: {}".format(epochs, model_store.global_model_version))
    if epochs == model_store.global_model_version:
        detail = {
            "global_model": model_store.global_model_compressed,
        }
    else:
        detail = {
            "global_model": None,
        }
    return detail


def start_train():
    time.sleep(trainer.args.start_sleep)
    train()


def my_route(app):
    @app.route("/trigger", methods=["GET", "POST"])
    def trigger_handler():
        # For POST
        if request.method == "POST":
            data = request.get_json()
            status = "yes"
            detail = {}
            message = data.get("message")
            if message == "fetch_uuid":
                detail = load_uuid()
            elif message == "global_model":
                detail = load_global_model(data.get("epochs"))
            elif message == "upload_local_w":
                threading.Thread(target=gather_local_w, args=(
                    data.get("uuid"), data.get("from_ip"), data.get("w_compressed"))).start()
            elif message == "release_global_w":
                threading.Thread(target=train, args=(data.get("w_glob_local"),)).start()
            elif message == "shutdown_python":
                threading.Thread(target=utils.util.shutdown_count, args=(
                    data.get("uuid"), data.get("from_ip"), fed_listen_port, trainer.args.num_users)).start()
            elif message == "shutdown":
                threading.Thread(target=utils.util.my_exit, args=(trainer.args.exit_sleep, )).start()
            response = {"status": status, "detail": detail}
            return response


def main():
    init()

    threading.Thread(target=start_train, args=()).start()

    flask_app = Flask(__name__)
    my_route(flask_app)
    logger.info("start serving at " + str(fed_listen_port) + "...")
    flask_app.run(host="0.0.0.0", port=fed_listen_port)


if __name__ == "__main__":
    main()
