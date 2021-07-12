import sys

from plot.utils.skew import plot_skew

fed_server = [54.88, 53.84, 54.79, 54.5, 54.75, 54.92, 54.83, 55.58, 55.74, 54.75, 55.21, 55.41, 55.5, 55.45, 55.37, 55.21, 55.7, 55.5, 56.12, 55.45, 55.7, 56.32, 55.41, 55.62, 55.25, 55.7, 55.91, 55.91, 55.99, 56.2]
main_nn = [49.3, 49.3, 49.42, 49.46, 49.34, 49.38, 49.34, 49.38, 49.3, 49.21, 49.3, 49.38, 49.3, 49.3, 49.21, 49.26, 49.21, 49.21, 49.17, 49.26, 49.17, 49.17, 49.17, 49.17, 49.13, 49.13, 49.13, 49.17, 49.09, 49.17]
main_fed_localA = [50.54, 50.58, 50.62, 50.5, 50.58, 50.62, 50.25, 50.45, 50.5, 50.33, 50.33, 50.41, 50.33, 50.37, 50.33, 50.29, 50.29, 50.37, 50.25, 50.33, 50.25, 50.33, 50.33, 50.41, 50.41, 50.41, 50.33, 50.33, 50.29, 50.33]
main_fed = [41.36, 41.36, 40.91, 41.28, 40.58, 41.07, 40.25, 40.79, 40.66, 41.03, 41.32, 40.5, 39.92, 40.95, 40.74, 40.87, 40.5, 42.23, 41.32, 41.74, 41.53, 41.24, 41.49, 41.03, 41.36, 40.95, 41.07, 41.32, 40.74, 41.28]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("Skew 15%", data, save_path)
