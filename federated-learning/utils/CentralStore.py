import logging
import threading

from utils.util import ColoredLogger

lock = threading.Lock()

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("CountStore")


class NextRoundCount:
    def __init__(self):
        self.next_round_count_num = 0

    def add_count(self, count_target):
        reach_target = False
        lock.acquire()
        self.next_round_count_num += 1
        if self.next_round_count_num == count_target:
            reach_target = True
        lock.release()
        logger.debug("Added next_round_count, now: {}".format(self.next_round_count_num))
        return reach_target

    def reset(self):
        lock.acquire()
        self.next_round_count_num = 0
        lock.release()
        logger.debug("Reset next_round_count, now: {}".format(self.next_round_count_num))


class ShutdownCount:
    def __init__(self):
        self.shutdown_count_num = 0

    def add_count(self, count_target):
        reach_target = False
        lock.acquire()
        self.shutdown_count_num += 1
        if self.shutdown_count_num == count_target:
            reach_target = True
        lock.release()
        logger.debug("Added shutdown_count_num, now: {}".format(self.shutdown_count_num))
        return reach_target

    def reset(self):
        lock.acquire()
        self.shutdown_count_num = 0
        lock.release()
        logger.debug("Reset shutdown_count_num, now: {}".format(self.shutdown_count_num))


class IPCount:
    def __init__(self):
        self.ipMap = {}
        self.uuid = 0

    def get_new_id(self):
        lock.acquire()
        self.uuid += 1
        new_id = self.uuid
        lock.release()
        return new_id

    def get_keys(self):
        return self.ipMap.keys()

    def get_map(self, key):
        return self.ipMap[key]

    def set_map(self, key, value):
        lock.acquire()
        self.ipMap[key] = value
        lock.release()
