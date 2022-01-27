#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import argparse

def args_parser():
    parser = argparse.ArgumentParser()

    # classic FL settings
    parser.add_argument('--epochs', type=int, default=50, help="rounds of training")
    parser.add_argument('--num_users', type=int, default=2, help="number of users: K")
    parser.add_argument('--frac', type=float, default=1.0, help="the fraction of clients: C")
    parser.add_argument('--local_ep', type=int, default=5, help="the number of local epochs: E")
    parser.add_argument('--local_bs', type=int, default=10, help="local batch size: B")
    parser.add_argument('--local_test_bs', type=int, default=128, help="test batch size")
    parser.add_argument('--lr', type=float, default=0.01, help="learning rate")
    parser.add_argument('--momentum', type=float, default=0.5, help="SGD momentum (default: 0.5)")

    # Model and Datasets
    # model arguments, support model: "cnn", "mlp"
    parser.add_argument('--model', type=str, default='cnn', help='model name')
    # support dataset: "mnist", "fmnist", "cifar10", "cifar100", "imagenet", "uci", "realworld"
    parser.add_argument('--dataset', type=str, default='imagenet', help="name of dataset")
    # total dataset training size: MNIST: 60000, FASHION-MNIST:60000, CIFAR-10: 60000, CIFAR-100: 60000,
    # ImageNet: 100000, UCI: 10929, REALWORLD: 285148,
    parser.add_argument('--dataset_train_size', type=int, default=500, help="total dataset training size")

    # env settings
    parser.add_argument('--fl_listen_port', type=str, default='8888', help="federated learning listen port")
    parser.add_argument('--gpu', type=int, default=-1, help="GPU ID, -1 for CPU")
    parser.add_argument('--log_level', type=str, default='DEBUG', help='DEBUG, INFO, WARNING, ERROR, or CRITICAL')
    # ip address that is used to test local IP
    parser.add_argument('--test_ip_addr', type=str, default="10.150.187.13", help="ip address used to test local IP")
    # sleep for several seconds before start train
    parser.add_argument('--start_sleep', type=int, default=60, help="sleep for seconds before start train")
    # sleep for several seconds before exit python
    parser.add_argument('--exit_sleep', type=int, default=60, help="sleep for seconds before exit python")

    # for APFL
    parser.add_argument('--apfl_hyper', type=float, default=0.3, help='APFL hypermeter alpha')
    parser.add_argument('--apfl_agg_freq', type=int, default=10, help='APFL aggregation round frequency')

    # for SCEI
    parser.add_argument('--hyperpara', type=float, default=0.75, help="hyperpara alpha")
    parser.add_argument('--hyperpara_static', action='store_true', help='whether static hyperpara or not')
    parser.add_argument('--hyperpara_min', type=float, default=0.5, help="hyperpara alpha min")
    parser.add_argument('--hyperpara_max', type=float, default=0.8, help="hyperpara alpha max")
    parser.add_argument('--negotiate_round', type=int, default=10, help="hyperpara negotiate round")

    args = parser.parse_args()
    return args
