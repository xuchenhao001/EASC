import sys

from plot.utils.skew import plot_skew

fed_server = [83.6, 83.55, 84.09, 84.26, 85.12, 85.04, 84.42, 85.04, 85.08, 85.74, 85.45, 85.5, 85.7, 86.12, 86.94, 87.56, 86.32, 87.31, 87.11, 87.27, 86.4, 87.52, 87.93, 87.36, 88.18, 87.23, 88.14, 88.39, 87.85, 88.26]
main_nn = [77.85, 77.93, 77.85, 78.06, 77.93, 78.1, 78.06, 77.81, 78.14, 78.1, 78.22, 77.98, 77.85, 78.06, 78.06, 78.02, 78.06, 78.02, 77.98, 77.98, 77.98, 78.06, 77.81, 78.06, 77.85, 77.69, 77.85, 77.98, 78.02, 78.06]
main_fed_localA = [78.47, 78.31, 78.47, 78.31, 78.35, 78.39, 78.31, 78.35, 78.31, 78.18, 78.39, 78.35, 78.39, 78.39, 78.22, 78.39, 78.43, 78.35, 78.35, 78.35, 78.35, 78.43, 78.39, 78.31, 78.47, 78.51, 78.35, 78.35, 78.55, 78.31]
main_fed = [88.6, 88.6, 88.64, 88.72, 88.8, 88.93, 89.17, 89.3, 89.26, 89.13, 89.3, 89.55, 89.67, 89.55, 89.63, 89.88, 89.92, 89.63, 89.79, 90.08, 90.12, 90.0, 90.21, 90.21, 90.04, 90.21, 90.17, 90.25, 90.33, 90.29]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("Skew 15%", data, save_path)
