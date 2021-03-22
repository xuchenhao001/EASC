#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import asyncio
import base64
import gzip
import hashlib
import json
import matplotlib
import math
import os
import random
import time
import socket
import statistics
import subprocess

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

from tornado import httpclient, ioloop, web, gen

np.random.seed(0)

# TO BE CHANGED
attackers_id = []
# alpha minimum
hyperpara_min = 0.5
# alpha maximum
hyperpara_max = 0.8
# rounds to negotiate alpha
negotiate_round = 10
# committee members proportion
committee_proportion = 0.3
# TO BE CHANGED FINISHED

# NOT TO TOUCH VARIABLES BELOW
blockchain_server_url = ""
trigger_url = ""
# blockchain_server_url = "http://localhost:3000/invoke/mychannel/fabcar"
# trigger_url = "http://localhost:8888/trigger"
total_epochs = 0
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
poll_count_num = 0
negotiate_count_num = 0
next_round_count_num = 0
g_start_time = {}
g_train_time = {}
g_test_time = {}
ip_map = {}
peerAddressList = []


######## Federated Learning process ########
# 0. the client send a train request to BC-node1-python
# 1. (prepare for the training) BC-node1-python initiate local (global) model, and then send the hash of global model
#    to the ledger.
# 2. BC-nodes-python choose committee members according to global model hash, pull up hraftd distributed processes,
#    send setup request to raftd and start up raft consensus，finally send raft network info to the ledger.
# 3. BC-nodes-python train local model based on previous round's local model, send local model to the committee leader.
# 4. committee leader received local model, send hash of local model to the ledger.
# 5. committee leader received all local models, aggregate to global model, then send the download link of global model
#    and the hash of global model to the ledger.
# 6. BC-nodes-python get the download link of global model from the ledger, download the global model, then calculate
#    alpha-accuracy map, which will be uploaded to the committee leader.
# 7. committee leader received alpha-accuracy map, send to the ledger
# 8. after gathering all alpha-accuracy maps, pick up the appropriate alpha according to the rule, save to the ledger.
# 9. BC-nodes-python get the appropriate alpha, merge the local model and the global model with alpha to generate the
#    new local model. Test the new local model, then repeat from step 2.


def test(data):
    detail = {"data": data}
    return "yes", detail


# returns variable from sourcing a file
def env_from_sourcing(file_to_source_path, variable_name):
    source = 'source %s && export MYVAR=$(echo "${%s[@]}")' % (file_to_source_path, variable_name)
    # dump = '/usr/bin/python3 -c "import os, json; print(json.dumps(dict(os.getenv(\'MYVAR\'))))"'
    dump = '/usr/bin/python3 -c "import os, json; print(os.getenv(\'MYVAR\'))"'
    pipe = subprocess.Popen(['/bin/bash', '-c', '%s && %s' % (source, dump)], stdout=subprocess.PIPE)
    # return json.loads(pipe.stdout.read())
    return pipe.stdout.read().decode("utf-8").rstrip()


async def http_client_post(url, body_data):
    json_body = json.dumps(body_data, sort_keys=True, indent=4, ensure_ascii=False, cls=NumpyEncoder).encode('utf8')
    print("Start http client post [" + body_data['message'] + "] to: " + url)
    method = "POST"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_client = httpclient.AsyncHTTPClient()
    try:
        request = httpclient.HTTPRequest(url=url, method=method, headers=headers, body=json_body, connect_timeout=300,
                                         request_timeout=300)
        response = await http_client.fetch(request)
        print("[HTTP Success] [" + body_data['message'] + "] from " + url + " SERVICE RESPONSE: %s" % response.body)
        return response.body
    except Exception as e:
        print("[HTTP Error] [" + body_data['message'] + "] from " + url + " SERVICE RESPONSE: %s" % e)
        return None


