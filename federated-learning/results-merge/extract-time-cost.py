import os

from utils import calculate_average_across_files


def extract_communication_cost(exp_node_number, model_name, dataset_name):
    experiment_names = ["apfl", "fedavg", "scei", "scei-async"]
    for path, dirs, files in os.walk("./output"):
        if path.endswith(model_name + "-" + dataset_name) and exp_node_number in path:
            for experiment_name in experiment_names:
                experiment_path = os.path.join(path, experiment_name)
                files_numbers_mean_2d_np = calculate_average_across_files(experiment_path)
                cost_communication = [round(i, 2) for i in files_numbers_mean_2d_np[:, 4]]
                print(experiment_name, "=", cost_communication)


def extract_overall_cost(exp_node_number, model_name, dataset_name):
    experiment_names = ["apfl", "fedavg", "local", "scei", "scei-async"]
    for path, dirs, files in os.walk("./output"):
        if path.endswith(model_name + "-" + dataset_name) and exp_node_number in path:
            for experiment_name in experiment_names:
                experiment_path = os.path.join(path, experiment_name)
                files_numbers_mean_2d_np = calculate_average_across_files(experiment_path)
                cost_communication = [round(i, 2) for i in files_numbers_mean_2d_np[:, 1]]
                print(experiment_name, "=", cost_communication)


def main():
    exp_node_number = "all-test-v1"
    model_name = "cnn"
    dataset_name = "cifar10"

    # extract_communication_cost(exp_node_number, model_name, dataset_name)
    extract_overall_cost(exp_node_number, model_name, dataset_name)


if __name__ == "__main__":
    main()
