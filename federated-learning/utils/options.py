#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import argparse

def args_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--epochs', type=int, default=50, help="rounds of training")
    parser.add_argument('--num_users', type=int, default=10, help="number of users: K")
    parser.add_argument('--frac', type=float, default=1.0, help="the fraction of clients: C")
    parser.add_argument('--local_ep', type=int, default=5, help="the number of local epochs: E")
    parser.add_argument('--local_bs', type=int, default=10, help="local batch size: B")
    parser.add_argument('--local_test_bs', type=int, default=128, help="test batch size")
    parser.add_argument('--lr', type=float, default=0.01, help="learning rate")
    parser.add_argument('--momentum', type=float, default=0.5, help="SGD momentum (default: 0.5)")

    # model arguments, support model: "cnn", "mlp"
    parser.add_argument('--model', type=str, default='cnn', help='model name')
    # support dataset: "mnist", "fmnist", "cifar", "uci", "realworld"
    parser.add_argument('--dataset', type=str, default='cifar', help="name of dataset")
    parser.add_argument('--gpu', type=int, default=-1, help="GPU ID, -1 for CPU")
    parser.add_argument('--log_level', type=str, default='DEBUG', help='DEBUG, INFO, WARNING, ERROR, or CRITICAL')

    # for APFL
    parser.add_argument('--apfl_hyper', type=float, default=0.3, help='APFL hypermeter alpha')

    # for SCEI
    parser.add_argument('--hyperpara', type=float, default=0.75, help="hyperpara alpha")
    parser.add_argument('--hyperpara_static', action='store_true', help='whether static hyperpara or not')
    parser.add_argument('--hyperpara_min', type=float, default=0.5, help="hyperpara alpha min")
    parser.add_argument('--hyperpara_max', type=float, default=0.8, help="hyperpara alpha max")
    parser.add_argument('--negotiate_round', type=int, default=10, help="hyperpara negotiate round")

    args = parser.parse_args()
    return args
