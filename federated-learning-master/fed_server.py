#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import asyncio
import base64
import gzip
import json
import matplotlib
import time

matplotlib.use('Agg')
import copy
import numpy as np
import threading
from threading import Thread
from torchvision import datasets, transforms
import torch

from utils.sampling import mnist_iid, cifar_iid, noniid_onepass
from utils.options import args_parser
from models.Update import LocalUpdate
from models.Nets import MLP, CNNMnist, CNNCifar
from models.Fed import FedAvg
from models.test import test_img, test_img_total

from tornado import httpclient, ioloop, web

np.random.seed(0)

# TO BE CHANGED
# alpha minimum
hyperpara_min = 0.5
# alpha maximum
hyperpara_max = 0.8
# rounds to negotiate alpha
negotiate_round = 10
# total train round
total_epochs = 50
blockchain_server_url = "http://10.137.3.70:3000/invoke/mychannel/fabcar"
trigger_url = "http://10.137.3.70:8888/trigger"
# blockchain_server_url = "http://localhost:3000/invoke/mychannel/fabcar"
# trigger_url = "http://localhost:8888/trigger"
# TO BE CHANGED FINISHED
args = None
net_glob = None
dataset_train = None
dataset_test = None
dict_users = None
idxs_users = None
check_train_ready_map = {}
check_negotiate_ready_map = {}
lock = threading.Lock()
train_users = None
test_users = None
skew_users1 = None
skew_users2 = None
skew_users3 = None
skew_users4 = None
train_count_num = 0
negotiate_count_num = 0
g_start_time = {}
g_train_time = {}
g_test_time = {}


def test(data):
    detail = {"data": data}
    return "yes", detail


async def http_client_post(url, json_body, message="None"):
    print("Start http client post [" + message + "] to: " + url)
    method = "POST"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_client = httpclient.AsyncHTTPClient()
    try:
        request = httpclient.HTTPRequest(url=url, method=method, headers=headers, body=json_body, connect_timeout=300,
                                         request_timeout=300)
        response = await http_client.fetch(request)
        print("[HTTP Success] [" + message + "] from " + url + " SERVICE RESPONSE: %s" % response.body)
        return response.body
    except Exception as e:
        print("[HTTP Error] [" + message + "] from " + url + " SERVICE RESPONSE: %s" % e)
        return None


