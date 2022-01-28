import logging
import time

from utils.ModelStore import PersonalModelStore, APFLPersonalModelStore
from utils.util import model_loader, ColoredLogger, test_model, train_model, record_log, reset_communication_time

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("Trainer")


class Trainer:
    def __init__(self):
        self.net_glob = None
        self.model_store = PersonalModelStore()
        self.init_time = time.time()
        self.round_start_time = time.time()
        self.round_train_duration = 0
        self.round_test_duration = 0
        self.epoch = 1
        self.uuid = -1
        # for committee election
        self.committee_elect_duration = 0

    def init_model(self, model, dataset, device, image_shape):
        self.net_glob = model_loader(model, dataset, device, image_shape)
        if self.net_glob is None:
            logger.error('Error: unrecognized model')
            return False
        return True

    def load_model(self, w):
        self.net_glob.load_state_dict(w)

    def dump_model(self):
        return self.net_glob.state_dict()

    def evaluate_model(self, dataset, args):
        self.net_glob.eval()
        acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4 = \
            test_model(self.net_glob, dataset, self.uuid - 1, args.local_test_bs, args.device)
        return acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4

    def evaluate_model_loss(self, dataset, args):
        self.net_glob.eval()
        loss_local, loss_local_skew1, loss_local_skew2, loss_local_skew3, loss_local_skew4 = \
            test_model(self.net_glob, dataset, self.uuid - 1, args.local_test_bs, args.device, get_acc=False)
        return loss_local, loss_local_skew1, loss_local_skew2, loss_local_skew3, loss_local_skew4

    def evaluate_model_with_log(self, dataset, args, record_epoch=None, clean=False, record_communication_time=False):
        if record_epoch is None:
            record_epoch = self.epoch
        communication_duration = 0
        if record_communication_time:
            communication_duration = reset_communication_time()
            communication_duration += self.committee_elect_duration
        if communication_duration < 0.001:
            communication_duration = 0.0
        test_start_time = time.time()
        acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4 = self.evaluate_model(dataset,
                                                                                                            args)
        test_duration = time.time() - test_start_time
        test_duration += self.round_test_duration
        total_duration = time.time() - self.init_time
        round_duration = time.time() - self.round_start_time
        train_duration = self.round_train_duration
        record_log(self.uuid, record_epoch,
                   [total_duration, round_duration, train_duration, test_duration, communication_duration],
                   [acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4], clean=clean)
        return acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4

    def is_first_epoch(self):
        return self.epoch == 1

    def train(self, dataset, args):
        w_local, loss = train_model(self.net_glob, dataset, self.uuid - 1, args.local_ep, args.device, args.lr,
                                    args.momentum, args.local_bs)
        return w_local, loss


class APFLTrainer(Trainer):
    def __init__(self):
        super().__init__()
        self.hyper_para = 0
        self.model_store = APFLPersonalModelStore()
