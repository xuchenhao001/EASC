import sys

from plot.utils import plot_time_cost

apfl = [0.89, 0.01, 0.0, 0.02, 0.01, 0.01, 0.0, 0.01, 0.0, 0.16, 0.0, 0.0, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.0, 0.23, 0.0, 0.0, 0.0, 0.02, 0.01, 0.01, 0.0, 0.01, 0.0, 0.16, 0.01, 0.01, 0.0, 0.02, 0.01, 0.01, 0.01, 0.01, 0.0, 0.22, 0.0, 0.01, 0.0, 0.0, 0.01, 0.01, 0.01, 0.0, 0.01, 0.19]
fedavg = [0.88, 0.89, 0.24, 0.23, 0.29, 0.23, 0.23, 0.24, 0.25, 0.27, 0.23, 0.26, 0.29, 0.25, 0.25, 0.25, 0.26, 0.29, 0.32, 0.29, 0.36, 0.29, 0.31, 0.27, 0.23, 0.23, 0.31, 0.27, 0.28, 0.28, 0.43, 0.3, 0.39, 0.34, 0.28, 0.29, 0.33, 0.42, 0.39, 0.25, 0.35, 0.29, 0.28, 0.26, 0.27, 0.38, 0.25, 0.37, 0.25, 0.25]
scei = [4.36, 0.78, 0.78, 0.82, 0.76, 0.83, 0.79, 0.74, 0.84, 0.55, 0.85, 0.75, 0.58, 0.89, 0.75, 0.83, 0.77, 0.8, 0.82, 0.81, 0.68, 0.53, 0.81, 0.82, 0.79, 0.75, 0.96, 0.88, 0.87, 0.81, 0.77, 0.72, 0.6, 1.01, 0.81, 0.88, 0.91, 0.72, 0.63, 1.0, 1.11, 1.13, 0.55, 0.88, 0.9, 1.03, 1.06, 0.95, 0.64, 0.52]
scei_async = [3.4, 0.5, 0.37, 0.33, 0.33, 0.32, 0.33, 0.36, 0.34, 0.29, 0.32, 0.34, 0.32, 0.3, 0.32, 0.32, 0.29, 0.33, 0.46, 0.29, 0.31, 0.35, 0.33, 0.3, 0.34, 0.36, 0.31, 0.31, 0.36, 0.32, 0.31, 0.33, 0.31, 0.33, 0.39, 0.32, 0.31, 0.3, 0.31, 0.31, 0.31, 0.32, 0.32, 0.37, 0.33, 0.3, 0.31, 0.29, 0.31, 0.34]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_cost("", scei, scei_async, apfl, fedavg, None, True, False, save_path, plot_size="3")
