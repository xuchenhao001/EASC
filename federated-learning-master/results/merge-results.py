#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import re
import numpy as np

user_number = 10

merged_file_name = "output/result-record_merged.txt"
# read all of the files into lines[]
lines = []
for user_id in range(user_number):
    filename = "output/" + "result-record_" + str(user_id+1) + ".txt"
    with open(filename, 'r') as file:
        lines.append(file.readlines())

# start to process lines[]
round_num = len(lines[0])

with open(merged_file_name, 'w') as f:
    pass
for r in range(round_num):
    round_gather_list = []
    for user_id in range(user_number):
        record = lines[user_id][r]
        record_trim = record[13:]
        numbers_str = re.findall(r"[-+]?\d*\.\d+|\d+", record_trim)
        numbers = [float(s) for s in numbers_str]
        round_gather_list.append(numbers)
    data = np.array(round_gather_list)
    avg = np.average(data, axis=0).tolist()
    avg_pretty = ["{0:0.2f}".format(i) for i in avg]
    avg_str = "\t".join(avg_pretty)
    with open(merged_file_name, 'a') as file:
        file.write(avg_str + "\n")
