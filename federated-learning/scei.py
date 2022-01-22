#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import logging
import math
import sys
import time
import numpy as np
import threading
from flask import Flask, request

import utils.util
from utils.CentralStore import IPCount
from utils.ModelStore import ModelStore
from utils.Trainer import Trainer
from models.Fed import fed_avg

logging.setLoggerClass(utils.util.ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("scei")

# TO BE CHANGED
# federated learning server listen port
fed_listen_port = 8888
# TO BE CHANGED FINISHED

# NOT TO TOUCH VARIABLES BELOW
trainer = Trainer()
model_store = ModelStore()
ipCount = IPCount()


def init():
    trainer.parse_args()
    trainer.init_urls(fed_listen_port)
    logger.setLevel(trainer.args.log_level)

    load_result = trainer.init_dataset()
    if not load_result:
        sys.exit()
    trainer.dataset.init_trojan_attack(trainer.args)

    load_result = trainer.init_model()
    if not load_result:
        sys.exit()

    # trained the initial local model, which will be treated as first global model.
    trainer.net_glob.train()
    # generate md5 hash from model, which is treated as global model of previous round.
    w = trainer.net_glob.state_dict()
    model_store.update_global_model(w, -1)  # -1 means the initial global model


# simulate RAFT procedure
async def prepare_committee():
    logger.info("Prepare committee for user [{}] in epoch [{}]".format(trainer.uuid, trainer.epoch))
    trainer.round_start_time = time.time()
    committee_elect_start_time = time.time()

    if trainer.is_first_epoch():
        # download initial global model
        body_data = {
            "message": "global_model",
            "epochs": -1,
        }
        detail = trainer.post_msg_trigger(body_data)
        global_model_compressed = detail.get("global_model")
        w_glob = utils.util.decompress_tensor(global_model_compressed)
        trainer.load_model(w_glob)

    # re-elect the committee members
    logger.debug('[RAFT] Current global model hash: ' + model_store.global_model_hash)
    committee_leader_id = int(model_store.global_model_hash, 16) % trainer.args.num_users + 1
    committee_proportion_num = math.ceil(trainer.args.num_users * 0.3)  # committee id delta value
    committee_highest_id = committee_proportion_num + committee_leader_id - 1
    logger.debug('[RAFT] The leader id is: %s' % str(committee_leader_id))
    # pull up hraftd distributed processes, if the value of uuid is in range of committee leader id and highest id.
    rounded_committee_highest_id = 0
    if committee_highest_id > trainer.args.num_users:
        rounded_committee_highest_id = committee_highest_id % trainer.args.num_users

    # if this node is elected as committee leader, send raft network info to the blockchain
    if int(trainer.uuid) == committee_leader_id:
        body_data = {
            'message': 'RAFT_INFO',
            'data': {
                'leader_id': rounded_committee_highest_id,
            },
            'uuid': trainer.uuid,
            'epochs': trainer.epoch,
        }
        trainer.post_msg_blockchain(body_data, trainer.args.num_users)
    trainer.committee_elect_duration = time.time() - committee_elect_start_time
    # continue training
    train()


def train():
    if trainer.uuid == -1:
        trainer.uuid = fetch_uuid()
    logger.debug("Train local model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # calculate initial model accuracy, record it as the benchmark.
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
    else:
        trainer.load_model(model_store.global_model)

    train_start_time = time.time()
    w_local, w_loss = trainer.train()
    model_store.my_local_model = w_local
    trainer.round_train_duration = time.time() - train_start_time

    # send local model to the committee leader
    w_local_compressed = utils.util.compress_tensor(w_local)
    body_data = {
        "message": "upload_local_w",
        "w_compressed": w_local_compressed,
        "uuid": trainer.uuid,
        "from_ip": trainer.from_ip,
    }
    trainer.post_msg_trigger(body_data)
    # send hash of local model to the blockchain
    body_data = {
        'message': 'LOCAL_HASH',
        'data': {
            'local_hash': utils.util.generate_md5_hash(w_local),
        },
        'uuid': trainer.uuid,
        'epochs': trainer.epoch,
    }
    trainer.post_msg_blockchain(body_data, trainer.args.num_users)


def gather_local_w(local_uuid, from_ip, w_compressed):
    ipCount.set_map(local_uuid, from_ip)
    if model_store.local_models_add_count(local_uuid, utils.util.decompress_tensor(w_compressed),
                                          trainer.args.num_users):
        logger.debug("Gathered enough w, average and release them")
        w_glob = fed_avg(model_store.local_models)
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


def receive_global_w(w_glob_compressed):
    logger.debug("Received latest global model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # load hash of new global model, which is downloaded from the leader
    w_glob = utils.util.decompress_tensor(w_glob_compressed)

    # test different alpha values with their accuracies
    acc_alpha_map = {}
    if trainer.args.hyperpara_static:  # if static alpha
        negotiate_step_list = [trainer.args.hyperpara]
    else:  # if dynamic alpha
        negotiate_step = (trainer.args.hyperpara_max - trainer.args.hyperpara_min) / trainer.args.negotiate_round
        negotiate_step_list = np.arange(trainer.args.hyperpara_min, trainer.args.hyperpara_max, negotiate_step)
    test_start_time = time.time()
    for alpha in negotiate_step_list:
        w_local_tmp = {}
        for key in w_glob.keys():
            w_local_tmp[key] = alpha * model_store.my_local_model[key] + (1 - alpha) * w_glob[key]

        # test new tmp local model
        trainer.load_model(w_local_tmp)
        acc_test, _, _, _, _ = trainer.evaluate_model()
        acc_alpha_map[alpha] = acc_test
        logger.debug("uuid: {}, alpha: {}, acc: {}".format(trainer.uuid, alpha, acc_test))
    trainer.round_test_duration = time.time() - test_start_time

    # upload acc-alpha map to committee leader and the ledger
    body_data = {
        "message": "acc_alpha_map",
        "acc_alpha_map": acc_alpha_map,
        "uuid": trainer.uuid,
        "from_ip": trainer.from_ip,
    }
    logger.debug('finished testing acc-alpha map, send accuracy and alpha map to the ledger')
    trainer.post_msg_trigger(body_data)


def gather_acc_alpha_map(acc_alpha_map, local_uuid, from_ip):
    ipCount.set_map(local_uuid, from_ip)
    if model_store.acc_alpha_add_count(local_uuid, acc_alpha_map, trainer.args.num_users):
        logger.debug("Gathered enough accuracy and alpha, find optimal alpha")
        optimal_alpha = find_optimal_alpha_acc("Max", model_store.acc_alpha_maps)
        # reset acc_alpha map
        model_store.acc_alpha_reset()
        # send optimal alpha to blockchain
        body_data = {
            'message': 'OPTIMAL_ALPHA',
            'data': {
                'optimal_alpha': optimal_alpha,
            },
            'uuid': trainer.uuid,
            'epochs': trainer.epoch,
        }
        trainer.post_msg_blockchain(body_data, trainer.args.num_users)
        # release optimal_alpha to each local node
        for uuid in ipCount.get_keys():
            body_data = {
                "message": "release_optimal_alpha",
                "optimal_alpha": optimal_alpha,
            }
            my_url = "http://" + ipCount.get_map(uuid) + ":" + str(fed_listen_port) + "/trigger"
            utils.util.http_client_post(my_url, body_data)


def find_optimal_alpha_acc(select_strategy, acc_alpha_maps):
    logger.debug("[Find Alpha] According to max acc_test average policy")
    alphas = acc_alpha_maps[0].keys()
    num_users = len(acc_alpha_maps)
    max_acc = 0
    max_alpha = alphas[0]
    for alpha in alphas:
        acc_sum = 0
        for acc_alpha_map in acc_alpha_maps:
            acc_sum += acc_alpha_map[alpha]
        if acc_sum > max_acc:
            max_alpha = alpha
    logger.debug("found optimal alpha {} with average accuracy: {}".format(max_alpha, max_acc/num_users))
    return max_alpha


def round_finish(optimal_alpha):
    # calculate new w_glob (w_local2) according to the alpha
    w_tmp = {}
    for key in model_store.global_model.keys():
        w_tmp[key] = optimal_alpha * model_store.my_local_model[key] + \
                     (1 - optimal_alpha) * model_store.global_model[key]
    model_store.my_local_model = w_tmp
    # finally, evaluate the local model
    trainer.load_model(model_store.my_local_model)
    trainer.evaluate_model_with_log(record_communication_time=True)

    # epochs count down to 0
    trainer.epoch += 1
    if trainer.epoch <= trainer.args.epochs:
        prepare_committee()
    else:
        logger.info("########## ALL DONE! ##########")
        body_data = {
            "message": "shutdown_python",
            "uuid": trainer.uuid,
            "from_ip": trainer.from_ip,
        }
        trainer.post_msg_trigger(body_data)


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
    prepare_committee()


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
                threading.Thread(target=receive_global_w, args=(data.get("w_compressed"), )).start()
            elif message == "acc_alpha_map":
                threading.Thread(target=gather_acc_alpha_map, args=(data.get("acc_alpha_map"), data.get("uuid"),
                                                                    data.get("from_ip"),)).start()
            elif message == "release_optimal_alpha":
                threading.Thread(target=round_finish, args=(data.get("optimal_alpha"), )).start()
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
