import logging
import sys
import time
import threading
from flask import Flask, request

import utils.util
from utils.CentralStore import IPCount
from utils.ModelStore import ModelStore
from utils.Trainer import Trainer
from utils.util import ColoredLogger
from models.Fed import fed_avg

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("fedavg")

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

    load_result = trainer.init_model()
    if not load_result:
        sys.exit()

    # trained the initial local model, which will be treated as first global model.
    trainer.net_glob.train()
    # generate md5 hash from model, which is treated as global model of previous round.
    w = trainer.net_glob.state_dict()
    model_store.update_global_model(w, -1)  # -1 means the initial global model


def train():
    if trainer.uuid == -1:
        trainer.uuid = fetch_uuid()
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
        detail = trainer.post_msg_trigger(body_data)
        global_model_compressed = detail.get("global_model")
        w_glob = utils.util.decompress_tensor(global_model_compressed)
        trainer.load_model(w_glob)
        trainer.evaluate_model_with_log(record_epoch=0, clean=True)
    else:
        trainer.load_model(model_store.global_model)

    train_start_time = time.time()
    w_local, w_loss = trainer.train()
    trainer.round_train_duration = time.time() - train_start_time

    # send local model to the first node
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


def receive_global_w(w_glob_compressed):
    logger.debug("Received latest global model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # load hash of new global model, which is downloaded from the leader
    w_glob = utils.util.decompress_tensor(w_glob_compressed)

    # finally, evaluate the global model
    trainer.load_model(w_glob)
    trainer.evaluate_model_with_log(record_communication_time=True)

    # epochs count down to 0
    trainer.epoch += 1
    if trainer.epoch <= trainer.args.epochs:
        train()
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
                threading.Thread(target=receive_global_w, args=(data.get("w_compressed"), )).start()
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
