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


def main():
    model_name = "cnn"
    dataset_name = "realworld"
    # experiment accuracy: column No.5
    # communication time: column No.3
    # total communication time: column No.0
    column_num = 0

    # experiment_names = ["fed_server", "main_fed_localA", "main_fed", "main_nn"]
    # experiment_names = ["fed_server", "fed_server_alpha_025", "fed_server_alpha_050", "fed_server_alpha_075", "main_fed", "main_nn"]
    # experiment_names = ["fed_server", "main_fed_localA", "main_fed"]
    experiment_names = ["fed_server", "main_fed_localA", "main_fed", "main_nn"]

    for path, dirs, files in os.walk("./output"):
        if path.endswith(model_name + "-" + dataset_name):
            for experiment_name in experiment_names:
                result_file = os.path.join(path, experiment_name, "merged.csv")
                result_list = extract_column(result_file, column_num)
                print(experiment_name, "=", result_list)


if __name__ == "__main__":
    main()
