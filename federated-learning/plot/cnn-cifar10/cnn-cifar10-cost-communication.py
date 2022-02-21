import sys

from plot.utils import plot_time_cost

apfl = [0.01, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.01, 0.0, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.01, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.01, 0.0, 0.03, 0.0, 0.01, 0.0, 0.0, 0.01, 0.0, 0.01, 0.0, 0.0, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.01, 0.0, 0.03]
fedavg = [0.22, 0.29, 0.21, 0.25, 0.22, 0.23, 0.22, 0.23, 0.24, 0.21, 0.26, 0.27, 0.28, 0.25, 0.23, 0.26, 0.22, 0.22, 0.22, 0.3, 0.24, 0.21, 0.22, 0.24, 0.23, 0.28, 0.29, 0.29, 0.34, 0.26, 0.27, 0.24, 0.24, 0.23, 0.25, 0.24, 0.3, 0.25, 0.24, 0.26, 0.25, 0.29, 0.33, 0.23, 0.25, 0.22, 0.23, 0.21, 0.26, 0.25]
scei = [0.55, 0.75, 0.86, 0.77, 0.79, 0.94, 0.67, 0.9, 0.74, 0.83, 0.69, 0.83, 0.68, 0.93, 0.67, 0.83, 0.84, 0.5, 0.92, 0.77, 0.92, 0.87, 1.17, 0.6, 0.73, 0.63, 1.03, 1.09, 0.62, 0.85, 0.59, 0.7, 0.97, 0.95, 0.87, 0.89, 0.87, 0.59, 0.62, 0.73, 0.91, 0.66, 0.79, 0.7, 0.83, 0.95, 0.57, 0.57, 0.55, 0.63]
scei_async = [0.4, 0.31, 0.68, 0.34, 0.3, 0.54, 0.34, 0.41, 0.29, 0.32, 0.31, 0.34, 0.32, 0.35, 0.34, 0.34, 0.4, 0.35, 0.32, 0.38, 0.3, 0.34, 0.36, 0.3, 0.37, 0.29, 0.45, 0.35, 0.38, 0.39, 0.31, 0.43, 0.42, 0.4, 0.37, 0.31, 0.38, 0.37, 0.35, 0.39, 0.33, 0.29, 0.38, 0.36, 0.32, 0.36, 0.31, 0.35, 0.32, 0.33]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_cost("", scei, scei_async, apfl, fedavg, None, False, True, save_path, plot_size="4")
