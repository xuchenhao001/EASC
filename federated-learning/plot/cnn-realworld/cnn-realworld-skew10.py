import sys

from plot.utils import plot_skew

apfl = [77.05, 77.27, 77.45, 77.25, 77.11, 76.77, 77.66, 77.43, 77.3, 77.0, 77.05, 76.89, 77.41, 78.07, 77.86, 77.43, 78.02, 78.16, 77.18, 77.36, 78.02, 77.8, 78.0, 77.95, 78.11, 78.68, 78.43, 78.43, 78.27, 78.11]
fedavg = [74.32, 75.2, 75.2, 74.59, 74.84, 76.09, 75.95, 74.86, 75.8, 76.41, 75.98, 76.23, 76.18, 76.48, 76.2, 76.25, 76.43, 76.27, 76.77, 76.75, 76.14, 76.98, 76.93, 76.52, 76.75, 76.91, 77.09, 76.59, 76.64, 76.68]
local = [76.82, 77.64, 77.09, 76.66, 76.89, 77.23, 76.8, 77.36, 77.52, 78.05, 77.45, 77.11, 77.16, 77.61, 77.5, 77.45, 77.48, 77.3, 77.45, 77.14, 77.8, 77.77, 78.05, 77.75, 77.77, 77.32, 77.57, 77.18, 77.45, 77.23]
scei = [79.91, 79.41, 80.91, 79.98, 80.27, 80.89, 81.23, 81.02, 81.64, 82.0, 82.45, 81.95, 81.59, 81.8, 82.11, 81.5, 82.39, 82.23, 82.27, 81.95, 83.05, 83.0, 82.18, 82.59, 82.95, 82.5, 83.23, 82.77, 83.36, 83.0]
scei_async = [76.36, 72.95, 78.18, 75.45, 78.18, 78.18, 76.36, 75.22, 78.40, 77.72, 77.27, 78.18, 78.18, 76.13, 74.31, 77.95, 77.04, 78.86, 78.63, 75.68, 77.04, 75.0 , 76.13, 78.40, 77.27, 78.86, 77.72, 78.63, 78.86, 77.72]

data = {'SCEI': scei, 'SCEI-A': scei_async, 'APFL': apfl, 'FedAvg': fedavg, 'Local': local}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("", data, False, False, save_path, plot_size="4")
