#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import asyncio
import json
import logging
import os
import socket
import sys
import time
import subprocess
import copy
import numpy as np
import threading
import torch
from tornado import httpclient, ioloop, web

from utils.options import args_parser
from models.Update import LocalUpdate
from models.Fed import FedAvg
from models.test import test_img_total
from utils.util import dataset_loader, model_loader

logging.basicConfig(format='%(asctime)s %(message)s')
logger = logging.getLogger("main_fed")

torch.manual_seed(0)
np.random.seed(0)

# TO BE CHANGED
# wait in seconds for other nodes to start
start_wait_time = 15
# federated learning server listen port
fed_listen_port = 8888
# TO BE CHANGED FINISHED

# NOT TO TOUCH VARIABLES BELOW
trigger_url = ""
peer_address_list = []
g_user_id = 0
lock = threading.Lock()
wMap = {}
ipMap = {}
net_glob = None
args = None
dataset_train = None
dataset_test = None
dict_users = []
test_users = []
skew_users = []
g_start_time = {}
g_train_time = {}


# returns variable from sourcing a file
def env_from_sourcing(file_to_source_path, variable_name):
    source = 'source %s && export MYVAR=$(echo "${%s[@]}")' % (file_to_source_path, variable_name)
    dump = '/usr/bin/python3 -c "import os, json; print(os.getenv(\'MYVAR\'))"'
    pipe = subprocess.Popen(['/bin/bash', '-c', '%s && %s' % (source, dump)], stdout=subprocess.PIPE)
    return pipe.stdout.read().decode("utf-8").rstrip()


async def train(user_id, w_glob, start_time, epochs):
    global net_glob
    global args
    global dataset_train
    global dataset_test
    global dict_users
    global test_users
    global skew_users
    if user_id is None:
        user_id = await fetch_user_id()

    # parse args
    args = args_parser()
    args.device = torch.device('cpu')
    logger.setLevel(args.log_level)

    # parse participant number
    args.num_users = len(peer_address_list)

    # the first time to train, init net_glob
    if epochs is None:
        epochs = args.epochs

        dataset_train, dataset_test, dict_users, test_users, skew_users = dataset_loader(args.dataset, args.iid,
                                                                                         args.num_users)
        if dict_users is None:
            logger.error('Error: unrecognized dataset')
            sys.exit()

        img_size = dataset_train[0][0].shape
        net_glob = model_loader(args.model, args.dataset, args.device, args.num_channels, args.num_classes, img_size)
        if net_glob is None:
            logger.error('Error: unrecognized model')
            sys.exit()
    else:
        # load w_glob as net_glob
        net_glob.load_state_dict(w_glob)
        net_glob.eval()

    # training
    train_start_time = time.time()
    local = LocalUpdate(args=args, dataset=dataset_train, idxs=dict_users[user_id - 1])
    w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
    train_time = time.time() - train_start_time
    from_ip = get_ip()
    await upload_local_w(user_id, epochs, w, from_ip, start_time, train_time)


async def gathered_global_w(user_id, epochs, w_glob, start_time, train_time):
    conver_json_value_to_tensor(w_glob)
    net_glob.load_state_dict(w_glob)
    net_glob.eval()

    test_start_time = time.time()
    idx = int(user_id) - 1
    idx_total = [test_users[idx], skew_users[0][idx], skew_users[1][idx], skew_users[2][idx], skew_users[3][idx]]
    correct = test_img_total(net_glob, dataset_test, idx_total, args)
    acc_local = torch.div(100.0 * correct[0], len(test_users[idx]))
    # skew 5%
    acc_local_skew1 = torch.div(100.0 * (correct[0] + correct[1]), (len(test_users[idx]) + len(skew_users[0][idx])))
    # skew 10%
    acc_local_skew2 = torch.div(100.0 * (correct[0] + correct[2]), (len(test_users[idx]) + len(skew_users[1][idx])))
    # skew 15%
    acc_local_skew3 = torch.div(100.0 * (correct[0] + correct[3]), (len(test_users[idx]) + len(skew_users[2][idx])))
    # skew 20%
    acc_local_skew4 = torch.div(100.0 * (correct[0] + correct[4]), (len(test_users[idx]) + len(skew_users[3][idx])))

    test_time = time.time() - test_start_time

    # before start next round, record the time
    filename = "result-record_" + str(user_id) + ".txt"
    # first time clean the file
    if epochs == args.epochs:
        with open(filename, 'w') as f:
            pass

    with open(filename, "a") as time_record_file:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        total_time = time.time() - start_time
        communication_time = total_time - train_time - test_time
        time_record_file.write(current_time + "[" + f"{epochs:0>2}" + "]"
                               + " <Total Time> " + str(total_time)[:8]
                               + " <Train Time> " + str(train_time)[:8]
                               + " <Test Time> " + str(test_time)[:8]
                               + " <Communication Time> " + str(communication_time)[:8]
                               + " <acc_local> " + str(acc_local.item())[:8]
                               + " <acc_local_skew1> " + str(acc_local_skew1.item())[:8]
                               + " <acc_local_skew2> " + str(acc_local_skew2.item())[:8]
                               + " <acc_local_skew3> " + str(acc_local_skew3.item())[:8]
                               + " <acc_local_skew4> " + str(acc_local_skew4.item())[:8]
                               + "\n")

    # start next round of train
    new_epochs = epochs - 1
    if new_epochs > 0:
        logger.info("#################### Epoch #" + str(new_epochs) + " start now ####################")
        # reset a new time for next round
        asyncio.ensure_future(train(user_id, w_glob, time.time(), new_epochs))
    else:
        logger.info("########## ALL DONE! ##########")


class MultiTrainThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(start_wait_time)
        logger.debug("start new thread")
        loop = asyncio.new_event_loop()
        loop.run_until_complete(train(None, None, time.time(), None))
        logger.debug("end thread")


def test(data):
    detail = {"data": data}
    return detail


async def load_user_id():
    lock.acquire()
    global g_user_id
    g_user_id += 1
    detail = {"user_id": g_user_id}
    lock.release()
    return detail


async def release_global_w(epochs):
    lock.acquire()
    global g_user_id
    g_user_id = 0
    lock.release()
    w_glob = FedAvg(wMap[epochs])
    convert_tensor_value_to_numpy(w_glob)
    for user_id in ipMap.keys():
        key = str(user_id) + "-" + str(epochs)
        start_time = g_start_time.get(key)
        train_time = g_train_time.get(key)
        data = {
            'message': 'release_global_w',
            'user_id': user_id,
            'epochs': epochs,
            'w_glob': w_glob,
            'start_time': start_time,
            'train_time': train_time,
        }
        json_body = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
        my_url = "http://" + ipMap[user_id] + ":" + str(fed_listen_port) + "/trigger"
        await http_client_post(my_url, json_body, 'release_global_w')


async def average_local_w(user_id, epochs, w, from_ip, start_time, train_time):
    lock.acquire()
    global wMap
    global ipMap

    global g_start_time
    global g_train_time
    key = str(user_id) + "-" + str(epochs)
    g_start_time[key] = start_time
    g_train_time[key] = train_time

    ipMap[user_id] = from_ip
    conver_json_value_to_tensor(w)
    epochW = wMap.get(epochs)
    if epochW is None:
        wMap[epochs] = [w]
    else:
        epochW.append(w)
        wMap[epochs] = epochW
    lock.release()
    if len(wMap[epochs]) == args.num_users:
        logger.debug("Gathered enough w, average and release them")
        asyncio.ensure_future(release_global_w(epochs))
        # await release_global_w(epochs)


async def http_client_post(url, json_body, message="None"):
    logger.debug("Start http client post [" + message + "] to: " + url)
    method = "POST"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_client = httpclient.AsyncHTTPClient()
    try:
        request = httpclient.HTTPRequest(url=url, method=method, headers=headers, body=json_body, connect_timeout=300,
                                         request_timeout=300)
        response = await http_client.fetch(request)
        logger.debug("[HTTP Success] [" + message + "] SERVICE RESPONSE: %s" % response.body)
        return response.body
    except Exception as e:
        logger.error("[HTTP Error] [" + message + "] SERVICE RESPONSE: %s" % e)
        return None


class MainHandler(web.RequestHandler):

    async def get(self):
        response = {"status": "yes", "detail": "test"}
        in_json = json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
        self.set_header("Content-Type", "application/json")
        self.write(in_json)

    async def post(self):
        data = json.loads(self.request.body)
        status = "yes"
        detail = {}
        self.set_header("Content-Type", "application/json")

        message = data.get("message")
        if message == "test":
            detail = test(data.get("weight"))
        elif message == "fetch_user_id":
            detail = await load_user_id()
        elif message == "upload_local_w":
            await average_local_w(data.get("user_id"), data.get("epochs"), data.get("w"), data.get("from_ip"),
                                  data.get("start_time"), data.get("train_time"))
        elif message == "release_global_w":
            await gathered_global_w(data.get("user_id"), data.get("epochs"), data.get("w_glob"),
                                    data.get("start_time"), data.get("train_time"))

        response = {"status": status, "detail": detail}
        in_json = json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
        self.write(in_json)


def make_app():
    return web.Application([
        (r"/trigger", MainHandler),
    ])


async def fetch_user_id():
    fetch_data = {
        'message': 'fetch_user_id',
    }
    json_body = json.dumps(fetch_data, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
    response = await http_client_post(trigger_url, json_body, 'fetch_user_id')
    responseObj = json.loads(response)
    detail = responseObj.get("detail")
    user_id = detail.get("user_id")
    return user_id


async def upload_local_w(user_id, epochs, w, from_ip, start_time, train_time):
    convert_tensor_value_to_numpy(w)
    upload_data = {
        'message': 'upload_local_w',
        'user_id': user_id,
        'epochs': epochs,
        'w': w,
        'from_ip': from_ip,
        'start_time': start_time,
        'train_time': train_time,
    }
    json_body = json.dumps(upload_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    await http_client_post(trigger_url, json_body, 'upload_local_w')
    return


def conver_json_value_to_tensor(data):
    for key, value in data.items():
        data[key] = torch.from_numpy(np.array(value))


def convert_tensor_value_to_numpy(data):
    for key, value in data.items():
        data[key] = value.cpu().numpy()


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        logger.debug("Detected IP address: " + IP)
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def main():
    global peer_address_list
    global trigger_url

    # parse network.config and read the peer addresses
    real_path = os.path.dirname(os.path.realpath(__file__))
    peer_address_var = env_from_sourcing(os.path.join(real_path, "../fabric-samples/network.config"), "PeerAddress")
    peer_address_list = peer_address_var.split(' ')
    peer_addrs = [peer_addr.split(":")[0] for peer_addr in peer_address_list]
    peer_header_addr = peer_addrs[0]
    trigger_url = "http://" + peer_header_addr + ":" + str(fed_listen_port) + "/trigger"

    # multi-thread training here
    my_ip = get_ip()
    threads = []
    for addr in peer_addrs:
        if addr == my_ip:
            thread_train = MultiTrainThread()
            threads.append(thread_train)

    # Start all threads
    for thread in threads:
        thread.start()

    app = make_app()
    app.listen(fed_listen_port)
    logger.info("start serving at " + str(fed_listen_port) + "...")
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
