import logging
import sys
import time
import threading
from flask import Flask, request

import utils.util
from utils.CentralStore import IPCount
from utils.DatasetStore import LocalDataset
from utils.EnvStore import EnvStore
from utils.ModelStore import CentralModelStore
from utils.Trainer import Trainer
from utils.util import ColoredLogger
from models.Fed import fed_avg

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("fedavg")

env_store = EnvStore()
local_dataset = LocalDataset()
central_model_store = CentralModelStore()
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


def train(trainer_uuid):
    trainer = trainer_pool[trainer_uuid]
    logger.debug("Train local model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    trainer.round_start_time = time.time()
    # calculate initial model accuracy, record it as the benchmark.
    if trainer.is_first_epoch():
        trainer.init_time = time.time()
        # download initial global model
        body_data = {
            "message": "global_model",
            "epochs": -1,
        }
        detail = utils.util.post_msg_trigger(env_store.trigger_url, body_data)
        global_model_compressed = detail.get("global_model")
        w_glob = utils.util.decompress_tensor(global_model_compressed)
        trainer.load_model(w_glob)
        trainer.evaluate_model_with_log(local_dataset, env_store.args, record_epoch=0, clean=True)
    else:
        trainer.load_model(trainer.model_store.my_global_model)

    train_start_time = time.time()
    w_local, w_loss = trainer.train(local_dataset, env_store.args)
    trainer.round_train_duration = time.time() - train_start_time

    # send local model to the first node
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


def gather_local_w(local_uuid, from_ip, w_compressed):
    ipCount.set_map(local_uuid, from_ip)
    if central_model_store.local_models_add_count(local_uuid, utils.util.decompress_tensor(w_compressed),
                                                  env_store.args.num_users):
        logger.debug("Gathered enough w, average and release them")
        w_glob = fed_avg(central_model_store.local_models, central_model_store.global_model, env_store.args.device)
        # reset local models after aggregation
        central_model_store.local_models_reset()
        # save global model
        central_model_store.update_global_model(w_glob)
        for uuid in ipCount.get_keys():
            body_data = {
                "message": "release_global_w",
                "w_compressed": central_model_store.global_model_compressed,
                "uuid": uuid,
            }
            my_url = "http://" + ipCount.get_map(uuid) + ":" + str(env_store.args.fl_listen_port) + "/trigger"
            utils.util.http_client_post(my_url, body_data)


def receive_global_w(trainer_uuid, w_glob_compressed):
    trainer = trainer_pool[trainer_uuid]
    logger.debug("Received latest global model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # load hash of new global model, which is downloaded from the leader
    w_glob = utils.util.decompress_tensor(w_glob_compressed)
    trainer.model_store.update_my_global_model(w_glob)

    # finally, evaluate the global model
    trainer.load_model(w_glob)
    trainer.evaluate_model_with_log(local_dataset, env_store.args, record_communication_time=True)

    # epochs count down to 0
    trainer.epoch += 1
    if trainer.epoch <= env_store.args.epochs:
        logger.info("########## EPOCH #{} ##########".format(trainer.epoch))
        train(trainer.uuid)
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


def load_global_model(epochs):
    if epochs == central_model_store.global_model_version:
        detail = {
            "global_model": central_model_store.global_model_compressed,
        }
    else:
        detail = {
            "global_model": None,
        }
    return detail


def start_train():
    time.sleep(env_store.args.start_sleep)
    trainer_uuid = init_trainer()
    train(trainer_uuid)


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
                threading.Thread(target=receive_global_w, args=(data.get("uuid"), data.get("w_compressed"))).start()
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
