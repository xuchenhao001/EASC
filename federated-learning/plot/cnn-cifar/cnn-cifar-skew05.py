import sys

from plot.utils.skew import plot_skew

fed_server = [65.91, 65.79, 65.43, 66.52, 66.71, 66.89, 66.71, 66.16, 66.22, 65.91, 66.71, 66.1, 66.28, 66.1, 66.46, 66.4, 66.16, 66.28, 65.61, 65.91, 66.04, 66.1, 66.04, 66.4, 66.1, 66.16, 66.16, 65.73, 66.1, 66.04]
main_nn = [64.57, 64.7, 64.63, 64.45, 64.45, 64.51, 64.45, 64.51, 64.45, 64.45, 64.45, 64.39, 64.39, 64.51, 64.39, 64.51, 64.57, 64.45, 64.51, 64.51, 64.51, 64.51, 64.51, 64.51, 64.51, 64.51, 64.51, 64.51, 64.45, 64.45]
main_fed_localA = [62.87, 62.38, 62.56, 62.68, 62.8, 62.56, 62.74, 62.68, 62.56, 62.74, 62.62, 62.87, 62.8, 62.93, 62.87, 62.74, 62.8, 62.74, 62.8, 62.74, 62.74, 62.8, 62.87, 62.74, 62.8, 62.87, 62.8, 62.74, 62.8, 62.74]
main_fed = [41.04, 40.24, 40.98, 40.98, 41.1, 41.4, 40.98, 41.59, 41.77, 41.04, 41.04, 41.59, 40.79, 41.04, 40.61, 40.85, 40.18, 39.94, 41.46, 39.94, 40.49, 40.61, 40.43, 41.04, 40.3, 40.06, 40.67, 40.37, 40.61, 40.98]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("Skew 5%", data, save_path)
