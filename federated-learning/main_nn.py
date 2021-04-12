#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import asyncio
import os
import subprocess

import matplotlib
import threading
from threading import Thread
import time
import socket

matplotlib.use('Agg')
import copy
import numpy as np
from torchvision import datasets, transforms
import torch
import json
from tornado import httpclient, ioloop, web

from utils.sampling import mnist_iid, mnist_noniid, cifar_iid, noniid_onepass
from utils.options import args_parser
from models.Update import LocalUpdate
from models.Nets import MLP, CNNMnist, CNNCifar
from models.test import test_img_total

torch.manual_seed(0)
np.random.seed(0)

# TO BE CHANGED
# federated learning server listen port
fed_listen_port = 8888
# TO BE CHANGED FINISHED

# NOT TO TOUCH VARIABLES BELOW
trigger_url = ""
peer_address_list = []
g_user_id = 0
lock = threading.Lock()


# returns variable from sourcing a file
def env_from_sourcing(file_to_source_path, variable_name):
    source = 'source %s && export MYVAR=$(echo "${%s[@]}")' % (file_to_source_path, variable_name)
    # dump = '/usr/bin/python3 -c "import os, json; print(json.dumps(dict(os.getenv(\'MYVAR\'))))"'
    dump = '/usr/bin/python3 -c "import os, json; print(os.getenv(\'MYVAR\'))"'
    pipe = subprocess.Popen(['/bin/bash', '-c', '%s && %s' % (source, dump)], stdout=subprocess.PIPE)
    # return json.loads(pipe.stdout.read())
    return pipe.stdout.read().decode("utf-8").rstrip()


async def train(user_id):
    dict_users = None
    test_users = None
    skew_users1 = None
    skew_users2 = None
    skew_users3 = None
    skew_users4 = None
    dataset_train = None
    dataset_test = None
    net_glob = None

    if user_id is None:
        user_id = await fetch_user_id()
    # parse args
    args = args_parser()
    args.device = torch.device('cpu')
    epochs = args.epochs

    # parse participant number
    args.num_users = len(peer_address_list)

    # load dataset and split users
    real_path = os.path.dirname(os.path.realpath(__file__))
    if args.dataset == 'mnist':
        mnist_data_path = os.path.join(real_path, "../data/mnist/")
        trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
        dataset_train = datasets.MNIST(mnist_data_path, train=True, download=True, transform=trans_mnist)
        dataset_test = datasets.MNIST(mnist_data_path, train=False, download=True, transform=trans_mnist)
        # sample users
        if args.iid:
            dict_users = mnist_iid(dataset_train, args.num_users)
        else:
            dict_users, test_users, skew_users1, skew_users2, skew_users3, skew_users4 = \
                noniid_onepass(dataset_train, dataset_test, args.num_users)
    elif args.dataset == 'cifar':
        cifar_data_path = os.path.join(real_path, "../data/cifar/")
        trans_cifar = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        dataset_train = datasets.CIFAR10(cifar_data_path, train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10(cifar_data_path, train=False, download=True, transform=trans_cifar)
        if args.iid:
            dict_users = cifar_iid(dataset_train, args.num_users)
        else:
            dict_users, test_users, skew_users1, skew_users2, skew_users3, skew_users4 = noniid_onepass(
                dataset_train,
                dataset_test,
                args.num_users)
            # exit('Error: only consider IID setting in CIFAR10')
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

    # initialize weights of model
    net_glob.train()

    # training for all epochs
    for iter in reversed(range(epochs)):
        print("Epoch [" + str(iter+1) + "] train for user [" + str(user_id) + "]")
        train_start_time = time.time()
        local = LocalUpdate(args=args, dataset=dataset_train, idxs=dict_users[user_id - 1])
        w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
        train_time = time.time() - train_start_time

        # start test
        test_start_time = time.time()
        idx = int(user_id) - 1
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

        test_time = time.time() - test_start_time

        # before start next round, record the time
        filename = "result-record_" + str(user_id) + ".txt"
        # first time clean the file
        if iter + 1 == args.epochs:
            with open(filename, 'w') as f:
                pass

        with open(filename, "a") as time_record_file:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            time_record_file.write(current_time + "[" + f"{iter + 1:0>2}" + "]"
                                   + " <Train Time> " + str(train_time)[:8]
                                   + " <Test Time> " + str(test_time)[:8]
                                   + " <acc_local> " + str(acc_local.item())[:8]
                                   + " <acc_local_skew1> " + str(acc_local_skew1.item())[:8]
                                   + " <acc_local_skew2> " + str(acc_local_skew2.item())[:8]
                                   + " <acc_local_skew3> " + str(acc_local_skew3.item())[:8]
                                   + " <acc_local_skew4> " + str(acc_local_skew4.item())[:8]
                                   + "\n")

        # update net_glob for next round
        net_glob.load_state_dict(w)

    print("##########\nALL DONE!\n##########")
    return


class MultiTrainThread(Thread):
    def __init__(self, user_id):
        Thread.__init__(self)
        self.user_id = user_id

    def run(self):
        print("start new thread")
        loop = asyncio.new_event_loop()
        loop.run_until_complete(train(self.user_id))
        print("end thread")


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


async def http_client_post(url, json_body, message="None"):
    print("Start http client post [" + message + "] to: " + url)
    method = "POST"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_client = httpclient.AsyncHTTPClient()
    try:
        request = httpclient.HTTPRequest(url=url, method=method, headers=headers, body=json_body, connect_timeout=300,
                                         request_timeout=300)
        response = await http_client.fetch(request)
        print("[HTTP Success] [" + message + "] SERVICE RESPONSE: %s" % response.body)
        return response.body
    except Exception as e:
        print("[HTTP Error] [" + message + "] SERVICE RESPONSE: %s" % e)
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


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        print("Detected IP address: " + IP)
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
            thread_train = MultiTrainThread(None)
            threads.append(thread_train)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all of threads to finish
    # for thread in threads:
    #     thread.join()

    app = make_app()
    app.listen(fed_listen_port)
    print("start serving at " + str(fed_listen_port) + "...")
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
