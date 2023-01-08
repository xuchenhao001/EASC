import sys

from plot.utils import plot_round_acc_nodes

scei005 = [62.3, 64.3, 66.2, 65.1, 62.8, 65.5, 62.2, 63.9, 64.7, 64.8, 61.4, 61.7, 62.8, 60.9, 61.8, 59.2, 62.0, 63.4, 60.8, 58.4, 63.8, 60.3, 62.7, 63.0, 63.3, 61.2, 62.0, 61.4, 59.4, 60.0, 60.3, 59.8, 59.5, 60.3, 61.0, 57.2, 59.6, 52.0, 59.5, 60.2, 60.4, 59.5, 59.6, 59.0, 59.5, 58.1, 58.4, 60.2, 58.8, 59.1]
scei010 = [64.9, 65.6, 67.25, 67.0, 66.85, 64.3, 63.9, 66.4, 65.05, 67.1, 66.1, 66.3, 65.45, 66.45, 65.15, 65.6, 65.85, 64.4, 63.85, 64.0, 61.65, 64.8, 66.05, 63.9, 65.25, 64.1, 63.35, 66.6, 62.05, 62.3, 65.3, 64.9, 66.0, 62.85, 64.05, 62.4, 63.1, 62.05, 66.6, 65.5, 61.35, 64.9, 62.6, 63.65, 63.3, 62.55, 60.55, 64.85, 62.4, 63.55]
scei020 = [62.92, 67.28, 65.75, 66.38, 66.18, 66.12, 65.55, 66.75, 65.47, 64.4, 65.6, 64.5, 65.65, 66.38, 64.6, 64.92, 65.68, 65.22, 66.25, 63.92, 64.05, 63.92, 64.03, 63.98, 63.85, 63.98, 63.72, 61.35, 63.35, 61.92, 62.6, 62.6, 62.18, 61.8, 62.12, 62.68, 61.45, 62.0, 60.35, 62.68, 62.72, 62.3, 60.82, 63.45, 59.12, 61.02, 64.28, 60.7, 64.05, 61.38]
scei050 = [62.02, 64.75, 67.78, 67.39, 66.44, 66.04, 66.66, 65.9, 66.36, 65.96, 66.45, 65.75, 66.92, 65.89, 66.25, 66.59, 66.9, 67.26, 66.72, 66.06, 66.73, 66.12, 65.97, 65.82, 66.13, 65.52, 66.33, 65.59, 64.99, 66.34, 66.09, 65.89, 65.99, 64.69, 65.26, 65.15, 65.21, 66.13, 65.52, 66.33, 65.59, 64.99, 66.34, 66.09, 65.89, 65.99, 64.69, 65.26, 65.15, 65.21]
scei100 = [62.42, 64.1, 65.94, 66.72, 65.61, 65.69, 66.1, 65.76, 65.52, 65.76, 65.85, 65.79, 65.81, 64.88, 65.22, 64.69, 64.64, 65.18, 64.87, 65.68, 65.65, 65.32, 64.96, 65.27, 65.59, 64.92, 64.78, 65.03, 65.55, 64.85, 65.03, 64.84, 65.48, 64.78, 64.71, 65.26, 64.98, 64.86, 64.99, 64.36, 65.32, 63.98, 65.02, 64.5, 64.72, 64.19, 64.28, 64.41, 64.38, 63.66]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc_nodes("", scei005, scei010, scei020, scei050, scei100, False, False, save_path, plot_size="4")