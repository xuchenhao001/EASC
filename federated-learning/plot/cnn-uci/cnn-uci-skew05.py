import sys

from plot.utils import plot_skew

apfl = [92.44, 92.45, 92.55, 92.38, 92.27, 92.48, 92.05, 92.44, 92.28, 92.43, 92.38, 92.26, 91.94, 92.45, 92.37, 92.49, 92.57, 92.21, 92.32, 92.5, 92.2, 92.41, 92.49, 92.33, 92.6, 92.27, 92.46, 92.22, 92.43, 92.22]
fedavg = [92.44, 92.07, 92.16, 92.44, 92.17, 92.3, 92.26, 91.9, 92.16, 91.91, 92.12, 91.8, 92.06, 92.24, 91.85, 91.68, 92.21, 91.67, 91.73, 91.99, 91.71, 91.9, 91.57, 91.55, 91.83, 91.93, 91.49, 91.68, 91.5, 91.67]
local = [90.82, 91.11, 91.16, 91.27, 91.33, 90.84, 90.83, 91.02, 91.0, 91.24, 91.21, 91.12, 90.77, 91.09, 90.95, 91.1, 91.15, 91.26, 90.82, 91.0, 91.0, 91.1, 91.23, 91.09, 91.11, 91.11, 91.02, 91.1, 90.99, 91.29]
scei = [94.13, 94.18, 94.01, 94.23, 94.5, 94.32, 94.32, 94.12, 94.16, 94.35, 94.52, 94.68, 94.29, 94.74, 94.74, 94.35, 94.65, 94.77, 94.82, 94.78, 95.01, 94.67, 94.65, 94.88, 94.62, 94.89, 94.88, 94.5, 94.79, 94.73]
scei_async = [88.53, 88.41, 85.60, 88.17, 89.87, 87.68, 86.58, 90.0 , 89.51, 88.41, 90.24, 89.87, 88.29, 90.0 , 89.26, 88.90, 89.14, 82.68, 87.68, 86.46, 89.26, 88.78, 88.41, 90.12, 88.29, 89.26, 89.14, 88.78, 89.51, 89.02]

data = {'SCEI': scei, 'SCEI-A': scei_async, 'APFL': apfl, 'FedAvg': fedavg, 'Local': local}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("", data, False, False, save_path, plot_size="4")
