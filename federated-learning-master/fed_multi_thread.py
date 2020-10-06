#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import asyncio

import matplotlib
import time
import uuid
from random import randrange

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

user_number = 2
total_epochs = 0
args = None
net_glob = None
dataset_train = None
dataset_test = None
dict_users = None
idxs_users = None
w_map = {}
w_glob_map = {}
acc_alpha_map = {}
negotiate_round = 0


def test(data):
    detail = {"data": data}
    return "yes", detail


# STEP #1
# Federated Learning: init step
def prepare():
    global args
    global net_glob
    global dataset_train
    global dataset_test
    global dict_users
    global idxs_users
    global total_epochs
    # parse args
    args = args_parser()
    args.device = torch.device('cpu')
    total_epochs = args.epochs

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
            # dict_users = mnist_noniid(dataset_train, 1)
            dict_users = mnist_noniid(dataset_train, args.num_users)
    elif args.dataset == 'cifar':
        trans_cifar = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        dataset_train = datasets.CIFAR10('../data/cifar', train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10('../data/cifar', train=False, download=True, transform=trans_cifar)
        if args.iid:
            # dict_users = cifar_iid(dataset_train, 1)
            dict_users = cifar_iid(dataset_train, args.num_users)
        else:
            exit('Error: only consider IID setting in CIFAR10')
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
    print(net_glob)
    net_glob.train()  # one node do this
    # copy weights
    w_glob = net_glob.state_dict()  # change model to parameters
    # upload w_glob onto blockchian
    convert_tensor_value_to_numpy(w_glob)
    print("\n\n##### Epoch #", total_epochs, " start now. #####\n")

    # multi-thread training here
    threads = []
    for i in range(thread_number):
        thread_train = MultiTrainThread(str(uuid.uuid4()), w_glob, total_epochs, time.time())
        threads.append(thread_train)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all of threads to finish
    for thread in threads:
        thread.join()


class MultiTrainThread(Thread):
    def __init__(self, my_uuid, w_glob, epochs, start_time):
        Thread.__init__(self)
        self.my_uuid = my_uuid
        self.w_glob = w_glob
        self.epochs = epochs
        self.start_time = start_time

    def run(self):
        print("start multi train thread: " + self.my_uuid)
        loop = asyncio.new_event_loop()
        loop.run_until_complete(train(self.my_uuid, self.w_glob, self.epochs, self.start_time))
        print("end multi train thread: " + self.my_uuid)


# STEP #3
# Federated Learning: train step
async def train(uuid, w_glob, epochs, start_time):
    global w_map
    print('train data now for uuid: ' + uuid)
    conver_json_value_to_tensor(w_glob)
    net_glob.load_state_dict(w_glob)
    idx = idxs_users[randrange(int(args.frac * args.num_users))]  # random select one for each round
    local = LocalUpdate(args=args, dataset=dataset_train, idxs=dict_users[idx])
    w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
    convert_tensor_value_to_numpy(w)
    # save w onto w_map
    w_map[uuid] = {'w': w}

    # wait until w_map full
    while len(w_map.keys()) != thread_number:
        time.sleep(1)
    await average(w_map, uuid, epochs, start_time)


# STEP #4
# Federated Learning: average w for w_glob
async def average(w_map, uuid, epochs, start_time):
    global w_glob_map
    print('received average request.')
    wArray = []
    for i in w_map.keys():
        w = w_map[i].get("w")
        conver_json_value_to_tensor(w)
        wArray.append(w)
    w_glob = FedAvg(wArray)
    w_local = w_map[uuid].get("w")

    # upload w_glob to local file here
    convert_tensor_value_to_numpy(w_glob)
    body_data = {
        'message': 'w_glob',
        'data': {
            'w_glob': w_glob,
        },
        'uuid': uuid,
        'epochs': epochs,
        'start_time': start_time,
    }
    # with open("useless_" + uuid + ".txt", "x") as useless_file:
    #     useless_file.write(json.dumps(body_data))

    # save w_glob onto w_glob_map
    w_glob_map[uuid] = {
        'w_glob': w_glob,
    }

    # wait until w_glob_map full
    while len(w_glob_map.keys()) != thread_number:
        time.sleep(1)
    # start step #5
    await negotiate(uuid, w_glob, w_glob_map, w_local, epochs, start_time)


async def negotiate(uuid, w_glob, w_glob_map, w_local, epochs, start_time):
    global acc_alpha_map
    global negotiate_round
    print("start negotiate for user: " + uuid)
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
        print("myuuid: " + uuid + ", alpha: " + str(alpha) + ", acc_test result: ", acc_test.numpy().item(0))

    # save acc_alpha onto acc_alpha_map
    acc_alpha_map[uuid] = {
        'acc_test': acc_test_list,
        'alpha': alpha_list,
    }

    # wait until acc_alpha_map full
    while len(acc_alpha_map.keys()) != thread_number:
        time.sleep(1)
    best_alpha = find_max_acc_avg(acc_alpha_map)
    await next_round(best_alpha, w_map, w_glob_map, uuid, epochs, start_time)


def find_max_acc_avg(acc_alpha_map):
    print("[Find Alpha] According to max acc_test average policy")
    accTestSum = [0.0] * negotiate_round
    randomUuid = ""
    # calculate sum acc_test for all users into array `accTestSum`
    for key in acc_alpha_map:
        accAlpha = acc_alpha_map[key]
        for i in range(len(accAlpha['acc_test'])):
            accTestSum[i] += accAlpha['acc_test'][i]
        randomUuid = key
    # find out the max value in `accTestSum`, return the alpha of that value.
    max = 0.0
    maxIndex = 0
    for i in range(len(accTestSum)):
        if i == 0 or accTestSum[i] > max:
            max = accTestSum[i]
            maxIndex = i
    alpha = acc_alpha_map[randomUuid]['alpha'][maxIndex]
    acc = max/2
    print("Found the max acc_test: ", acc, " with alpha: ", alpha)
    return alpha


# STEP #7
# Federated Learning: with new alpha, train w_local2, restart the round
async def next_round(alpha, w_map, w_glob_map, uuid, epochs, start_time):
    print('received alpha, train new w_glob for uuid: ' + uuid)
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
    with open("time-record_" + uuid + ".txt", "a") as time_record_file:
        time_record_file.write("[" + f"{epochs:0>2}" + "] " + str(time.time() - start_time) + "\n")
    if new_epochs > 0:
        print("##### Epoch #", new_epochs, " start now. #####")
        # reset a new time for next round
        await train(uuid, w_glob, new_epochs, time.time())
    else:
        print("##########\nALL DONE!\n##########")


def conver_json_value_to_tensor(data):
    for key, value in data.items():
        data[key] = torch.from_numpy(np.array(value))


def convert_tensor_value_to_numpy(data):
    for key, value in data.items():
        data[key] = value.numpy()


if __name__ == "__main__":
    prepare()
