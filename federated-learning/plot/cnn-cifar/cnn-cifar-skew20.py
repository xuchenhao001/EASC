import sys

from plot.utils.skew import plot_skew

fed_server = [49.32, 49.23, 49.05, 49.77, 50.0, 50.18, 50.14, 49.77, 49.82, 49.68, 50.05, 49.86, 50.09, 49.91, 50.18, 50.23, 49.73, 49.86, 49.68, 49.55, 49.82, 50.0, 49.91, 50.23, 49.82, 50.09, 50.18, 49.59, 50.09, 50.14]
main_nn = [48.14, 48.23, 48.18, 48.05, 48.05, 48.09, 48.05, 48.09, 48.05, 48.05, 48.05, 48.0, 48.0, 48.09, 48.0, 48.09, 48.14, 48.05, 48.09, 48.09, 48.09, 48.09, 48.09, 48.09, 48.09, 48.09, 48.09, 48.09, 48.05, 48.05]
main_fed_localA = [46.86, 46.5, 46.64, 46.73, 46.82, 46.64, 46.77, 46.73, 46.64, 46.77, 46.68, 46.86, 46.82, 46.91, 46.86, 46.77, 46.82, 46.77, 46.82, 46.77, 46.77, 46.82, 46.86, 46.77, 46.82, 46.86, 46.82, 46.77, 46.82, 46.77]
main_fed = [39.73, 38.55, 39.73, 39.55, 39.55, 39.86, 39.45, 40.32, 40.05, 39.64, 40.18, 40.41, 39.5, 40.45, 39.73, 40.0, 39.59, 38.95, 40.45, 39.05, 39.82, 39.86, 39.32, 40.09, 39.55, 39.32, 39.32, 39.18, 39.68, 39.45]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("Skew 20%", data, save_path)
