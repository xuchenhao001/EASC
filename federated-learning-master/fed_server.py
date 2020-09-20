#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import asyncio

import matplotlib
import json

matplotlib.use('Agg')
import copy
import numpy as np
from threading import Thread
from torchvision import datasets, transforms
import torch

from utils.sampling import mnist_iid, mnist_noniid, cifar_iid
from utils.options import args_parser
from models.Update import LocalUpdate
from models.Nets import MLP, CNNMnist, CNNCifar
from models.Fed import FedAvg
from models.test import test_img

from tornado import gen, httpclient, ioloop, web

url = "http://localhost:3000/invoke/mychannel/fabcar"
# url = "http://localhost:3000/test/echo"
total_epochs = 10
args = None
net_glob = None
dataset_train = None
dataset_test = None
dict_users = None


def test(data):
    detail = {"data": data}
    return "yes", detail


@gen.coroutine
def http_client_post(json_body, message="None"):
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


# STEP #1
# Federated Learning: init step
async def prepare():
    global args
    global net_glob
    global dataset_train
    global dataset_test
    global dict_users
    # parse args
    args = args_parser()
    args.device = torch.device('cpu')

    # load dataset and split users
    if args.dataset == 'mnist':
        trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
        dataset_train = datasets.MNIST('../data/mnist/', train=True, download=True, transform=trans_mnist)
        dataset_test = datasets.MNIST('../data/mnist/', train=False, download=True, transform=trans_mnist)
        # sample users
        if args.iid:
            dict_users = mnist_iid(dataset_train, 1)
        else:
            dict_users = mnist_noniid(dataset_train, 1)
    elif args.dataset == 'cifar':
        trans_cifar = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        dataset_train = datasets.CIFAR10('../data/cifar', train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10('../data/cifar', train=False, download=True, transform=trans_cifar)
        if args.iid:
            dict_users = cifar_iid(dataset_train, 1)
        else:
            exit('Error: only consider IID setting in CIFAR10')
    else:
        exit('Error: unrecognized dataset')
    img_size = dataset_train[0][0].shape
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
    net_glob.train()  # one node do this
    # copy weights
    w_glob = net_glob.state_dict() # change model to parameters
    # upload w_glob onto blockchian
    convert_tensor_value_to_numpy(w_glob)
    print("##### Epoch #", total_epochs, " start now. #####")
    body_data = {
        'message': 'prepare',
        'data': {
            'w_glob': w_glob,
        },
        'epochs': total_epochs
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(json_body, 'prepare')
    print(response)


# STEP #3
# Federated Learning: train step
async def train(data, uuid, epochs):
    print('train data now for uuid: ' + uuid)
    w_glob = data.get("w_glob")
    conver_json_value_to_tensor(w_glob)
    net_glob.load_state_dict(w_glob)
    # local = LocalUpdate(args=args, dataset=dataset_train, idxs=dict_users[idx])
    local = LocalUpdate(args=args, dataset=dataset_train, idxs=dict_users[0])
    w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
    convert_tensor_value_to_numpy(w)
    body_data = {
        'message': 'train',
        'data': {
            'w': w,
        },
        'uuid': uuid,
        'epochs': epochs,
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(json_body, 'train')
    print(response)


# STEP #4
# Federated Learning: average w for w_glob
async def average(w_map, uuid, epochs):
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
    }
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    response = await http_client_post(json_body, 'w_glob')
    print(response)
    # start new thread for step #5
    thread_negotiate = myNegotiateThread(uuid, w_glob, w_local, epochs)
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
        # negotiate(self.my_uuid, self.w_glob, self.w_local)
        print("end my negotiate thread: " + self.my_uuid)


async def negotiate(my_uuid, w_glob, w_local, epochs):
    print("start negotiate for user: " + my_uuid)
    hyperpara_min = 0.5
    hyperpara_max = 0.8
    negotiate_round = 10

    negotiate_step = (hyperpara_max - hyperpara_min) / negotiate_round
    negotiate_step_list = np.arange(hyperpara_min, hyperpara_max, negotiate_step)
    alpha_list = []
    acc_test_list = []
    for alpha in negotiate_step_list:
        w_local2 = {}
        for key in w_glob.keys():
            w_local2[key] = alpha * w_local[key] + (1 - alpha) * w_glob[key]

        # change parameters to model
        net_glob.load_state_dict(w_local2)
        net_glob.eval()
        # test the accuracy
        acc_test, loss_test = test_img(net_glob, dataset_test, args)
        alpha_list.append(alpha)
        acc_test_list.append(acc_test.numpy().item(0))
        print("myuuid: " + my_uuid + ", alpha: " + str(alpha) + ", acc_test result: ", acc_test.numpy().item(0))

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
    response = await http_client_post(json_body, 'negotiate')
    print(response)


# STEP #7
# Federated Learning: with new alpha, train w_local2, restart the round
async def next_round(data, uuid, epochs):
    print('received alpha, train new w_glob for uuid: ' + uuid)
    alpha = data.get("alpha")
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
    if new_epochs > 0:
        print("##### Epoch #", new_epochs, " start now. #####")
        await train(data, uuid, new_epochs)
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
        data[key] = value.numpy()


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
            await train(data.get("data"), data.get("uuid"), data.get("epochs"))
        elif message == "average":
            await average(data.get("data"), data.get("uuid"), data.get("epochs"))
        elif message == "alpha":
            await next_round(data.get("data"), data.get("uuid"), data.get("epochs"))


def make_app():
    return web.Application([
        (r"/messages", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("start serving at 8888...")
    ioloop.IOLoop.current().start()
