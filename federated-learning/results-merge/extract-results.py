#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import os

import pandas as pd


# extract the column from results as you want
def extract_column(path, column_num):
    df = pd.read_csv(path)
    choose_column = df.iloc[:, column_num]
    return choose_column.to_list()


# extract the final value from specific results column
def extract_final_value(path, column_num):
    df = pd.read_csv(path)
    choose_value = df.iloc[:, column_num].iloc[-1]
    return choose_value


# extract the final value from specific results column
def extract_late_rounds_value(path, from_round_num, column_num):
    df = pd.read_csv(path)
    choose_value = df.iloc[:, column_num].iloc[from_round_num:]
    return list(choose_value)


def extract_series_data():
    exp_node_number = "10-nodes"
    model_name = "cnn"
    dataset_name = "cifar"
    # experiment accuracy: column No.5
    # communication time: column No.3
    # total time: column No.0
    column_num = 5

    # experiment_names = ["fed_server", "main_fed_localA", "main_fed", "main_nn"]
    # experiment_names = ["fed_server", "fed_server_alpha_025", "fed_server_alpha_050", "fed_server_alpha_075", "main_fed", "main_nn"]
    # experiment_names = ["fed_server", "main_fed_localA", "main_fed"]
    experiment_names = ["fed_server"]
    # experiment_names = ["main_fed"]

    for path, dirs, files in os.walk("./output"):
        if path.endswith(model_name + "-" + dataset_name) and exp_node_number in path:
            for experiment_name in experiment_names:
                result_file = os.path.join(path, experiment_name, "merged.csv")
                result_list = extract_column(result_file, column_num)
                print(experiment_name, "=", result_list)


def extract_skew_data():
    exp_node_number = "10-nodes"
    model_name = "cnn"
    dataset_name = "realworld"

    experiment_names = ["fed_server", "main_nn", "main_fed_localA", "main_fed"]
    column_num = 5  # for acc_local columns
    skew_data_from_round = 20

    experiment_results = []
    for path, dirs, files in os.walk("./output"):
        if path.endswith(model_name + "-" + dataset_name) and exp_node_number in path:
            for i in range(len(experiment_names)):
                result_file = os.path.join(path, experiment_names[i], "merged.csv")
                # result_no_skew = extract_late_rounds_value(result_file, 20, column_num)
                result_skew_05 = extract_late_rounds_value(result_file, skew_data_from_round, column_num + 1)
                result_skew_10 = extract_late_rounds_value(result_file, skew_data_from_round, column_num + 2)
                result_skew_15 = extract_late_rounds_value(result_file, skew_data_from_round, column_num + 3)
                result_skew_20 = extract_late_rounds_value(result_file, skew_data_from_round, column_num + 4)
                experiment_results.append([result_skew_05, result_skew_10,
                                           result_skew_15, result_skew_20])

    print(model_name, "-", dataset_name)
    print("skew 05:")
    for i in range(len(experiment_names)):
        print(experiment_names[i], "=", experiment_results[i][0])
    print()
    print("skew 10:")
    for i in range(len(experiment_names)):
        print(experiment_names[i], "=", experiment_results[i][1])
    print()
    print("skew 15:")
    for i in range(len(experiment_names)):
        print(experiment_names[i], "=", experiment_results[i][2])
    print()
    print("skew 20:")
    for i in range(len(experiment_names)):
        print(experiment_names[i], "=", experiment_results[i][3])
    print()


def main():
    # extract_series_data()
    extract_skew_data()


if __name__ == "__main__":
    main()
