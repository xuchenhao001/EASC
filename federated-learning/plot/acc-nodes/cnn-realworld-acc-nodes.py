import sys

from plot.utils import plot_round_acc_nodes

scei005 = [78.6, 80.75, 82.8, 84.35, 84.8, 81.45, 84.05, 80.95, 85.5, 84.0, 86.2, 83.55, 85.7, 84.2, 86.4, 85.5, 85.0, 85.2, 85.55, 86.7, 86.2, 84.4, 86.2, 86.4, 85.5, 84.5, 86.2, 86.5, 86.0, 86.5, 85.50, 86.7, 86.5, 85.0, 86.5, 86.4, 86.5, 86.0, 86.2, 87.5, 85.0, 86.2, 87.25, 86.37, 86.3, 87.4, 86.32, 85.4, 86.5, 86.0]
scei010 = [79.66, 80.45, 81.7, 83.05, 82.58, 83.5, 83.82, 83.89, 85.08, 86.02, 85.76, 86.52, 86.29, 86.64, 86.25, 86.05, 86.01, 86.46, 86.34, 86.57, 86.11, 86.64, 87.2, 86.87, 86.66, 87.45, 86.51, 86.97, 87.22, 86.62, 86.76, 87.95, 87.24, 87.25, 87.27, 86.65, 86.7, 87.2, 88.09, 88.4, 88.27, 88.46, 88.86, 88.12, 88.49, 88.35, 87.43, 87.95, 87.86, 88.01]
scei020 = [79.53, 82.25, 83.08, 83.47, 84.1, 84.38, 83.97, 84.58, 85.85, 86.15, 85.4, 86.6, 86.0, 86.75, 86.28, 86.88, 86.33, 87.25, 87.08, 87.47, 87.53, 87.7, 88.03, 88.17, 88.12, 87.78, 87.97, 88.78, 88.35, 88.17, 87.75, 88.33, 88.6, 89.03, 88.65, 88.25, 88.03, 88.55, 88.78, 89.03, 88.9, 88.28, 88.85, 88.95, 89.17, 88.67, 88.9, 88.67, 89.22, 89.2]
scei050 = [76.31, 79.34, 80.78, 81.43, 83.05, 83.84, 84.18, 85.0, 85.75, 85.5, 86.0, 86.75, 86.75, 87.75, 87.75, 87.0, 87.25, 87.5, 88.75, 88.75, 88.0, 88.75, 88.75, 89.0, 89.5 , 89.0 , 89.75, 89.5, 88.75, 88.0, 89.25, 89.25, 88.5, 89.5, 89.5, 89.5, 89.0, 89.0, 89.25, 89.5, 89.75, 89.5, 89.75, 89.5, 90.2, 90.0, 91.0, 91.0, 90.25, 90.5]
scei100 = [78.37, 79.48, 80.65, 81.14, 82.18, 83.21, 84.17, 85.08, 85.56, 86.19, 86.44, 87.01, 87.06, 87.06, 87.43, 87.7, 87.54, 87.72, 88.28, 88.12, 88.34, 88.5, 89.09, 89.26, 89.47, 89.07, 89.12, 89.23, 89.73, 89.63, 90.02, 89.73, 89.72, 89.28, 89.92, 89.25, 89.58, 89.01, 89.15, 89.18, 88.97, 89.48, 89.42, 90.05, 90.27, 89.89, 89.82, 90.01, 89.74, 90.01]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc_nodes("", scei005, scei010, scei020, scei050, scei100, False, False, save_path, plot_size="4")
