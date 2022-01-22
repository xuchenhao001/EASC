import copy
import logging
import threading

from utils.util import ColoredLogger, compress_tensor, generate_md5_hash

lock = threading.Lock()

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("ModelStore")


class ModelStore:
    def __init__(self):
        self.local_models_count_num = 0
        self.local_models = {}
        self.global_model = None
        self.global_model_compressed = None
        self.global_model_hash = None
        self.global_model_version = -1
        # for customized local model
        self.my_local_model = None
        self.acc_alpha_count_num = 0
        self.acc_alpha_maps = {}

    def local_models_add_count(self, local_uuid, w_local, count_target):
        reach_target = False
        lock.acquire()
        self.local_models[local_uuid] = w_local
        self.local_models_count_num += 1
        if self.local_models_count_num == count_target:
            reach_target = True
        lock.release()
        logger.debug("Count local_models: {}. Gathered {} local models in total".format(self.local_models_count_num,
                                                                                        len(self.local_models)))
        return reach_target

    def local_models_reset(self):
        lock.acquire()
        self.local_models = {}
        self.local_models_count_num = 0
        lock.release()
        logger.debug("Reset local_models, now: {}".format(len(self.local_models)))

    def acc_alpha_add_count(self, local_uuid, acc_alpha_map, count_target):
        reach_target = False
        lock.acquire()
        self.acc_alpha_maps[local_uuid] = acc_alpha_map
        self.acc_alpha_count_num += 1
        if self.acc_alpha_count_num == count_target:
            reach_target = True
        lock.release()
        logger.debug("Received acc_alpha_map: {} in total".format(self.acc_alpha_count_num))
        return reach_target

    def acc_alpha_reset(self):
        lock.acquire()
        self.acc_alpha_maps = {}
        self.acc_alpha_count_num = 0
        lock.release()
        logger.debug("Reset acc_alpha_maps, now: {}".format(len(self.local_models)))

    def update_global_model(self, w_glob, epochs=None):
        self.global_model = w_glob
        self.global_model_compressed = compress_tensor(w_glob)
        self.global_model_hash = generate_md5_hash(w_glob)
        if epochs is None:
            self.global_model_version += 1
        else:
            self.global_model_version = epochs


class APFLModelStore(ModelStore):
    def __init__(self):
        ModelStore.__init__(self)
        # for apfl
        self.difference1 = None
        self.difference2 = None
        self.w_glob = None
        self.w_glob_local = None
        self.w_glob_local_compressed = None
        self.w_locals = None
        self.w_locals_per = None

    def update_w_glob(self, w_glob):
        self.w_glob = copy.deepcopy(w_glob)

    def update_w_glob_local(self, w_glob_local):
        self.w_glob_local = copy.deepcopy(w_glob_local)
        self.w_glob_local_compressed = compress_tensor(w_glob_local)

    def update_w_locals(self, w_locals):
        self.w_locals = copy.deepcopy(w_locals)

    def update_w_locals_per(self, w_locals_per):
        self.w_locals_per = copy.deepcopy(w_locals_per)

    def update_difference1(self, difference1):
        self.difference1 = copy.deepcopy(difference1)

    def update_difference2(self, difference2):
        self.difference2 = copy.deepcopy(difference2)
