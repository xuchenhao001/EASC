#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import logging
import math
import sys
import time
import numpy as np
import threading

import torch
from flask import Flask, request

import utils.util
from utils.CentralStore import IPCount
from utils.DatasetStore import LocalDataset
from utils.EnvStore import EnvStore
from utils.ModelStore import AsyncCentralModelStore
from utils.Trainer import Trainer
from models.Fed import async_fed_avg

logging.setLoggerClass(utils.util.ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("scei-async")

env_store = EnvStore()
local_dataset = LocalDataset()
central_model_store = AsyncCentralModelStore()
ipCount = IPCount()
trainer_pool = {}  # multiple thread trainers stored in this map


def init_trainer():
    trainer = Trainer()
    trainer.uuid = fetch_uuid()

    load_result = trainer.init_model(env_store.args.model, env_store.args.dataset, env_store.args.device,
                                     local_dataset.image_shape)
    if not load_result:
        sys.exit()

    # trained the initial local model, which will be treated as first global model.
    trainer.net_glob.train()
    # generate md5 hash from model, which is treated as global model of previous round.
    w = trainer.net_glob.state_dict()
    central_model_store.update_global_model(w, epochs=-1)  # -1 means the initial global model
    trainer.model_store.update_my_global_model(w)
    trainer_pool[trainer.uuid] = trainer
    return trainer.uuid


# simulate RAFT procedure
def prepare_committee(trainer_uuid):
    trainer = trainer_pool[trainer_uuid]
    logger.info("Prepare committee for user [{}] in epoch [{}]".format(trainer.uuid, trainer.epoch))
    trainer.round_start_time = time.time()
    committee_elect_start_time = time.time()

    if trainer.is_first_epoch():
        trainer.init_time = time.time()
        w_glob = fetch_global_model()
        trainer.model_store.update_my_global_model(w_glob)

    # re-elect the committee members
    logger.debug('[RAFT] Current global model hash: ' + trainer.model_store.my_global_model_hash)
    committee_leader_id = int(trainer.model_store.my_global_model_hash, 16) % env_store.args.num_users + 1
    committee_proportion_num = math.ceil(env_store.args.num_users * 0.3)  # committee id delta value
    committee_highest_id = committee_proportion_num + committee_leader_id - 1
    logger.debug('[RAFT] The leader id is: %s' % str(committee_leader_id))
    # pull up hraftd distributed processes, if the value of uuid is in range of committee leader id and highest id.
    rounded_committee_highest_id = 0
    if committee_highest_id > env_store.args.num_users:
        rounded_committee_highest_id = committee_highest_id % env_store.args.num_users

    # if this node is elected as committee leader, send raft network info to the blockchain
    if trainer.uuid == committee_leader_id:
        body_data = {
            'message': 'RAFT_INFO',
            'data': {
                'leader_id': rounded_committee_highest_id,
            },
            'uuid': trainer.uuid,
            'epochs': trainer.epoch,
        }
        utils.util.post_msg_blockchain(body_data, env_store.args.num_users)
    trainer.committee_elect_duration = time.time() - committee_elect_start_time
    # continue training
    train(trainer.uuid)


def train(trainer_uuid):
    trainer = trainer_pool[trainer_uuid]
    logger.debug("Train local model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # calculate initial model accuracy, record it as the benchmark.
    if trainer.is_first_epoch():
        w_glob = fetch_global_model()
        trainer.model_store.update_my_global_model(w_glob)
        trainer.load_model(w_glob)
        trainer.evaluate_model_with_log(local_dataset, env_store.args, record_epoch=0, clean=True)
    else:
        trainer.load_model(trainer.model_store.my_global_model)

    train_start_time = time.time()
    w_local, w_loss = trainer.train(local_dataset, env_store.args)
    trainer.model_store.my_local_model = w_local
    trainer.round_train_duration = time.time() - train_start_time

    # send local model to the committee leader
    w_local_compressed = utils.util.compress_tensor(w_local)
    body_data = {
        "message": "upload_local_w",
        "w_compressed": w_local_compressed,
        "uuid": trainer.uuid,
        "from_ip": env_store.from_ip,
    }
    utils.util.post_msg_trigger(env_store.trigger_url, body_data)
    # send hash of local model to the blockchain
    body_data = {
        'message': 'LOCAL_HASH',
        'data': {
            'local_hash': utils.util.generate_md5_hash(w_local),
        },
        'uuid': trainer.uuid,
        'epochs': trainer.epoch,
    }
    utils.util.post_msg_blockchain(body_data, env_store.args.num_users)

    # finished uploading local model, fetch latest global model and calculate alpha
    fetch_latest_global_w(trainer.uuid)


def gather_local_w(local_uuid, from_ip, w_compressed):
    ipCount.set_map(local_uuid, from_ip)

    logger.debug("aggregate global model after received a new local model.")
    w_local = utils.util.decompress_tensor(w_compressed)
    w_glob = async_fed_avg(w_local, central_model_store.global_model, env_store.args.device)
    # save global model
    central_model_store.update_global_model(w_glob)
    # send the hash of the global model to the ledger
    body_data = {
        'message': 'UploadGlobalModelHash',
        'data': {
            'global_model_hash': central_model_store.global_model_hash,
        },
    }
    utils.util.post_msg_blockchain(body_data, env_store.args.num_users)


def fetch_latest_global_w(trainer_uuid):
    trainer = trainer_pool[trainer_uuid]
    logger.debug("fetch latest global model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))
    w_glob = fetch_global_model()
    trainer.model_store.update_my_global_model(w_glob)

    # test different alpha values with their accuracies
    acc_alpha_map = {}
    if env_store.args.hyperpara_static:  # if static alpha
        negotiate_step_list = [env_store.args.hyperpara]
    else:  # if dynamic alpha
        negotiate_step = (env_store.args.hyperpara_max - env_store.args.hyperpara_min) / env_store.args.negotiate_round
        negotiate_step_list = np.arange(env_store.args.hyperpara_min, env_store.args.hyperpara_max, negotiate_step)
    negotiate_step_list = np.around(negotiate_step_list, 2)
    test_start_time = time.time()
    for alpha in negotiate_step_list:
        w_local_tmp = {}
        for key in w_glob.keys():
            if env_store.args.device != torch.device('cpu'):
                w_glob[key] = w_glob[key].to(env_store.args.device)
            w_local_tmp[key] = alpha * trainer.model_store.my_local_model[key] + (1 - alpha) * w_glob[key]

        # test new tmp local model
        trainer.load_model(w_local_tmp)
        acc_test, _, _, _, _ = trainer.evaluate_model(local_dataset, env_store.args)
        acc_alpha_map[alpha] = acc_test
        logger.debug("uuid: {}, alpha: {}, acc: {}".format(trainer.uuid, alpha, acc_test))
    trainer.round_test_duration = time.time() - test_start_time

    # upload acc-alpha map to committee leader and the ledger
    body_data = {
        "message": "acc_alpha_map",
        "acc_alpha_map": acc_alpha_map,
        "uuid": trainer.uuid,
        "from_ip": env_store.from_ip,
    }
    logger.debug('finished testing acc-alpha map, send accuracy and alpha map to the ledger')
    utils.util.post_msg_trigger(env_store.trigger_url, body_data)

    # fetch the latest optimal alpha and finish the round
    round_finish(trainer.uuid)


def gather_acc_alpha_map(acc_alpha_map, local_uuid, from_ip):
    ipCount.set_map(local_uuid, from_ip)
    # asynchronously update acc-alpha map
    central_model_store.async_acc_alpha_add(local_uuid, acc_alpha_map)
    optimal_alpha = find_optimal_alpha_acc("Max", central_model_store.acc_alpha_maps)
    # store optimal alpha in central
    central_model_store.optimal_alpha = optimal_alpha
    # send optimal alpha to blockchain
    body_data = {
        'message': 'OPTIMAL_ALPHA',
        'data': {
            'optimal_alpha': optimal_alpha,
        },
    }
    utils.util.post_msg_blockchain(body_data, env_store.args.num_users)


def find_optimal_alpha_acc(select_strategy, acc_alpha_maps):
    logger.debug("[Find Alpha] According to max acc_test average policy")
    num_users = len(acc_alpha_maps)
    if num_users == 0:
        return 1.0  # default optimal alpha is 1.0
    alphas = acc_alpha_maps[list(acc_alpha_maps.keys())[0]].keys()
    max_acc = 0
    max_alpha = list(alphas)[0]
    for alpha in alphas:
        acc_sum = 0
        for _, acc_alpha_map in acc_alpha_maps.items():
            acc_sum += acc_alpha_map[alpha]
        if acc_sum > max_acc:
            max_alpha = alpha
    logger.debug("found optimal alpha {} with average accuracy: {}".format(max_alpha, max_acc / num_users))
    return max_alpha


def round_finish(trainer_uuid):
    trainer = trainer_pool[trainer_uuid]
    logger.debug("fetch optimal alpha for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))
    optimal_alpha = fetch_optimal_alpha()
    # calculate new private local model according to the alpha
    w_tmp = {}
    optimal_alpha = float(optimal_alpha)
    for key in trainer.model_store.my_global_model.keys():
        if env_store.args.device != torch.device('cpu'):
            trainer.model_store.my_global_model[key] = \
                trainer.model_store.my_global_model[key].to(env_store.args.device)
        w_tmp[key] = optimal_alpha * trainer.model_store.my_local_model[key] + \
                     (1 - optimal_alpha) * trainer.model_store.my_global_model[key]
    trainer.model_store.my_local_model = w_tmp
    # finally, evaluate the local model
    trainer.load_model(trainer.model_store.my_local_model)
    trainer.evaluate_model_with_log(local_dataset, env_store.args, record_communication_time=True)

    # epochs count down to 0
    trainer.epoch += 1
    if trainer.epoch <= env_store.args.epochs:
        logger.info("########## EPOCH #{} ##########".format(trainer.epoch))
        prepare_committee(trainer.uuid)
    else:
        logger.info("########## ALL DONE! ##########")
        body_data = {
            "message": "shutdown_python",
            "uuid": trainer.uuid,
            "from_ip": env_store.from_ip,
        }
        utils.util.post_msg_trigger(env_store.trigger_url, body_data)


def fetch_uuid():
    body_data = {
        "message": "fetch_uuid",
    }
    detail = utils.util.post_msg_trigger(env_store.trigger_url, body_data)
    uuid = detail.get("uuid")
    return uuid


def load_uuid():
    new_id = ipCount.get_new_id()
    detail = {"uuid": new_id}
    return detail


def fetch_global_model():
    body_data = {
        "message": "fetch_global_model"
    }
    detail = utils.util.post_msg_trigger(env_store.trigger_url, body_data)
    global_model_compressed = detail.get("global_model")
    w_glob = utils.util.decompress_tensor(global_model_compressed)
    return w_glob


def load_global_model():
    detail = {
        "global_model": central_model_store.global_model_compressed,
    }
    return detail


def fetch_optimal_alpha():
    body_data = {
        "message": "fetch_optimal_alpha"
    }
    detail = utils.util.post_msg_trigger(env_store.trigger_url, body_data)
    optimal_alpha = detail.get("optimal_alpha")
    return optimal_alpha


def load_optimal_alpha():
    detail = {
        "optimal_alpha": central_model_store.optimal_alpha,
    }
    return detail


def start_train():
    time.sleep(env_store.args.start_sleep)
    trainer_uuid = init_trainer()
    prepare_committee(trainer_uuid)


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
            elif message == "fetch_global_model":
                detail = load_global_model()
            elif message == "fetch_optimal_alpha":
                detail = load_optimal_alpha()
            elif message == "upload_local_w":
                threading.Thread(target=gather_local_w, args=(
                    data.get("uuid"), data.get("from_ip"), data.get("w_compressed"))).start()
            elif message == "acc_alpha_map":
                threading.Thread(target=gather_acc_alpha_map, args=(data.get("acc_alpha_map"), data.get("uuid"),
                                                                    data.get("from_ip"),)).start()
            elif message == "shutdown_python":
                threading.Thread(target=utils.util.shutdown_count, args=(
                    data.get("uuid"), data.get("from_ip"), env_store.args.fl_listen_port,
                    env_store.args.num_users)).start()
            elif message == "shutdown":
                threading.Thread(target=utils.util.my_exit, args=(env_store.args.exit_sleep,)).start()
            response = {"status": status, "detail": detail}
            return response


def main():
    # init environment arguments
    env_store.init()
    # init local dataset
    local_dataset.init_local_dataset(env_store.args.dataset, env_store.args.num_users)
    # set logger level
    logger.setLevel(env_store.args.log_level)

    for _ in range(env_store.args.num_users):
        logger.debug("start new thread")
        threading.Thread(target=start_train, args=()).start()

    flask_app = Flask(__name__)
    my_route(flask_app)
    logger.info("start serving at " + str(env_store.args.fl_listen_port) + "...")
    flask_app.run(host="0.0.0.0", port=int(env_store.args.fl_listen_port))


if __name__ == "__main__":
    main()
