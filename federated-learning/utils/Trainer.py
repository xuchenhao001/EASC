import logging
import os
import time

import torch

from utils.options import args_parser
from utils.util import model_loader, ColoredLogger, http_client_post, test_model, train_model, record_log, \
    reset_communication_time, env_from_sourcing
from utils.Datasets import MyDataset

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("Train")


class Trainer:
    def __init__(self):
        self.blockchain_server_url = ""
        self.trigger_url = ""
        self.peer_address_list = []
        self.args = None
        self.net_glob = None
        self.dataset = None
        self.init_time = time.time()
        self.round_start_time = time.time()
        self.round_train_duration = 0
        self.epoch = 1
        self.uuid = -1

    def parse_args(self):
        self.args = args_parser()
        self.args.device = torch.device(
            'cuda:{}'.format(self.args.gpu) if torch.cuda.is_available() and self.args.gpu != -1 else 'cpu')
        # read num_users from blockchain
        self.args.num_users = len(self.peer_address_list)
        arguments = vars(self.args)
        logger.info("==========================================")
        for k, v in arguments.items():
            arg = "{}: {}".format(k, v)
            logger.info("* {0:<40}".format(arg))
        logger.info("==========================================")

    def init_urls(self, fed_listen_port):
        # parse network.config and read the peer addresses
        real_path = os.path.dirname(os.path.realpath(__file__))
        self.peer_address_list = env_from_sourcing(os.path.join(real_path, "../../fabric-network/network.config"),
                                                   "PEER_ADDRS").split(" ")
        peer_header_addr = self.peer_address_list[0].split(":")[0]
        # initially the trigger url is load on the first peer
        self.trigger_url = "http://" + peer_header_addr + ":" + str(fed_listen_port) + "/trigger"

    def init_dataset(self):
        self.dataset = MyDataset(self.args.dataset, self.args.dataset_train_size, self.args.iid, self.args.num_users)
        if self.dataset.dataset_train is None:
            logger.error('Error: unrecognized dataset')
            return False
        return True

    def init_model(self):
        img_size = self.dataset.dataset_train[0][0].shape
        self.net_glob = model_loader(self.args.model, self.args.dataset, self.args.device, img_size)
        if self.net_glob is None:
            logger.error('Error: unrecognized model')
            return False
        return True

    def load_model(self, w):
        self.net_glob.load_state_dict(w)

    def dump_model(self):
        return self.net_glob.state_dict()

    def evaluate_model(self):
        self.net_glob.eval()
        acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4 = \
            test_model(self.net_glob, self.dataset, self.uuid - 1, self.args.iid, self.args.local_test_bs,
                       self.args.device)
        return acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4

    def evaluate_model_loss(self):
        self.net_glob.eval()
        loss_local, loss_local_skew1, loss_local_skew2, loss_local_skew3, loss_local_skew4 = \
            test_model(self.net_glob, self.dataset, self.uuid - 1, self.args.iid, self.args.local_test_bs,
                       self.args.device, get_acc=False)
        return loss_local, loss_local_skew1, loss_local_skew2, loss_local_skew3, loss_local_skew4

    def evaluate_model_with_log(self, record_epoch=None, clean=False, record_communication_time=False):
        if record_epoch is None:
            record_epoch = self.epoch
        communication_duration = 0
        if record_communication_time:
            communication_duration = reset_communication_time()
        if communication_duration < 0.001:
            communication_duration = 0.0
        test_start_time = time.time()
        acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4 = self.evaluate_model()
        test_duration = time.time() - test_start_time
        total_duration = time.time() - self.init_time
        round_duration = time.time() - self.round_start_time
        train_duration = self.round_train_duration
        record_log(self.uuid, record_epoch,
                   [total_duration, round_duration, train_duration, test_duration, communication_duration],
                   [acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4], clean=clean)
        return acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4

    def post_msg_trigger(self, body_data):
        response = http_client_post(self.trigger_url, body_data)
        if "detail" in response:
            return response.get("detail")

    def is_first_epoch(self):
        return self.epoch == 1

    def train(self):
        w_local, loss = train_model(self.net_glob, self.dataset, self.uuid - 1, self.args.local_ep, self.args.device,
                                    self.args.lr, self.args.momentum, self.args.local_bs, self.is_first_epoch())
        return w_local, loss

    # for dynamic adjusting server learning rate by multiply 0.1 in every 20 rounds of training
    def server_learning_rate_adjust(self, current_epoch):
        server_lr_decimate_str = self.args.server_lr_decimate.strip()
        if len(server_lr_decimate_str) < 1:
            # if the parameter is empty, do nothing
            return
        server_lr_decimate = list(map(int, list(server_lr_decimate_str.split(","))))
        if int(current_epoch) in server_lr_decimate:
            self.args.server_lr *= 0.1
            logger.info("Decimate the server learning rate to: {}.".format(self.args.server_lr))


class APFLTrainer(Trainer):
    def __init__(self):
        super().__init__()
        self.hyper_para = 0
