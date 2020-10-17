#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import copy
import numpy as np
from torchvision import datasets, transforms
import torch

from utils.sampling import mnist_iid, mnist_noniid, cifar_iid, noniid_onepass
from utils.options import args_parser
from models.Update import LocalUpdate
from models.Nets import MLP, CNNMnist, CNNCifar
from models.Fed import FedAvg
from models.test import test_img

torch.manual_seed(0)
np.random.seed(0)

if __name__ == '__main__':
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
            dict_users = mnist_iid(dataset_train, args.num_users)
        else:
            dict_users, test_users, skew_users1,skew_users2,skew_users3,skew_users4 = noniid_onepass(dataset_train, dataset_test, args.num_users)
    elif args.dataset == 'cifar':
        trans_cifar = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        dataset_train = datasets.CIFAR10('../data/cifar', train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10('../data/cifar', train=False, download=True, transform=trans_cifar)
        if args.iid:
            dict_users = cifar_iid(dataset_train, args.num_users)
        else:
            dict_users, test_users, skew_users1,skew_users2,skew_users3,skew_users4 = noniid_onepass(dataset_train, dataset_test, args.num_users)
            # exit('Error: only consider IID setting in CIFAR10')
    else:
        exit('Error: unrecognized dataset')
    img_size = dataset_train[0][0].shape

    # build model
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

    # copy weights
    w_glob = net_glob.state_dict()

    # training
    loss_train = []
    cv_loss, cv_acc = [], []
    val_loss_pre, counter = 0, 0
    net_best = None
    best_loss = None
    val_acc_list, net_list = [], []

    hyperpara=args.hyper
    

    w_locals2 = []


    m = max(int(args.frac * args.num_users), 1)
    idxs_users = np.random.choice(range(args.num_users), m, replace=False)

    for k in range(m):
        w_locals2.append(copy.deepcopy(w_glob))

    for iter in range(args.epochs):
        w_locals, loss_locals = [], []
        
        acc_locals = []
        acc_locals_skew = []
    
        # training
        k=0
        for idx in idxs_users:
            net_glob.load_state_dict(w_locals2[k])
            local = LocalUpdate(args=args, dataset=dataset_train, idxs=dict_users[idx])
            w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
            w_locals.append(copy.deepcopy(w))
            loss_locals.append(copy.deepcopy(loss))
            k=k+1
        
        # aggregating
        w_glob = FedAvg(w_locals)
        
        for k, idx in enumerate(idxs_users):
            for j in w_glob.keys():
                w_locals2[k][j] = hyperpara * w_locals[k][j] + (1-hyperpara)* w_glob[j]
      
        # testing
        acc_locals = []
        acc_locals_skew1 = []
        acc_locals_skew2 = []
        acc_locals_skew3 = []
        acc_locals_skew4 = []

        for k, idx in enumerate(idxs_users):
            net_glob.load_state_dict(w_locals2[k])
            net_glob.eval()
            correct_test, loss_test = test_img(net_glob, dataset_test, test_users[idx], args)
            acc_locals.append(torch.div(100.0 * correct_test, len(test_users[idx])))
            
            # skew 5%
            correct_skew1, loss_skew1 = test_img(net_glob, dataset_test, skew_users1[idx], args)
            acc_locals_skew1.append(torch.div(100.0 * (correct_skew1 + correct_test)
                , (len(test_users[idx]) + len(skew_users1[idx]))))
            # skew 10%
            correct_skew2, loss_skew2 = test_img(net_glob, dataset_test, skew_users2[idx], args)
            acc_locals_skew2.append(torch.div(100.0 * (correct_skew2 + correct_test)
                , (len(test_users[idx]) + len(skew_users2[idx]))))
            # skew 15%
            correct_skew3, loss_skew3 = test_img(net_glob, dataset_test, skew_users3[idx], args)
            acc_locals_skew3.append(torch.div(100.0 * (correct_skew3 + correct_test)
                , (len(test_users[idx]) + len(skew_users3[idx]))))
            # skew 20%
            correct_skew4, loss_skew4 = test_img(net_glob, dataset_test, skew_users4[idx], args)
            acc_locals_skew4.append(torch.div(100.0 * (correct_skew1 + correct_test)
                , (len(test_users[idx]) + len(skew_users4[idx]))))


        accfile = open('./log/accfile_{}users_{}_{}_{}_iid{}_fixed{}.dat'.format(args.num_users,args.dataset, args.model, args.epochs, args.iid, args.hyper), "a")
        accfile.write('Round ' + str(iter) + '\n')
        for i in range(len(acc_locals)):
            sac = str(acc_locals[i].item())
            acc_skew1 = str(acc_locals_skew1[i].item())
            acc_skew2 = str(acc_locals_skew2[i].item())
            acc_skew3 = str(acc_locals_skew3[i].item())
            acc_skew4 = str(acc_locals_skew4[i].item())
            accfile.write('User ' + str(i) + ' update model test  acc: ' + sac + '\n')
            accfile.write('User ' + str(i) + ' update model skew1 acc: ' + acc_skew1 + '\n')
            accfile.write('User ' + str(i) + ' update model skew2 acc: ' + acc_skew2 + '\n')
            accfile.write('User ' + str(i) + ' update model skew3 acc: ' + acc_skew3 + '\n')
            accfile.write('User ' + str(i) + ' update model skew4 acc: ' + acc_skew4 + '\n')
        accfile.close()

        lossfile = open('./log/lossfile_{}users_{}_{}_{}_iid{}fixed{}.dat'.format(args.num_users,args.dataset, args.model, args.epochs, args.iid, args.hyper), "a")
        for i, lo in enumerate(loss_locals):
            slo = str(lo)
            lossfile.write('User ' + str(i) + ': ' + slo + '\n')
        lossfile.close()

        # print loss
        loss_avg = sum(loss_locals) / len(loss_locals)
        print('Round {:3d}, Average loss {:.3f}'.format(iter, loss_avg))
        #loss_train.append(loss_avg)

    # save data to file loss.dat

    # lossfile = open('./log/lostfile_{}_{}_{}_iid{}.dat'.format(args.dataset, args.model, args.epochs, args.iid), "w")

    # for lo in loss_train:
    #     slo = str(lo)
    #     lossfile.write(slo)
    #     lossfile.write('\n')
    # lossfile.close()

    # plot loss curve
    # plt.figure()
    # plt.plot(range(len(loss_train)), loss_train)
    # plt.ylabel('train_loss')
    # plt.savefig('./log/fed_{}_{}_{}_C{}_iid{}_avg600.png'.format(args.dataset, args.model, args.epochs, args.frac, args.iid))

    # # testing
    # net_glob.eval()
    # acc_train, loss_train = test_img(net_glob, dataset_train, args)
    # acc_test, loss_test = test_img(net_glob, dataset_test, args)
    # print("Training accuracy: {:.2f}".format(acc_train))
    # print("Testing accuracy: {:.2f}".format(acc_test))

