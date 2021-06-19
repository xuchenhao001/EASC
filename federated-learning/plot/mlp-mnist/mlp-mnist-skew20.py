import sys

from plot.utils.skew import plot_skew

fed_server = [69.68, 69.82, 70.23, 70.18, 71.27, 70.41, 70.5, 70.68, 70.95, 71.27, 71.27, 71.27, 72.36, 73.64, 73.18, 74.45, 74.82, 75.36, 75.5, 73.5, 74.45, 73.5, 73.27, 75.73, 76.0, 76.86, 76.45, 76.45, 76.18, 76.5]
main_nn = [66.23, 66.23, 66.23, 66.32, 66.23, 66.27, 66.32, 66.32, 66.23, 66.32, 66.36, 66.41, 66.36, 66.18, 66.36, 66.32, 66.23, 66.32, 66.23, 66.32, 66.27, 66.27, 66.23, 66.27, 66.23, 66.18, 66.14, 66.18, 66.23, 66.14]
main_fed_localA = [65.91, 65.68, 65.82, 65.86, 65.77, 66.05, 65.95, 65.95, 65.77, 65.86, 65.86, 66.0, 66.09, 66.09, 66.05, 65.91, 65.95, 65.86, 65.91, 65.86, 66.05, 66.0, 66.05, 66.14, 66.14, 65.95, 66.14, 66.05, 66.09, 66.14]
main_fed = [83.82, 84.14, 84.32, 84.32, 84.36, 84.64, 84.86, 85.23, 85.27, 85.14, 85.41, 85.68, 85.82, 85.73, 86.05, 86.0, 86.18, 86.09, 86.14, 86.36, 86.14, 86.55, 86.59, 86.55, 86.82, 86.68, 86.91, 86.73, 86.82, 86.82]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew(data, save_path)
