import sys

from plot.utils.skew import plot_skew

fed_server = [91.71, 91.73, 91.6, 91.88, 92.23, 92.1, 92.12, 91.87, 92.08, 92.36, 92.69, 92.91, 92.41, 93.02, 92.98, 92.6, 92.91, 93.03, 93.17, 93.14, 93.64, 93.22, 93.17, 93.47, 93.27, 93.47, 93.55, 93.09, 93.45, 93.48]
main_nn = [86.59, 86.87, 86.92, 87.02, 87.08, 86.62, 86.6, 86.79, 86.77, 87.0, 86.97, 86.88, 86.55, 86.85, 86.72, 86.86, 86.91, 87.01, 86.59, 86.77, 86.77, 86.86, 86.99, 86.85, 86.87, 86.87, 86.79, 86.86, 86.76, 87.05]
main_fed_localA = [88.14, 88.15, 88.24, 88.08, 87.98, 88.17, 87.77, 88.14, 87.99, 88.13, 88.08, 87.97, 87.66, 88.16, 88.08, 88.2, 88.28, 87.93, 88.03, 88.21, 87.92, 88.13, 88.2, 88.05, 88.3, 88.0, 88.19, 87.97, 88.16, 87.97]
main_fed = [92.29, 91.97, 92.05, 92.27, 92.03, 92.19, 92.12, 91.76, 92.01, 91.8, 92.01, 91.67, 91.95, 92.1, 91.73, 91.57, 92.09, 91.56, 91.63, 91.92, 91.62, 91.81, 91.43, 91.42, 91.71, 91.81, 91.33, 91.56, 91.35, 91.55]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("", data, save_path)
