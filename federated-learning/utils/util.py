#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import base64
import copy
import gzip
import hashlib
import json
import logging
import os
import socket
import threading
import time

import numpy as np
import requests
import torch

from models.Nets import CNNCifar, CNNMnist, UCI_CNN, MLP, CNNImageNet
from models.Test import test_img_total
from models.Train import train_cnn_mlp
from utils.blockchain import post_to_blockchain

lock = threading.Lock()
# format colorful log output
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
# The background is set with 40 plus the number of the color, and the foreground with 30
# These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED
}


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)


# Custom logger class with multiple destinations
class ColoredLogger(logging.Logger):
    FORMAT = "[$BOLD%(asctime)-20s$RESET][%(levelname)s] %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
    # FORMAT = "%(asctime)s %(message)s"
    COLOR_FORMAT = formatter_message(FORMAT, True)

    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return


logging.setLoggerClass(ColoredLogger)
logger = logging.getLogger("util")


def model_loader(model_name, dataset_name, device, img_size):
    net_glob = None
    # build model, init part
    if model_name == 'cnn' and dataset_name == 'mnist':
        net_glob = CNNMnist(num_classes=10).to(device)
    elif model_name == 'cnn' and dataset_name == 'cifar10':
        net_glob = CNNCifar(num_classes=10).to(device)
    elif model_name == 'cnn' and dataset_name == 'cifar100':
        net_glob = CNNCifar(num_classes=100).to(device)
    elif model_name == 'cnn' and dataset_name == 'imagenet':
        net_glob = CNNImageNet(num_classes=200).to(device)
    elif model_name == 'cnn' and dataset_name == 'uci':
        net_glob = UCI_CNN(num_classes=6).to(device)
    elif model_name == 'cnn' and dataset_name == 'realworld':
        net_glob = UCI_CNN(num_classes=8).to(device)
    elif model_name == 'mlp':
        len_in = 1
        for x in img_size:
            len_in *= x
        net_glob = MLP(dim_in=len_in).to(device)
    return net_glob


def test_model(net_glob, my_dataset, idx, local_test_bs, device, get_acc=True, is_iid=False):
    if is_iid:
        idx_total = [my_dataset.test_users[idx]]
        acc_list, loss_list = test_img_total(net_glob, my_dataset, idx_total, local_test_bs, device)
        acc_local = acc_list[0].item()
        loss_local = loss_list[0].item()
        if get_acc:
            return acc_local, 0.0, 0.0, 0.0, 0.0
        else:
            return loss_local, 0.0, 0.0, 0.0, 0.0
    else:
        idx_total = [my_dataset.test_users[idx], my_dataset.skew_users[0][idx], my_dataset.skew_users[1][idx],
                     my_dataset.skew_users[2][idx], my_dataset.skew_users[3][idx]]
        acc_list, loss_list = test_img_total(net_glob, my_dataset, idx_total, local_test_bs, device)
        acc_local = acc_list[0].item()
        acc_local_skew1 = acc_list[1].item()
        acc_local_skew2 = acc_list[2].item()
        acc_local_skew3 = acc_list[3].item()
        acc_local_skew4 = acc_list[4].item()
        loss_local = loss_list[0].item()
        loss_local_skew1 = loss_list[1].item()
        loss_local_skew2 = loss_list[2].item()
        loss_local_skew3 = loss_list[3].item()
        loss_local_skew4 = loss_list[4].item()
        if get_acc:
            return acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4
        else:
            return loss_local, loss_local_skew1, loss_local_skew2, loss_local_skew3, loss_local_skew4


def train_model(net_glob, my_dataset, idx, local_ep, device, lr, momentum, local_bs):
    net_glob_cp = copy.deepcopy(net_glob).to(device)
    return train_cnn_mlp(net_glob_cp, my_dataset, idx, local_ep, device, lr, momentum, local_bs)


def http_client_post(url, body_data, accumulate_time=True):
    logger.debug("[HTTP Start] [" + body_data['message'] + "] Start http client post to: " + url)
    request_start_time = time.time()
    response = requests.post(url, json=body_data, timeout=300)
    logger.debug("[HTTP Success] [" + body_data['message'] + "] from " + url)
    request_time = time.time() - request_start_time
    if accumulate_time:
        add_communication_time(request_time)
    return response.json()


def simu_http_post(url, body_data, node_num, accumulate_time=True):
    logger.debug("[SIMU HTTP Start] [" + body_data['message'] + "] Start http client post to: " + url)
    request_start_time = time.time()
    post_to_blockchain(node_num)
    logger.debug("[SIMU HTTP Success] [" + body_data['message'] + "] from " + url)
    request_time = time.time() - request_start_time
    if accumulate_time:
        add_communication_time(request_time)


