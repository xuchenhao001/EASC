import sys

from plot.utils.skew import plot_skew

fed_server = [83.92, 84.88, 86.04, 87.31, 86.81, 88.15, 85.31, 84.96, 87.0, 88.12, 86.15, 90.23, 87.73, 88.12, 86.69, 90.35, 88.88, 87.81, 89.42, 89.77, 91.31, 90.5, 90.81, 91.5, 90.77, 90.46, 92.46, 90.15, 90.88, 90.46]
main_nn = [75.54, 75.42, 75.31, 75.38, 75.35, 75.31, 75.38, 75.54, 75.5, 75.23, 75.46, 75.38, 75.46, 75.65, 75.62, 75.46, 75.38, 75.58, 75.42, 75.5, 75.54, 75.42, 75.46, 75.69, 75.62, 75.5, 75.54, 75.62, 75.69, 75.5]
main_fed_localA = [75.31, 75.46, 75.31, 74.92, 75.19, 75.54, 75.69, 75.42, 75.38, 75.46, 75.5, 75.5, 75.5, 75.42, 75.27, 75.46, 75.58, 75.54, 75.69, 75.54, 75.42, 75.35, 75.54, 75.46, 75.38, 75.54, 75.46, 75.31, 75.35, 75.54]
main_fed = [92.54, 92.73, 92.85, 92.85, 92.92, 93.23, 93.15, 93.19, 93.23, 93.58, 94.0, 93.92, 93.65, 94.08, 94.04, 94.19, 93.85, 94.5, 94.27, 94.35, 94.85, 95.31, 94.96, 94.81, 94.96, 94.85, 95.31, 95.27, 95.19, 95.04]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("Skew 20%", data, save_path)