# STEP #1
# Federated Learning: init step
def init():
    global args
    global total_epochs
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
    global blockchain_server_url
    global trigger_url
    global peerAddressList
    # parse network.config and read the peer addresses
    real_path = os.path.dirname(os.path.realpath(__file__))
    peerAddressVar = env_from_sourcing(os.path.join(real_path, "../fabric-samples/network.config"), "PeerAddress")
    peerAddressList = peerAddressVar.split(' ')
    peerHeaderAddr = peerAddressList[0].split(":")[0]
    blockchain_server_url = "http://" + peerHeaderAddr + ":3000/invoke/mychannel/fabcar"
    trigger_url = "http://" + peerHeaderAddr + ":8888/trigger"

    # parse args
    args = args_parser()
    args.device = torch.device('cuda:{}'.format(args.gpu) if torch.cuda.is_available() and args.gpu != -1 else 'cpu')
    total_epochs = args.epochs
    # parse participant number
    args.num_users = len(peerAddressList)

    # load dataset and split users
    if args.dataset == 'mnist':
        trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
        mnist_data_path = os.path.join(real_path, "../data/mnist/")
        dataset_train = datasets.MNIST(mnist_data_path, train=True, download=True, transform=trans_mnist)
        dataset_test = datasets.MNIST(mnist_data_path, train=False, download=True, transform=trans_mnist)
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
        cifar_data_path = os.path.join(real_path, "../data/cifar/")
        dataset_train = datasets.CIFAR10(cifar_data_path, train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10(cifar_data_path, train=False, download=True, transform=trans_cifar)
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
    # finally trained the initial local model, which will be treated as first global model.
    net_glob.train()


# STEP #1
async def start():
    print("####################\nEpoch #", total_epochs, " start now\n####################")
    # generate md5 hash from model, which is treated as global model of previous round.
    model_md5 = generate_md5_hash(net_glob)
    # upload md5 hash to ledger
    body_data = {
        'message': 'Start',
        'data': {
            'global_hash': model_md5,
            'user_number': args.num_users,
        },
        'epochs': total_epochs
    }
    await http_client_post(blockchain_server_url, body_data)


# STEP #2
async def prepare(data, uuid, epochs):
    print('Received boot strap request for user: ' + uuid)
    md5hash = data.get("global_hash")
    committee_leader_id = int(md5hash, 16) % args.num_users + 1
    committee_proportion_num = math.ceil(args.num_users * committee_proportion)  # committee id delta value
    committee_highest_id = committee_proportion_num + committee_leader_id - 1
    # pull up hraftd distributed processes, if the value of uuid is in range of committee leader id and highest id.
    if int(uuid) <= committee_highest_id or int(uuid) <= committee_highest_id % args.num_users:
        print("# BOOT LOCAL RAFT PROCESS! #")
        myIP = peerAddressList[int(uuid) - 1].split(":")[0]
        myPort = peerAddressList[int(uuid) - 1].split(":")[1]
        httpPort = int(myPort) + 100
        raftPort = int(myPort) + 101
        boot_local_raft_proc(uuid, myIP, httpPort, raftPort)
    # wait for a while in case raft processes on some nodes are not running.
    await gen.sleep(5)
    if int(uuid) == committee_leader_id:
        print("Find out the leader ID: " + uuid)
        print("# BOOT RAFT CONSENSUS NETWORK! #")

        leaderIP = peerAddressList[int(uuid) - 1].split(":")[0]
        leaderPort = peerAddressList[int(uuid) - 1].split(":")[1]
        httpPort = int(leaderPort) + 100
        raftPort = int(leaderPort) + 101
        leaderAddr = leaderIP + ":" + str(httpPort)
        leaderRaftAddr = leaderIP + ":" + str(raftPort)

        clientAddrs = []
        clientRaftAddrs = []
        clientIds = []
        for id in range(int(uuid), committee_highest_id):
            if id > args.num_users:
                index = id % args.num_users
                clientIds.append(str(id))
        body_data = {
            'leaderAddr': leaderAddr,
            'leaderRaftAddr': leaderRaftAddr,
            'leaderId': str(uuid),
            'clientAddrs': 'Start',
            'clientRaftAddrs': 'Start',
            'clientIds': 'Start',
        }


# boot local raft process, preparing for the raft consensus algorithm
def boot_local_raft_proc(uuid, ip, http_port, raft_port):
    node_id = "node" + str(uuid)
    haddr = ip + ":" + str(http_port)
    raddr = ip + ":" + str(raft_port)
    real_path = os.path.dirname(os.path.realpath(__file__))
    hraftd_path = os.path.join(real_path, "../raft/hraftd")
    snapshot_path = os.path.join(real_path, "../raft/" + node_id)
    subprocess.Popen([hraftd_path, "-id", node_id, "-haddr", haddr, "-raddr", raddr, snapshot_path])
    return


# generate raft address from peer address
def generate_raft_addr(peer_addr):
    print('generate peer addr for: ' + peer_addr)
    ip = peer_addr.split(":")[0]
    port = peer_addr.split(":")[1]
    http_port = str(int(port) + 100)  # raft http port is (100 + peer port)
    raft_port = str(int(port) + 101)  # raft port is (101 + peer port)
    return {'httpAddr': ip + ':' + http_port, 'raftAddr': ip + ':' + raft_port}


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
    # fake attackers
    if uuid in attackers_id:
        w = disturb_w(w)
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
    await http_client_post(blockchain_server_url, body_data)
    trigger_data = {
        'message': 'train_ready',
        'epochs': epochs,
        'uuid': uuid,
        'start_time': start_time,
        'train_time': train_time,
    }
    await http_client_post(trigger_url, trigger_data)


def disturb_w(w):
    disturbed_w = copy.deepcopy(w)
    for name, param in w.items():
        beta = random.random()
        transformed_w = param * beta
        disturbed_w[name] = transformed_w
    return disturbed_w


# STEP #4.1
# Security poll
async def security_poll(w_compressed_map, uuid, epochs):
    print('received security poll request.')
    w_map = {}
    # calculate loss mean and std
    for w_uuid in w_compressed_map.keys():
        w = w_compressed_map[w_uuid].get("w")
        decompressed_w = decompress_data(w)
        conver_json_value_to_tensor(decompressed_w)
        w_map[w_uuid] = decompressed_w
    # test the loss of weight on myself dataset
    idx = int(uuid) - 1
    loss_map = {}
    cross_test_start_time = time.time()
    for w_uuid in w_map.keys():
        net_glob.load_state_dict(w_map[w_uuid])
        net_glob.eval()
        acc_test, loss_test = test_img(net_glob, dataset_test, test_users[idx], args)
        loss_map[w_uuid] = loss_test
        print("Cross test for user " + str(w_uuid) + " result: " + str(loss_test))
    cross_test_time = time.time() - cross_test_start_time
    loss_mean = statistics.mean(list(loss_map.values()))
    loss_std = statistics.stdev(list(loss_map.values()))
    outlier_line = 2 * loss_std + loss_mean
    print("Outlier line for epoch [" + str(epochs) + "] is: " + str(outlier_line))
    # just for local test
    # outlier_line = 0.6
    # find out outlier loss value
    outlier_uuid = []
    for w_uuid in loss_map.keys():
        if loss_map[w_uuid] > outlier_line:
            print("!!! Found attacker: " + w_uuid + " with loss: " + str(loss_map[w_uuid]))
            outlier_uuid.append(int(w_uuid))
    body_data = {
        'message': 'outlier_record',
        'data': {
            'outlier_ids': outlier_uuid,
        },
        'uuid': uuid,
        'epochs': epochs,
    }
    await http_client_post(blockchain_server_url, body_data)
    trigger_data = {
        'message': 'outlier_record_ready',
        'epochs': epochs,
        'uuid': uuid,
    }
    response = await http_client_post(trigger_url, trigger_data)
    # first decode from blockchain server, then decode from smart contract
    responseObj = json.loads(response)
    sc_responseObj = json.loads(responseObj.get("detail"))
    outlier_list = sc_responseObj.get("detail")
    print("Get outlier_list: " + ', '.join(str(e) for e in outlier_list))

    # STEP 4.2 average w, generate new global_w
    wArray = []
    for w_uuid in w_map.keys():
        # filter outliers
        if int(w_uuid) not in outlier_list:
            wArray.append(w_map[w_uuid])
    w_glob = FedAvg(wArray)
    w_local = w_map[uuid]

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
    await http_client_post(blockchain_server_url, body_data)
    # start new thread for step #5
    thread_negotiate = myNegotiateThread(uuid, w_glob, w_local, epochs, cross_test_time)
    thread_negotiate.start()


# STEP #5
# Federated Learning: negotiate and test accuracy, upload to blockchain
class myNegotiateThread(Thread):
    def __init__(self, my_uuid, w_glob, w_local, epochs, cross_test_time):
        Thread.__init__(self)
        self.my_uuid = my_uuid
        self.w_glob = w_glob
        self.w_local = w_local
        self.epochs = epochs
        self.cross_test_time = cross_test_time

    def run(self):
        print("start my negotiate thread: " + self.my_uuid)
        loop = asyncio.new_event_loop()
        loop.run_until_complete(negotiate(self.my_uuid, self.w_glob, self.w_local, self.epochs, self.cross_test_time))
        print("end my negotiate thread: " + self.my_uuid)


async def negotiate(my_uuid, w_glob, w_local, epochs, cross_test_time):
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
    await http_client_post(blockchain_server_url, body_data)
    trigger_data = {
        'message': 'negotiate_ready',
        'epochs': epochs,
        'uuid': my_uuid,
        'test_time': test_time + cross_test_time,
    }
    await http_client_post(trigger_url, trigger_data)


# STEP #7
# Federated Learning: with new alpha, train w_local2, restart the round
async def round_finish(data, uuid, epochs):
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
    response = await http_client_post(trigger_url, fetch_data)
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
        from_ip = get_ip()
        body_data = {
            'message': 'next_round_count',
            'data': data,
            'uuid': uuid,
            'epochs': epochs,
            'from_ip': from_ip,
        }
        await http_client_post(trigger_url, body_data)
    else:
        print("##########\nALL DONE!\n##########")


async def next_round_start(data, uuid, new_epochs):
    print("####################\nEpoch #", new_epochs, " start now\n####################")
    # reset a new time for next round
    await train(data, uuid, new_epochs, time.time())


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


# generate md5 hash for global model
def generate_md5_hash(model):
    w_model = model.state_dict()
    convert_tensor_value_to_numpy(w_model)
    data_md5 = hashlib.md5(json.dumps(w_model, sort_keys=True, cls=NumpyEncoder).encode('utf-8')).hexdigest()
    return data_md5


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
        elif message == "start":
            asyncio.ensure_future(start())
        elif message == "prepare":
            asyncio.ensure_future(prepare(data.get("data"), data.get("uuid"), data.get("epochs")))
        elif message == "prepare":
            asyncio.ensure_future(train(data.get("data"), data.get("uuid"), data.get("epochs"), time.time()))
        elif message == "security_poll":
            asyncio.ensure_future(security_poll(data.get("data"), data.get("uuid"), data.get("epochs")))
        elif message == "alpha":
            asyncio.ensure_future(round_finish(data.get("data"), data.get("uuid"), data.get("epochs")))
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
    lock.release()
    if train_count_num == args.num_users:
        print("Gathered enough train_ready, send to blockchain server. now: " + str(train_count_num))
        # check train read first, since network delay may cause blockchain dirty read.
        while True:
            trigger_data = {
                'message': 'check_train_read',
                'epochs': epochs,
            }
            response = await http_client_post(blockchain_server_url, trigger_data)
            if response is not None:
                break
            await gen.sleep(1)  # if dirty read happened, sleep for 1 second then retry.

        # trigger train_ready
        trigger_data = {
            'message': 'train_ready',
            'epochs': epochs,
        }
        await http_client_post(blockchain_server_url, trigger_data)


# This is a blocking process until blockchain returns poll results
async def poll_count(epochs, uuid):
    lock.acquire()
    global poll_count_num
    poll_count_num += 1
    print("Received a outlier_record_ready from " + str(uuid) + ", now: " + str(poll_count_num))
    lock.release()
    while True:
        if poll_count_num == args.num_users:
            print("Gathered enough outlier_record_ready, send to blockchain server. now: " + str(poll_count_num))
            # check train read first, since network delay may cause blockchain dirty read.
            while True:
                trigger_data = {
                    'message': 'check_poll_read',
                    'epochs': epochs,
                }
                response = await http_client_post(blockchain_server_url, trigger_data)
                if response is not None:
                    break
                await gen.sleep(1)  # if dirty read happened, sleep for 1 second then retry.

            # get poll results, and go back continue to average w
            trigger_data = {
                'message': 'poll_ready',
                'epochs': epochs,
            }
            result = await http_client_post(blockchain_server_url, trigger_data)
            return result.decode("utf-8")
        else:
            # if not enough poll gathered, sleep for 1 second then retry.
            await gen.sleep(1)


async def negotiate_count(epochs, uuid, test_time):
    lock.acquire()
    global negotiate_count_num
    global g_test_time
    negotiate_count_num += 1
    key = str(uuid) + "-" + str(epochs)
    g_test_time[key] = test_time
    lock.release()
    if negotiate_count_num == args.num_users:
        # check negotiate read first, since network delay may cause blockchain dirty read.
        while True:
            trigger_data = {
                'message': 'check_negotiate_read',
                'epochs': epochs,
            }
            response = await http_client_post(blockchain_server_url, trigger_data)
            if response is not None:
                break
            await gen.sleep(1)  # if dirty read happened, sleep for 1 second then retry.

        trigger_data = {
            'message': 'negotiate_ready',
            'epochs': epochs,
        }
        await http_client_post(blockchain_server_url, trigger_data)


async def next_round_count(data, epochs, uuid, from_ip):
    global train_count_num
    global poll_count_num
    global negotiate_count_num
    global next_round_count_num
    lock.acquire()
    next_round_count_num += 1
    ip_map[uuid] = from_ip
    lock.release()
    if next_round_count_num == args.num_users:
        # reset counts
        lock.acquire()
        train_count_num = 0
        poll_count_num = 0
        negotiate_count_num = 0
        next_round_count_num = 0
        lock.release()
        # sleep 20 seconds before trigger next round
        print("SLEEP FOR A WHILE...")
        await gen.sleep(20)
        # trigger each node of python to next round
        for user_id in ip_map.keys():
            trigger_data = {
                'message': 'next_round_start',
                'uuid': user_id,
                'epochs': epochs - 1,
                'data': data,
            }
            my_url = "http://" + ip_map[user_id] + ":8888/trigger"
            asyncio.ensure_future(http_client_post(my_url, trigger_data))


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
        if message == "outlier_record_ready":
            detail = await poll_count(data.get("epochs"), data.get("uuid"))
        elif message == "negotiate_ready":
            await negotiate_count(data.get("epochs"), data.get("uuid"), data.get("test_time"))
        elif message == "next_round_count":
            await next_round_count(data.get("data"), data.get("epochs"), data.get("uuid"), data.get("from_ip"))
        elif message == "next_round_start":
            await next_round_start(data.get("data"), data.get("uuid"), data.get("epochs"))
        elif message == "fetch_time":
            detail = await fetch_time(data.get("uuid"), data.get("epochs"))

        response = {"status": status, "detail": detail}
        in_json = json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
        self.write(in_json)


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