accumulate_communication_time = 0


def add_communication_time(request_time):
    global accumulate_communication_time
    lock.acquire()
    accumulate_communication_time += request_time
    lock.release()


def reset_communication_time():
    global accumulate_communication_time
    lock.acquire()
    communication_time = accumulate_communication_time
    accumulate_communication_time = 0
    lock.release()
    return communication_time


def post_msg_trigger(trigger_url, body_data):
    response = http_client_post(trigger_url, body_data)
    if "detail" in response:
        return response.get("detail")


def post_msg_blockchain(body_data, num_users):
    simu_http_post("blockchain", body_data, num_users)


def __conver_numpy_value_to_tensor(numpy_data):
    tensor_data = copy.deepcopy(numpy_data)
    for key, value in tensor_data.items():
        tensor_data[key] = torch.from_numpy(np.array(value))
    return tensor_data


def __convert_tensor_value_to_numpy(tensor_data):
    numpy_data = copy.deepcopy(tensor_data)
    for key, value in numpy_data.items():
        numpy_data[key] = value.cpu().numpy()
    return numpy_data


# compress object to base64 string
def __compress_data(data):
    encoded = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode(
        'utf8')
    compressed_data = gzip.compress(encoded)
    b64_encoded = base64.b64encode(compressed_data)
    return b64_encoded.decode('ascii')


# based64 decode to byte, and then decompress it
def __decompress_data(data):
    base64_decoded = base64.b64decode(data)
    decompressed = gzip.decompress(base64_decoded)
    return json.loads(decompressed)


# compress the tensor data
def compress_tensor(data):
    compressed_data = __compress_data(__convert_tensor_value_to_numpy(data))
    return compressed_data


# decompress the data into tensor
def decompress_tensor(data):
    tensor_data = __conver_numpy_value_to_tensor(__decompress_data(data))
    return tensor_data


# generate md5 hash for global model. Require a tensor type gradients.
def generate_md5_hash(model_weights):
    np_model_weights = __convert_tensor_value_to_numpy(model_weights)
    data_md5 = hashlib.md5(json.dumps(np_model_weights, sort_keys=True, cls=NumpyEncoder).encode('utf-8')).hexdigest()
    return data_md5


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def get_ip(test_ip_addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        # s.connect(('10.255.255.255', 1))
        s.connect((test_ip_addr, 1))
        ip = s.getsockname()[0]
        logger.debug("Detected IP address: " + ip)
    except socket.error:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


# here starts built in functions
shutdown_count_num = 0
ipMap = {}


def shutdown_count(uuid, from_ip, fed_listen_port, num_users):
    lock.acquire()
    global shutdown_count_num
    global ipMap
    shutdown_count_num += 1
    ipMap[uuid] = from_ip
    lock.release()
    if shutdown_count_num == num_users:
        # send request to shut down the python
        body_data = {
            'message': 'shutdown',
        }
        logger.debug('Send shutdown python request.')
        for uuid in ipMap.keys():
            client_url = "http://" + ipMap[uuid] + ":" + str(fed_listen_port) + "/trigger"
            http_client_post(client_url, body_data)


# time_list: [total_time, round_time, train_time, test_time, commu_time]
# acc_list: [acc_local, acc_local_skew1, acc_local_skew2, acc_local_skew3, acc_local_skew4]  (for cnn or mlp)
def record_log(user_id, epoch, time_list, acc_list, clean=False):
    filename = "result-record_" + str(user_id) + ".txt"

    # first time clean the file
    if clean:
        open(filename, 'w').close()

    with open(filename, "a") as time_record_file:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        time_record_file.write(current_time + "[" + "{:03d}".format(epoch) + "]"
                               + " <Total Time> " + str(time_list[0])[:8]
                               + " <Round Time> " + str(time_list[1])[:8]
                               + " <Train Time> " + str(time_list[2])[:8]
                               + " <Test Time> " + str(time_list[3])[:8]
                               + " <Communication Time> " + str(time_list[4])[:8]
                               + " <acc_local> " + str(acc_list[0])[:8]
                               + " <acc_local_skew1> " + str(acc_list[1])[:8]
                               + " <acc_local_skew2> " + str(acc_list[2])[:8]
                               + " <acc_local_skew3> " + str(acc_list[3])[:8]
                               + " <acc_local_skew4> " + str(acc_list[4])[:8]
                               + "\n")


def my_exit(exit_sleep):
    time.sleep(exit_sleep)  # sleep for a while before exit
    logger.info("########## PYTHON SHUTTING DOWN! ##########")
    os._exit(0)
