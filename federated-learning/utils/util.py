#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import os

from torchvision import datasets, transforms

from datasets.REALWORLD import REALWORLDDataset
from datasets.UCI import UCIDataset
from models.Nets import CNNCifar, CNNMnist, UCI_CNN, MLP
from utils.sampling import mnist_iid, cifar_iid, noniid_onepass


def dataset_loader(dataset_name, isIID, num_users):
    dataset_train = None
    dataset_test = None
    dict_users = None
    test_users = None
    skew_users = None
    real_path = os.path.dirname(os.path.realpath(__file__))
    # load dataset and split users
    if dataset_name == 'mnist':
        trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
        mnist_data_path = os.path.join(real_path, "../../data/mnist/")
        dataset_train = datasets.MNIST(mnist_data_path, train=True, download=True, transform=trans_mnist)
        dataset_test = datasets.MNIST(mnist_data_path, train=False, download=True, transform=trans_mnist)
        # sample users
        if isIID:
            dict_users = mnist_iid(dataset_train, num_users)
        else:
            dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_test, num_users,
                                                                dataset_name='mnist')
    elif dataset_name == 'cifar':
        trans_cifar = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        cifar_data_path = os.path.join(real_path, "../../data/cifar/")
        dataset_train = datasets.CIFAR10(cifar_data_path, train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10(cifar_data_path, train=False, download=True, transform=trans_cifar)
        if isIID:
            dict_users = cifar_iid(dataset_train, num_users)
        else:
            dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_test, num_users,
                                                                dataset_name='cifar')
    elif dataset_name == 'uci':
        uci_data_path = os.path.join(real_path, "../../data/uci/")
        dataset_train = UCIDataset(data_path=uci_data_path, phase='train')
        dataset_test = UCIDataset(data_path=uci_data_path, phase='eval')
        if isIID:
            dict_users = cifar_iid(dataset_train, num_users)
        else:
            dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_test, num_users,
                                                                dataset_name='uci')
    elif dataset_name == 'realworld':
        realworld_data_path = os.path.join(real_path, "../../data/realworld_client/")
        dataset_train = REALWORLDDataset(data_path=realworld_data_path, phase='train')
        dataset_test = REALWORLDDataset(data_path=realworld_data_path, phase='eval')
        if isIID:
            dict_users = cifar_iid(dataset_train, num_users)
        else:
            dict_users, test_users, skew_users = noniid_onepass(dataset_train, dataset_test, num_users,
                                                                dataset_name='realworld')
    return dataset_train, dataset_test, dict_users, test_users, skew_users


def model_loader(model_name, dataset_name, device, num_channels, num_classes, img_size):
    net_glob = None
    # build model, init part
    if model_name == 'cnn' and dataset_name == 'cifar':
        net_glob = CNNCifar(num_classes).to(device)
    elif model_name == 'cnn' and dataset_name == 'mnist':
        net_glob = CNNMnist(num_channels, num_classes).to(device)
    elif model_name == 'cnn' and dataset_name == 'uci':
        net_glob = UCI_CNN(n_class=6).to(device)
    elif model_name == 'cnn' and dataset_name == 'realworld':
        net_glob = UCI_CNN(n_class=8).to(device)
    elif model_name == 'mlp':
        len_in = 1
        for x in img_size:
            len_in *= x
        net_glob = MLP(dim_in=len_in, dim_hidden=64, dim_out=num_classes).to(device)
    return net_glob
