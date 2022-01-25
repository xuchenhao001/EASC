import logging
import sys
import time
import threading
from flask import Flask, request

import utils
from utils.CentralStore import IPCount
from utils.DatasetStore import LocalDataset
from utils.EnvStore import EnvStore
from utils.ModelStore import CentralModelStore
from utils.Trainer import Trainer
from utils.util import ColoredLogger

logging.setLoggerClass(ColoredLogger)
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logger = logging.getLogger("local_train")

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
    trainer_pool[trainer.uuid] = trainer
    return trainer.uuid


def train(trainer_uuid):
    trainer = trainer_pool[trainer_uuid]
    logger.debug("Train local model for user: {}, epoch: {}.".format(trainer.uuid, trainer.epoch))

    # training for all epochs
    while trainer.epoch <= env_store.args.epochs:
        logger.info("########## EPOCH #{} ##########".format(trainer.epoch))
        logger.info("Epoch [{}] train for user [{}]".format(trainer.epoch, trainer.uuid))
        trainer.round_start_time = time.time()
        # calculate initial model accuracy, record it as the bench mark.
        if trainer.is_first_epoch():
            trainer.init_time = time.time()
            trainer.evaluate_model_with_log(local_dataset, env_store.args, record_epoch=0, clean=True)

        train_start_time = time.time()
        w_local, _ = trainer.train(local_dataset, env_store.args)
        trainer.round_train_duration = time.time() - train_start_time

        # finally, evaluate the global model
        trainer.load_model(w_local)
        trainer.evaluate_model_with_log(local_dataset, env_store.args, record_communication_time=True)

        trainer.epoch += 1

    logger.info("########## ALL DONE! ##########")
    body_data = {
        "message": "shutdown_python",
        "uuid": trainer.uuid,
        "from_ip": env_store.from_ip,
    }
    utils.util.post_msg_trigger(env_store.trigger_url, body_data)


def start_train():
    time.sleep(env_store.args.start_sleep)
    trainer_uuid = init_trainer()
    train(trainer_uuid)


def load_uuid():
    new_id = ipCount.get_new_id()
    detail = {"uuid": new_id}
    return detail


def fetch_uuid():
    body_data = {
        "message": "fetch_uuid",
    }
    detail = utils.util.post_msg_trigger(env_store.trigger_url, body_data)
    uuid = detail.get("uuid")
    return uuid


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
