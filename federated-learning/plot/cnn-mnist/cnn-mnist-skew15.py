import sys

from plot.utils import plot_skew

apfl = [78.93, 80.54, 80.45, 80.58, 80.45, 80.21, 80.83, 80.5, 80.41, 27.98, 77.64, 79.92, 80.45, 80.37, 80.74, 80.87, 80.99, 80.79, 80.58, 72.23, 81.32, 81.24, 81.74, 81.24, 81.16, 81.12, 81.4, 81.36, 81.07, 83.39, 82.52, 81.82, 81.61, 81.57, 81.49, 81.32, 81.36, 80.95, 77.48, 84.96, 83.55, 82.73, 82.31, 81.98, 81.65, 81.86, 81.57, 81.03, 75.08, 78.93]
fedavg = [13.18, 79.09, 88.72, 90.37, 92.19, 93.97, 94.05, 95.37, 95.0, 94.83, 95.25, 95.99, 96.03, 96.24, 96.07, 96.57, 95.83, 96.65, 96.36, 96.32, 96.36, 96.36, 96.9, 96.69, 96.24, 96.45, 96.2, 96.49, 97.15, 96.9, 96.61, 96.98, 97.07, 96.98, 97.36, 97.36, 97.27, 96.94, 97.31, 97.07, 97.36, 97.31, 97.31, 96.69, 96.98, 97.19, 97.27, 97.48, 97.36, 97.31]
local = [79.63, 80.54, 80.08, 79.59, 80.74, 80.04, 80.45, 80.66, 80.29, 80.08, 80.17, 79.63, 72.23, 71.4, 71.65, 66.32, 59.88, 58.97, 61.9, 62.11, 56.36, 50.79, 51.03, 42.15, 44.79, 45.0, 39.17, 33.14, 33.43, 33.39, 33.22, 33.26, 32.89, 33.31, 32.81, 32.85, 32.69, 33.1, 29.38, 31.86, 32.44, 25.29, 25.5, 25.54, 25.58, 25.66, 25.79, 25.62, 25.54, 25.7]
scei = [79.5, 80.0, 81.2, 81.74, 83.39, 84.13, 85.12, 85.95, 86.07, 87.44, 87.07, 87.44, 88.72, 88.31, 88.55, 89.5, 89.3, 89.38, 89.55, 89.79, 89.55, 89.42, 90.54, 90.04, 89.92, 90.12, 90.54, 91.03, 90.7, 90.95, 90.41, 90.58, 90.62, 91.32, 90.54, 91.74, 91.53, 91.69, 91.28, 91.74, 91.61, 91.57, 91.57, 92.69, 91.57, 92.56, 92.19, 91.2, 91.94, 92.02]
scei_async = [77.77, 80.0, 80.45, 82.4, 83.14, 84.05, 83.88, 85.25, 85.7, 86.32, 86.9, 87.19, 86.98, 87.07, 87.02, 87.77, 88.22, 88.6, 88.6, 89.01, 89.67, 88.84, 89.09, 89.63, 89.88, 90.25, 90.04, 90.91, 90.87, 90.7, 90.58, 90.54, 90.41, 90.91, 91.82, 91.03, 91.12, 91.4, 90.91, 91.86, 91.82, 91.12, 90.95, 91.12, 90.54, 91.07, 90.99, 90.83, 90.66, 90.5]

data = {'SCEI': scei, 'SCEI-A': scei_async, 'APFL': apfl, 'FedAvg': fedavg, 'Local': local}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("", data, False, False, save_path, plot_size="4")
