import sys

from plot.utils.skew import plot_skew

fed_server = [87.89, 88.64, 89.42, 90.54, 90.04, 91.45, 88.8, 88.8, 90.58, 91.24, 89.75, 92.81, 90.99, 90.91, 90.0, 93.1, 92.19, 91.2, 92.31, 92.73, 93.6, 92.85, 93.22, 93.51, 92.93, 92.64, 94.09, 92.52, 93.14, 92.85]
main_nn = [81.16, 81.03, 80.91, 80.99, 80.95, 80.91, 80.99, 81.16, 81.12, 80.83, 81.07, 80.99, 81.07, 81.28, 81.24, 81.07, 80.99, 81.2, 81.03, 81.12, 81.16, 81.03, 81.07, 81.32, 81.24, 81.12, 81.16, 81.24, 81.32, 81.12]
main_fed_localA = [80.91, 81.07, 80.91, 80.5, 80.79, 81.16, 81.32, 81.03, 80.99, 81.07, 81.12, 81.12, 81.12, 81.03, 80.87, 81.07, 81.2, 81.16, 81.32, 81.16, 81.03, 80.95, 81.16, 81.07, 80.99, 81.16, 81.07, 80.91, 80.95, 81.16]
main_fed = [93.39, 93.8, 93.64, 93.84, 93.6, 94.05, 94.09, 94.01, 94.09, 94.26, 94.92, 94.88, 94.5, 94.67, 94.83, 95.04, 94.92, 95.08, 95.0, 95.04, 95.41, 95.79, 95.54, 95.41, 95.5, 95.41, 95.66, 95.87, 95.58, 95.74]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("Skew 15%", data, save_path)
