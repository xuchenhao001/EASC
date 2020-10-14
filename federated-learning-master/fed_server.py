#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import asyncio

import json
import matplotlib
import time
from random import randrange

matplotlib.use('Agg')
import copy
import numpy as np
import threading
from threading import Thread
from torchvision import datasets, transforms
import torch

from utils.sampling import mnist_iid, mnist_noniid, cifar_iid, noniid_onepass
from utils.options import args_parser
from models.Update import LocalUpdate
from models.Nets import MLP, CNNMnist, CNNCifar
from models.Fed import FedAvg
from models.test import test_img

from tornado import gen, httpclient, ioloop, web

np.random.seed(0)

user_number = 2
blockchain_server_url = "http://localhost:3000/invoke/mychannel/fabcar"
trigger_url = "http://10.0.2.15:8888/trigger"
total_epochs = 50
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


def test(data):
    detail = {"data": data}
    return "yes", detail


@gen.coroutine
def http_client_post(url, json_body, message="None"):
    print("Start http client post: " + message)
    method = "POST"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_client = httpclient.AsyncHTTPClient()
    try:
        request = httpclient.HTTPRequest(url=url, method=method, headers=headers, body=json_body, connect_timeout=300,
                                         request_timeout=300)
        response = yield http_client.fetch(request)
        print("[HTTP Success] [" + message + "] SERVICE RESPONSE: %s" % response.body)
        return response.body
    except Exception as e:
        print("[HTTP Error] [" + message + "] SERVICE RESPONSE: %s" % e)
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
            dict_users = mnist_iid(dataset_train, user_number)
        else:
            dict_users, test_users, skew_users1, skew_users2, skew_users3, skew_users4 = noniid_onepass(dataset_train,
                                                                                                        dataset_test,
                                                                                                        user_number)
    elif args.dataset == 'cifar':
        trans_cifar = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        dataset_train = datasets.CIFAR10('../data/cifar', train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10('../data/cifar', train=False, download=True, transform=trans_cifar)
        if args.iid:
            # dict_users = cifar_iid(dataset_train, 1)
            dict_users = cifar_iid(dataset_train, user_number)
        else:
            dict_users, test_users, skew_users1, skew_users2, skew_users3, skew_users4 = noniid_onepass(dataset_train,
                                                                                                        dataset_test,
                                                                                                        user_number)
            # exit('Error: only consider IID setting in CIFAR10')
    else:
        exit('Error: unrecognized dataset')
    img_size = dataset_train[0][0].shape

    m = max(int(args.frac * user_number), 1)
    idxs_users = np.random.choice(range(user_number), m, replace=False)

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
    print(net_glob)
    net_glob.train()


# STEP #1.2
async def prepare():
    # copy weights
    w_glob = net_glob.state_dict()  # change model to parameters
    # upload w_glob onto blockchian
    convert_tensor_value_to_numpy(w_glob)
    print("\n\n##### Epoch #", total_epochs, " start now. #####\n")
    body_data = {
        'message': 'prepare',
        'data': {
            'w_glob': w_glob,
            'user_number': user_number,
        },
        'start_time': time.time(),
        'train_time': 0,
        'test_time': 0,
        'epochs': total_epochs
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(blockchain_server_url, json_body, 'prepare')
    print(response)


# STEP #3
# Federated Learning: train step
async def train(data, uuid, epochs, start_time):
    print('train data now for user: ' + uuid)
    w_glob = data.get("w_glob")
    conver_json_value_to_tensor(w_glob)
    net_glob.load_state_dict(w_glob)

    idx = int(uuid) - 1
    local = LocalUpdate(args=args, dataset=dataset_train, idxs=dict_users[idx])
    train_start_time = time.time()
    w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
    train_time = time.time() - train_start_time
    convert_tensor_value_to_numpy(w)
    body_data = {
        'message': 'train',
        'data': {
            'w': w,
        },
        'uuid': uuid,
        'epochs': epochs,
        'start_time': start_time,
        'train_time': train_time,
        'test_time': 0,
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(blockchain_server_url, json_body, 'train')
    print(response)
    trigger_data = {
        'message': 'train_ready',
        'epochs': epochs,
        'start_time': start_time,
        'train_time': train_time,
        'test_time': 0,
    }
    json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(trigger_url, json_body, 'train_ready')
    print(response)


# STEP #4
# Federated Learning: average w for w_glob
async def average(w_map, uuid, epochs, start_time, train_time):
    print('received average request.')
    wArray = []
    for i in w_map.keys():
        w = w_map[i].get("w")
        conver_json_value_to_tensor(w)
        wArray.append(w)
    w_glob = FedAvg(wArray)
    w_local = w_map[uuid].get("w")

    # upload w_glob to blockchain here
    convert_tensor_value_to_numpy(w_glob)
    body_data = {
        'message': 'w_glob',
        'data': {
            'w_glob': w_glob,
        },
        'uuid': uuid,
        'epochs': epochs,
        'start_time': start_time,
        'train_time': train_time,
        'test_time': 0,
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(blockchain_server_url, json_body, 'w_glob')
    print(response)
    # start new thread for step #5
    thread_negotiate = myNegotiateThread(uuid, w_glob, w_local, epochs, start_time, train_time)
    thread_negotiate.start()


# STEP #5
# Federated Learning: negotiate and test accuracy, upload to blockchain
class myNegotiateThread(Thread):
    def __init__(self, my_uuid, w_glob, w_local, epochs, start_time, train_time):
        Thread.__init__(self)
        self.my_uuid = my_uuid
        self.w_glob = w_glob
        self.w_local = w_local
        self.epochs = epochs
        self.start_time = start_time
        self.train_time = train_time

    def run(self):
        print("start my negotiate thread: " + self.my_uuid)
        loop = asyncio.new_event_loop()
        loop.run_until_complete(negotiate(self.my_uuid, self.w_glob, self.w_local, self.epochs, self.start_time,
                                          self.train_time))
        # negotiate(self.my_uuid, self.w_glob, self.w_local)
        print("end my negotiate thread: " + self.my_uuid)


async def negotiate(my_uuid, w_glob, w_local, epochs, start_time, train_time):
    print("start negotiate for user: " + my_uuid)
    hyperpara_min = 0.5
    hyperpara_max = 0.8
    negotiate_round = 10

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
        acc_test, loss_test = test_img(net_glob, dataset_test, args, idx=test_users[idx])
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
        'start_time': start_time,
        'train_time': train_time,
        'test_time': test_time,
    }
    print('negotiate finished, send acc_test and alpha to blockchain for uuid: ' + my_uuid)
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(blockchain_server_url, json_body, 'negotiate')
    print(response)
    trigger_data = {
        'message': 'negotiate_ready',
        'epochs': epochs,
        'start_time': start_time,
        'train_time': train_time,
        'test_time': test_time,
    }
    json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(trigger_url, json_body, 'negotiate_ready')
    print(response)


# STEP #7
# Federated Learning: with new alpha, train w_local2, restart the round
async def next_round(data, uuid, epochs, start_time, train_time, test_time):
    print('received alpha, train new w_glob for uuid: ' + uuid)
    alpha = data.get("alpha")
    accuracy = data.get("accuracy")
    w_map = data.get("wMap")
    w_glob_map = data.get("wGlobMap")
    print(w_map.keys())
    print(w_glob_map.keys())
    w_local = w_map[uuid].get("w")
    w_glob = w_glob_map[uuid].get("w_glob")
    conver_json_value_to_tensor(w_local)
    conver_json_value_to_tensor(w_glob)
    # calculate new w_glob (w_local2) according to the alpha
    w_local2 = {}
    for key in w_glob.keys():
        w_local2[key] = alpha * w_local[key] + (1 - alpha) * w_glob[key]

    # start next round! Go to STEP #3
    data = {
        'w_glob': w_local2,
    }
    # epochs count backwards until 0
    new_epochs = epochs - 1
    # before start next round, record the time
    with open("result-record_" + uuid + ".txt", "a") as time_record_file:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        total_time = time.time() - start_time
        communication_time = total_time - train_time - test_time
        time_record_file.write(current_time + "[" + f"{epochs:0>2}" + "]"
                               + " <Total Time> " + str(total_time)[:8]
                               + " <Train Time> " + str(train_time)[:8]
                               + " <Test Time> " + str(test_time)[:8]
                               + " <Communication Time> " + str(communication_time)[:8]
                               + " <Accuracy> " + str(accuracy)[:8]
                               + "\n")
    if new_epochs > 0:
        print("##### Epoch #", new_epochs, " start now. #####")
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
            await train(data.get("data"), data.get("uuid"), data.get("epochs"), data.get("start_time"))
        elif message == "average":
            await average(data.get("data"), data.get("uuid"), data.get("epochs"), data.get("start_time"),
                          data.get("train_time"))
        elif message == "alpha":
            await next_round(data.get("data"), data.get("uuid"), data.get("epochs"), data.get("start_time"),
                             data.get("train_time"), data.get("test_time"))


async def train_count(epochs, start_time, train_time, test_time):
    lock.acquire()
    global train_count_num
    train_count_num += 1
    if train_count_num == user_number:
        train_count_num = 0
        trigger_data = {
            'message': 'train_ready',
            'epochs': epochs,
            'start_time': start_time,
            'train_time': train_time,
            'test_time': 0,
        }
        json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode(
            'utf8')
        response = await http_client_post(blockchain_server_url, json_body, 'train_ready')
        print(response)
    lock.release()


async def negotiate_count(epochs, start_time, train_time, test_time):
    lock.acquire()
    global negotiate_count_num
    negotiate_count_num += 1
    if negotiate_count_num == user_number:
        negotiate_count_num = 0
        trigger_data = {
            'message': 'negotiate_ready',
            'epochs': epochs,
            'start_time': start_time,
            'train_time': train_time,
            'test_time': test_time,
        }
        json_body = json.dumps(trigger_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode(
            'utf8')
        response = await http_client_post(blockchain_server_url, json_body, 'train_ready')
        print(response)
    lock.release()


class TriggerHandler(web.RequestHandler):

    async def post(self):
        data = json.loads(self.request.body)
        status = "yes"
        detail = {}
        self.set_header("Content-Type", "application/json")
        response = {"status": status, "detail": detail}
        in_json = json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
        self.write(in_json)

        message = data.get("message")
        if message == "train_ready":
            await train_count(data.get("epochs"), data.get("start_time"), data.get("train_time"), data.get("test_time"))
        elif message == "negotiate_ready":
            await negotiate_count(data.get("epochs"), data.get("start_time"), data.get("train_time"),
                                  data.get("test_time"))


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
