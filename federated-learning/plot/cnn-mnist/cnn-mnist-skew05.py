import sys

from plot.utils.skew import plot_skew

fed_server = [91.04, 91.1, 91.46, 91.4, 91.71, 91.59, 91.71, 91.77, 92.2, 92.2, 91.77, 92.13, 91.65, 92.38, 92.44, 93.35, 92.5, 93.17, 92.87, 92.74, 92.62, 94.02, 92.56, 94.02, 95.06, 93.84, 93.54, 94.09, 94.33, 94.21]
main_nn = [90.24, 90.18, 90.3, 90.12, 90.24, 90.18, 90.18, 90.24, 90.24, 90.3, 90.3, 90.24, 90.18, 90.37, 90.18, 90.3, 90.24, 90.18, 90.3, 90.18, 90.24, 90.3, 90.24, 90.43, 90.24, 90.37, 90.3, 90.24, 90.12, 90.18]
main_fed_localA = [90.06, 89.51, 89.88, 89.7, 89.94, 89.7, 90.0, 89.76, 89.76, 89.88, 89.88, 89.94, 89.7, 89.63, 89.88, 90.0, 89.94, 89.76, 89.88, 90.06, 89.94, 90.0, 90.0, 89.94, 90.0, 89.63, 89.76, 89.82, 89.76, 90.0]
main_fed = [94.7, 95.18, 94.45, 95.43, 95.49, 95.3, 95.73, 95.85, 96.28, 96.1, 95.79, 95.67, 96.1, 95.73, 96.46, 96.1, 95.79, 96.71, 96.52, 97.01, 96.4, 96.16, 95.73, 96.83, 96.83, 96.71, 96.83, 96.52, 96.83, 96.4]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew(data, save_path)