# STEP #1.1
# Federated Learning: init step
def init():
    global args
    global net_glob
    global dataset_train
    global dataset_test
    global dict_users
    global idxs_users
    global train_users
    global test_users
    global skew_users1
    global skew_users2
    global skew_users3
    global skew_users4
    # parse args
    args = args_parser()
    args.device = torch.device('cuda:{}'.format(args.gpu) if torch.cuda.is_available() and args.gpu != -1 else 'cpu')

    # load dataset and split users
    if args.dataset == 'mnist':
        trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
        dataset_train = datasets.MNIST('../data/mnist/', train=True, download=True, transform=trans_mnist)
        dataset_test = datasets.MNIST('../data/mnist/', train=False, download=True, transform=trans_mnist)
        # sample users
        if args.iid:
            # dict_users = mnist_iid(dataset_train, 1)
            dict_users = mnist_iid(dataset_train, args.num_users)
        else:
            dict_users, test_users, skew_users1, skew_users2, skew_users3, skew_users4 = noniid_onepass(dataset_train,
                                                                                                        dataset_test,
                                                                                                        args.num_users)
    elif args.dataset == 'cifar':
        trans_cifar = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        dataset_train = datasets.CIFAR10('../data/cifar', train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10('../data/cifar', train=False, download=True, transform=trans_cifar)
        if args.iid:
            # dict_users = cifar_iid(dataset_train, 1)
            dict_users = cifar_iid(dataset_train, args.num_users)
        else:
            dict_users, test_users, skew_users1, skew_users2, skew_users3, skew_users4 = noniid_onepass(dataset_train,
                                                                                                        dataset_test,
                                                                                                        args.num_users)
            # exit('Error: only consider IID setting in CIFAR10')
    else:
        exit('Error: unrecognized dataset')
    img_size = dataset_train[0][0].shape

    m = max(int(args.frac * args.num_users), 1)
    idxs_users = np.random.choice(range(args.num_users), m, replace=False)

    # build model, init part
    if args.model == 'cnn' and args.dataset == 'cifar':
        net_glob = CNNCifar(args=args).to(args.device)
    elif args.model == 'cnn' and args.dataset == 'mnist':
        net_glob = CNNMnist(args=args).to(args.device)
    elif args.model == 'mlp':
        len_in = 1
        for x in img_size:
            len_in *= x
        net_glob = MLP(dim_in=len_in, dim_hidden=64, dim_out=args.num_classes).to(args.device)
    else:
        exit('Error: unrecognized model')
    net_glob.train()


# STEP #1.2
async def prepare():
    # copy weights
    w_glob = net_glob.state_dict()  # change model to parameters
    # upload w_glob onto blockchian
    convert_tensor_value_to_numpy(w_glob)
    w_glob_compressed = compress_data(w_glob)
    print("####################\nEpoch #", total_epochs, " start now\n####################")
    body_data = {
        'message': 'prepare',
        'data': {
            'w_glob': w_glob_compressed,
            'user_number': args.num_users,
        },
        'epochs': total_epochs
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    await http_client_post(blockchain_server_url, json_body, 'prepare_bc')


# STEP #3
# Federated Learning: train step
async def train(data, uuid, epochs, start_time):
    print('train data now for user: ' + uuid)
    w_glob = data.get("w_glob")
    decompressed_w_glob = decompress_data(w_glob)
    conver_json_value_to_tensor(decompressed_w_glob)
    net_glob.load_state_dict(decompressed_w_glob)

    idx = int(uuid) - 1
    local = LocalUpdate(args=args, dataset=dataset_train, idxs=dict_users[idx])
    train_start_time = time.time()
    w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
    train_time = time.time() - train_start_time
    convert_tensor_value_to_numpy(w)
    w_compressed = compress_data(w)
    body_data = {
        'message': 'train',
        'data': {
            'w': w_compressed,
        },
        'uuid': uuid,
        'epochs': epochs,
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    await http_client_post(blockchain_server_url, json_body, 'train_bc')
    trigger_data = {
        'message': 'train_ready',
        'epochs': epochs,
        'uuid': uuid,
        'start_time': start_time,
        'train_time': train_time,
    }
    json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    await http_client_post(trigger_url, json_body, 'train_ready')


# STEP #4
# Federated Learning: average w for w_glob
async def average(w_map, uuid, epochs):
    print('received average request.')
    wArray = []
    for i in w_map.keys():
        w = w_map[i].get("w")
        decompressed_w = decompress_data(w)
        conver_json_value_to_tensor(decompressed_w)
        wArray.append(decompressed_w)
    w_glob = FedAvg(wArray)
    w_local = w_map[uuid].get("w")
    decompressed_w_local = decompress_data(w_local)
    conver_json_value_to_tensor(decompressed_w_local)

    # upload w_glob to blockchain here
    convert_tensor_value_to_numpy(w_glob)
    w_glob_compressed = compress_data(w_glob)
    body_data = {
        'message': 'w_glob',
        'data': {
            'w_glob': w_glob_compressed,
        },
        'uuid': uuid,
        'epochs': epochs,
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    await http_client_post(blockchain_server_url, json_body, 'w_glob_bc')
    # start new thread for step #5
    thread_negotiate = myNegotiateThread(uuid, w_glob, decompressed_w_local, epochs)
    thread_negotiate.start()


# STEP #5
# Federated Learning: negotiate and test accuracy, upload to blockchain
class myNegotiateThread(Thread):
    def __init__(self, my_uuid, w_glob, w_local, epochs):
        Thread.__init__(self)
        self.my_uuid = my_uuid
        self.w_glob = w_glob
        self.w_local = w_local
        self.epochs = epochs

    def run(self):
        print("start my negotiate thread: " + self.my_uuid)
        loop = asyncio.new_event_loop()
        loop.run_until_complete(negotiate(self.my_uuid, self.w_glob, self.w_local, self.epochs))
        print("end my negotiate thread: " + self.my_uuid)


async def negotiate(my_uuid, w_glob, w_local, epochs):
    print("start negotiate for user: " + my_uuid)

    negotiate_step = (hyperpara_max - hyperpara_min) / negotiate_round
    negotiate_step_list = np.arange(hyperpara_min, hyperpara_max, negotiate_step)
    alpha_list = []
    acc_test_list = []
    test_start_time = time.time()
    for alpha in negotiate_step_list:
        w_local2 = {}
        for key in w_glob.keys():
            w_local2[key] = alpha * w_local[key] + (1 - alpha) * w_glob[key]

        # change parameters to model
        net_glob.load_state_dict(w_local2)
        net_glob.eval()
        # test the accuracy
        idx = int(my_uuid) - 1
        acc_test, loss_test = test_img(net_glob, dataset_test, test_users[idx], args)
        alpha_list.append(alpha)
        acc_test_list.append(acc_test.numpy().item(0))
        print("myuuid: " + my_uuid + ", alpha: " + str(alpha) + ", acc_test result: ", acc_test.numpy().item(0))

    test_time = time.time() - test_start_time
    # send acc_test_list and alpha_list to smart contract
    body_data = {
        'message': 'negotiate',
        'data': {
            'acc_test': acc_test_list,
            'alpha': alpha_list,
        },
        'uuid': my_uuid,
        'epochs': epochs,
    }
    print('negotiate finished, send acc_test and alpha to blockchain for uuid: ' + my_uuid)
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    await http_client_post(blockchain_server_url, json_body, 'negotiate_bc')
    trigger_data = {
        'message': 'negotiate_ready',
        'epochs': epochs,
        'uuid': my_uuid,
        'test_time': test_time,
    }
    json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    await http_client_post(trigger_url, json_body, 'negotiate_ready')


# STEP #7
# Federated Learning: with new alpha, train w_local2, restart the round
async def next_round(data, uuid, epochs):
    print('received alpha, train new w_glob for uuid: ' + uuid)
    alpha = data.get("alpha")
    accuracy = data.get("accuracy")
    w_map = data.get("wMap")
    w_glob_map = data.get("wGlobMap")
    w_local = w_map[uuid].get("w")
    w_glob = w_glob_map[uuid].get("w_glob")
    decompressed_w_local = decompress_data(w_local)
    conver_json_value_to_tensor(decompressed_w_local)
    decompressed_w_glob = decompress_data(w_glob)
    conver_json_value_to_tensor(decompressed_w_glob)
    # calculate new w_glob (w_local2) according to the alpha
    w_local2 = {}
    for key in decompressed_w_glob.keys():
        w_local2[key] = alpha * decompressed_w_local[key] + (1 - alpha) * decompressed_w_glob[key]

    # start next round! Go to STEP #3
    convert_tensor_value_to_numpy(w_local2)
    compressed_w_local2 = compress_data(w_local2)
    data = {
        'w_glob': compressed_w_local2,
    }
    # epochs count backwards until 0
    new_epochs = epochs - 1
    # fetch time record
    fetch_data = {
        'message': 'fetch_time',
        'uuid': uuid,
        'epochs': epochs,
    }
    json_body = json.dumps(fetch_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(trigger_url, json_body, 'fetch_time')
    responseObj = json.loads(response)
    detail = responseObj.get("detail")
    start_time = detail.get("start_time")
    test_time = detail.get("test_time")
    train_time = detail.get("train_time")

    # finally, test the acc_local, acc_local_skew1~4
    conver_json_value_to_tensor(w_local2)
    net_glob.load_state_dict(w_local2)
    net_glob.eval()
    test_addition_start_time = time.time()
    idx = int(uuid) - 1
    idx_total = [test_users[idx], skew_users1[idx], skew_users2[idx], skew_users3[idx], skew_users4[idx]]
    correct = test_img_total(net_glob, dataset_test, idx_total, args)
    acc_local = torch.div(100.0 * correct[0], len(test_users[idx]))
    # skew 5%
    acc_local_skew1 = torch.div(100.0 * (correct[0] + correct[1]), (len(test_users[idx]) + len(skew_users1[idx])))
    # skew 10%
    acc_local_skew2 = torch.div(100.0 * (correct[0] + correct[2]), (len(test_users[idx]) + len(skew_users2[idx])))
    # skew 15%
    acc_local_skew3 = torch.div(100.0 * (correct[0] + correct[3]), (len(test_users[idx]) + len(skew_users3[idx])))
    # skew 20%
    acc_local_skew4 = torch.div(100.0 * (correct[0] + correct[4]), (len(test_users[idx]) + len(skew_users4[idx])))
    test_addition_time = time.time() - test_addition_start_time
    test_time += test_addition_time

    # before start next round, record the time
    filename = "result-record_" + uuid + ".txt"
    # first time clean the file
    if epochs == total_epochs:
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
                               + " <Alpha> " + str(alpha)[:8]
                               + " <acc_local> " + str(acc_local.item())[:8]
                               + " <acc_local_skew1> " + str(acc_local_skew1.item())[:8]
                               + " <acc_local_skew2> " + str(acc_local_skew2.item())[:8]
                               + " <acc_local_skew3> " + str(acc_local_skew3.item())[:8]
                               + " <acc_local_skew4> " + str(acc_local_skew4.item())[:8]
                               + "\n")
    if new_epochs > 0:
        print("SLEEP FOR A WHILE...")
        time.sleep(20)
        print("####################\nEpoch #", new_epochs, " start now\n####################")
        # reset a new time for next round
        await train(data, uuid, new_epochs, time.time())
    else:
        print("##########\nALL DONE!\n##########")


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def conver_json_value_to_tensor(data):
    for key, value in data.items():
        data[key] = torch.from_numpy(np.array(value))


def convert_tensor_value_to_numpy(data):
    for key, value in data.items():
        data[key] = value.cpu().numpy()


# compress object to base64 string
def compress_data(data):
    encoded = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode(
        'utf8')
    compressed_data = gzip.compress(encoded)
    b64_encoded = base64.b64encode(compressed_data)
    return b64_encoded.decode('ascii')


# based64 decode to byte, and then decompress it
def decompress_data(data):
    base64_decoded = base64.b64decode(data)
    decompressed = gzip.decompress(base64_decoded)
    return json.loads(decompressed)


class MainHandler(web.RequestHandler):

    async def get(self):
        response = await prepare()
        in_json = json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
        self.set_header("Content-Type", "application/json")
        self.write(in_json)

    async def post(self):
        # reply to smart contract first
        data = json.loads(self.request.body)
        status = "yes"
        detail = {}
        self.set_header("Content-Type", "application/json")
        response = {"status": status, "detail": detail}
        in_json = json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
        self.write(in_json)

        # Then judge message type and process
        message = data.get("message")
        if message == "test":
            test(data.get("data"))
        elif message == "prepare":
            asyncio.ensure_future(train(data.get("data"), data.get("uuid"), data.get("epochs"), time.time()))
        elif message == "average":
            asyncio.ensure_future(average(data.get("data"), data.get("uuid"), data.get("epochs")))
        elif message == "alpha":
            asyncio.ensure_future(next_round(data.get("data"), data.get("uuid"), data.get("epochs")))
        return


async def train_count(epochs, uuid, start_time, train_time):
    lock.acquire()
    global train_count_num
    global g_start_time
    global g_train_time
    train_count_num += 1
    print("Received a train_ready, now: " + str(train_count_num))
    key = str(uuid) + "-" + str(epochs)
    g_start_time[key] = start_time
    g_train_time[key] = train_time
    if train_count_num == args.num_users:
        print("Gathered enough train_ready, send to blockchain server. now: " + str(train_count_num))
        train_count_num = 0
        lock.release()
        # check train read first, since network delay may cause blockchain dirty read.
        while True:
            trigger_data = {
                'message': 'check_train_read',
                'epochs': epochs,
            }
            json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False).encode(
                'utf8')
            response = await http_client_post(blockchain_server_url, json_body, 'check_train_read')
            if response is not None:
                break
            time.sleep(1)  # if dirty read happened, sleep for 1 second then retry.

        # trigger train_ready
        trigger_data = {
            'message': 'train_ready',
            'epochs': epochs,
        }
        json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False).encode(
            'utf8')
        await http_client_post(blockchain_server_url, json_body, 'train_ready_bc')
    else:
        lock.release()


async def negotiate_count(epochs, uuid, test_time):
    lock.acquire()
    global negotiate_count_num
    global g_test_time
    negotiate_count_num += 1
    key = str(uuid) + "-" + str(epochs)
    g_test_time[key] = test_time
    if negotiate_count_num == args.num_users:
        negotiate_count_num = 0
        lock.release()
        # check negotiate read first, since network delay may cause blockchain dirty read.
        while True:
            trigger_data = {
                'message': 'check_negotiate_read',
                'epochs': epochs,
            }
            json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False).encode(
                'utf8')
            response = await http_client_post(blockchain_server_url, json_body, 'check_negotiate_read')
            if response is not None:
                break
            time.sleep(1)  # if dirty read happened, sleep for 1 second then retry.

        trigger_data = {
            'message': 'negotiate_ready',
            'epochs': epochs,
        }
        json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False).encode(
            'utf8')
        await http_client_post(blockchain_server_url, json_body, 'negotiate_ready_bc')
    else:
        lock.release()


