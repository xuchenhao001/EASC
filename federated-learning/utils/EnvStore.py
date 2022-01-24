import logging
import torch

from utils.options import args_parser
from utils.util import ColoredLogger, get_ip

logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("EnvStore")


class EnvStore:
    def __init__(self):
        self.trigger_url = ""
        self.from_ip = ""
        self.args = None

    def init(self):
        self.args = args_parser()
        self.args.device = torch.device(
            'cuda:{}'.format(self.args.gpu) if torch.cuda.is_available() and self.args.gpu != -1 else 'cpu')
        self.from_ip = get_ip(self.args.test_ip_addr)
        self.trigger_url = "http://" + self.from_ip + ":" + str(self.args.fl_listen_port) + "/trigger"
        # print parameters in log
        arguments = vars(self.args)
        logger.info("==========================================")
        for k, v in arguments.items():
            arg = "{}: {}".format(k, v)
            logger.info("* {0:<40}".format(arg))
        logger.info("==========================================")
