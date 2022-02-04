import sys

from plot.utils import plot_time_cost

apfl = [0.59, 0.0, 0.0, 0.0, 0.01, 0.0, 0.02, 0.03, 0.01, 0.13, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.02, 0.02, 0.01, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.01, 0.03, 0.01, 0.15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.02, 0.02, 0.01, 0.14, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.03, 0.03, 0.01, 0.19]
fedavg = [1.1, 0.54, 0.36, 0.39, 0.39, 0.34, 0.36, 0.51, 0.42, 0.38, 0.58, 0.38, 0.36, 0.42, 0.41, 0.32, 0.54, 0.38, 0.45, 0.39, 0.36, 0.36, 0.35, 0.41, 0.42, 0.46, 0.34, 0.35, 0.38, 0.47, 0.36, 0.37, 0.38, 0.42, 0.43, 0.38, 0.37, 0.61, 0.52, 0.55, 0.34, 0.41, 0.38, 0.43, 0.37, 0.37, 0.33, 0.33, 0.38, 0.39]
scei = [4.29, 1.1, 1.01, 0.97, 1.03, 0.76, 1.01, 0.84, 1.02, 0.66, 0.88, 1.02, 0.55, 0.96, 0.98, 0.94, 0.77, 0.96, 1.15, 0.9, 1.07, 0.76, 1.19, 1.01, 0.78, 1.02, 1.76, 1.02, 0.92, 1.02, 0.77, 1.02, 0.69, 0.93, 0.93, 0.89, 1.93, 0.9, 0.81, 1.12, 0.84, 1.24, 2.13, 1.15, 1.07, 0.71, 0.85, 1.02, 0.89, 0.73]
scei_async = [4.05, 0.52, 0.6, 0.51, 0.5, 0.44, 0.49, 0.66, 0.49, 0.52, 0.53, 0.56, 0.73, 0.49, 0.59, 0.58, 0.54, 0.65, 0.49, 0.48, 0.56, 0.48, 0.51, 0.62, 0.51, 0.54, 0.51, 0.76, 0.59, 0.53, 0.51, 0.83, 0.52, 0.56, 0.57, 0.53, 0.44, 0.51, 0.51, 0.54, 0.65, 0.7, 0.61, 0.56, 0.64, 0.52, 0.52, 0.5, 0.51, 0.51]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_cost("", scei, scei_async, apfl, fedavg, None, True, False, save_path, plot_size="3")