async def fetch_time(uuid, epochs):
    key = str(uuid) + "-" + str(epochs)
    start_time = g_start_time.get(key)
    train_time = g_train_time.get(key)
    test_time = g_test_time.get(key)
    detail = {
        "start_time": start_time,
        "train_time": train_time,
        "test_time": test_time,
    }
    return detail


class TriggerHandler(web.RequestHandler):

    async def post(self):
        data = json.loads(self.request.body)
        status = "yes"
        detail = {}
        self.set_header("Content-Type", "application/json")

        message = data.get("message")
        if message == "train_ready":
            await train_count(data.get("epochs"), data.get("uuid"), data.get("start_time"), data.get("train_time"))
        elif message == "negotiate_ready":
            await negotiate_count(data.get("epochs"), data.get("uuid"), data.get("test_time"))
        elif message == "fetch_time":
            detail = await fetch_time(data.get("uuid"), data.get("epochs"))

        response = {"status": status, "detail": detail}
        in_json = json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
        self.write(in_json)


def make_app():
    return web.Application([
        (r"/messages", MainHandler),
        (r"/trigger", TriggerHandler),
    ])


if __name__ == "__main__":
    init()
    app = make_app()
    app.listen(8888)
    print("start serving at 8888...")
    ioloop.IOLoop.current().start()

