#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import copy

import torch


def fed_avg(w_dict, w_glob, device):
    if len(w_dict) == 0:
        return w_glob
    w_avg = {}
    for k in w_glob.keys():
        for local_uuid in w_dict:
            if k not in w_avg:
                w_avg[k] = torch.zeros_like(w_glob[k], device=device)
            if device != torch.device('cpu'):
                w_dict[local_uuid][k] = w_dict[local_uuid][k].to(device)
            w_avg[k] = torch.add(w_avg[k], w_dict[local_uuid][k])
        w_avg[k] = torch.div(w_avg[k], len(w_dict))
    return w_avg


def async_fed_avg(w_local, w_glob, device):
    w_avg = copy.deepcopy(w_glob)
    for k in w_avg.keys():
        if device != torch.device('cpu'):
            w_local[k] = w_local[k].to(device)
        w_avg[k] = torch.add(w_avg[k], w_local[k])
        w_avg[k] = torch.div(w_avg[k], 2)
    return w_avg
