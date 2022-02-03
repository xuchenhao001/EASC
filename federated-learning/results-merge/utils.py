import os
import re

import numpy as np


def parse_lines_filtered(file_path):
    # read all lines in file to lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    file_gather_list = []
    for r in range(len(lines)):
        record = lines[r]
        round_number = int(record[9:12])
        if round_number > 0:  # filter all epochs that greater than zero
            record_trim = record[13:]
            numbers_str = re.findall(r"[-+]?\d*\.\d+|\d+ ", record_trim)
            numbers_float = [float(s) for s in numbers_str]
            file_gather_list.append(numbers_float)
    return file_gather_list


def extract_files_lines(experiment_path):
    result_files = [f for f in os.listdir(experiment_path) if f.startswith('result-record_')]

    files_numbers_3d = []
    for result_file in result_files:
        file_path = os.path.join(experiment_path, result_file)
        file_numbers_2d = parse_lines_filtered(file_path)  # parse each file into two dimensional array
        files_numbers_3d.append(file_numbers_2d)
    return files_numbers_3d


def calculate_average_across_files(experiment_path):
    files_numbers_3d = extract_files_lines(experiment_path)
    files_numbers_3d_np = np.array(files_numbers_3d)
    files_numbers_mean_2d_np = files_numbers_3d_np.mean(axis=0)
    return files_numbers_mean_2d_np


# if find out the one greater than time, return the index, else return -1
def find_greater_time_index(file_items_2d, time_to_compare):
    for i, v in enumerate(file_items_2d):
        if v[0] >= time_to_compare:
            return i
    return -1


def extract_by_timeline(files_items_3d, sampling_frequency, final_time):
    sampling_time = 0
    avg_list = []
    while True:
        sampling_time += sampling_frequency
        acc_list = []
        for file_items_2d in files_items_3d:
            greater_time_index = find_greater_time_index(file_items_2d, sampling_time)
            # locate the largest row smaller than sampling_time
            if greater_time_index != -1:
                latest_acc = file_items_2d[greater_time_index][5]
                acc_list.append(latest_acc)
        if sampling_time + sampling_frequency >= final_time:
            break
        if len(acc_list) == 0:
            avg_list.append(None)
        else:
            avg = sum(acc_list) / len(acc_list)
            avg_list.append(round(avg, 2))
    return avg_list


def latest_acc_by_timeline(experiment_path, sampling_frequency, final_time):
    files_numbers_3d = extract_files_lines(experiment_path)
    return extract_by_timeline(files_numbers_3d, sampling_frequency, final_time)
