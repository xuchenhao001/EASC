#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import datetime
import math
import os
import time

from numpy import random as nprandom


# block size is defined as the size of the new block in KB
def generate_block(block_size):
    with open("new_block", "wb") as out:
        out.truncate(block_size * 1024)


# simulate new block propagation in network, return propagation time
# block_size: 5KB, network_speed: 200KB/s, participants: 200,
# network_avg_delay: 200ms, network_delay_std: 100, propagation_rate: 2
# return: sum_time (ms)
def propagation_time_in_network(block_size, network_speed, participants, network_avg_delay, network_delay_std,
                                propagation_rate):
    propagation_round = round(math.log(participants, propagation_rate))
    propagation_round_time = abs(nprandom.normal(loc=network_avg_delay, scale=network_delay_std,
                                                 size=(propagation_round,)))
    transmit_block_time = float(block_size) / network_speed
    sum_time = 0
    for index in range(propagation_round):
        sum_time += transmit_block_time + propagation_round_time[index]
    return sum_time


def consensus_time(participants, block_size, network_speed, network_avg_delay, network_delay_std, propagation_rate):

    consensus_sum_time = datetime.timedelta(0)
    start_time = datetime.datetime.now()
    generate_block(block_size)
    end_time = datetime.datetime.now()
    propagation_time_ms = propagation_time_in_network(block_size, network_speed, participants, network_avg_delay,
                                                      network_delay_std, propagation_rate)
    consensus_sum_time += end_time - start_time + datetime.timedelta(milliseconds=propagation_time_ms)
    sum_time_ms = consensus_sum_time.seconds * 1000 + consensus_sum_time.microseconds / 1000
    if os.path.exists("new_block"):
        os.remove("new_block")
    return sum_time_ms


def post_to_blockchain(node_num):
    # block size in KB
    block_size = 5
    # network speed in KB/s
    network_speed = 2048
    # network delay in ms
    network_avg_delay = 50
    network_delay_std = 1
    propagation_rate = 2
    time_ms = consensus_time(node_num, block_size, network_speed, network_avg_delay, network_delay_std,
                             propagation_rate)
    time.sleep(time_ms/1000)

