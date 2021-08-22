import sys

from plot.utils.skew import plot_skew

fed_server = [62.41, 61.32, 62.36, 61.7, 62.22, 62.45, 62.12, 63.3, 63.49, 62.12, 62.92, 63.02, 62.97, 62.83, 62.83, 62.78, 63.25, 62.88, 63.44, 63.11, 63.35, 63.77, 62.83, 62.69, 62.74, 63.3, 63.4, 63.35, 63.3, 63.68]
main_nn = [56.27, 56.27, 56.42, 56.46, 56.32, 56.37, 56.32, 56.37, 56.27, 56.18, 56.27, 56.37, 56.27, 56.27, 56.18, 56.23, 56.18, 56.18, 56.13, 56.23, 56.13, 56.13, 56.13, 56.13, 56.08, 56.08, 56.08, 56.13, 56.04, 56.13]
main_fed_localA = [57.69, 57.74, 57.78, 57.64, 57.74, 57.78, 57.36, 57.59, 57.64, 57.45, 57.45, 57.55, 57.45, 57.5, 57.45, 57.41, 57.41, 57.5, 57.36, 57.45, 57.36, 57.45, 57.45, 57.55, 57.55, 57.55, 57.45, 57.45, 57.41, 57.45]
main_fed = [43.49, 43.73, 43.35, 43.63, 42.59, 42.92, 42.17, 42.5, 42.5, 43.11, 43.07, 42.5, 41.93, 43.07, 42.88, 43.11, 42.5, 44.43, 43.44, 43.92, 43.35, 43.07, 43.4, 43.16, 43.16, 42.69, 43.07, 43.35, 42.64, 43.25]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("", data, save_path)
