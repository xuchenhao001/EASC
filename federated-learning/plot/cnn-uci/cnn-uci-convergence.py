import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [90.62, 91.08, 91.2, 91.2, 91.55, 91.42, 91.7, 91.95, 92.75, 92.67, 92.4, 92.85, 92.12, 92.58, 92.7, 92.28, 92.22, 92.05, 92.42, 92.95, 92.7, 93.15, 93.08, 92.5, 93.1, 92.58, 92.75, 92.62, 92.95, 92.72, 92.72, 92.55, 92.38, 92.33, 92.67, 92.58, 92.72, 92.25, 92.5, 92.25, 92.03, 92.75, 92.5, 92.38, 92.08, 92.25, 92.22, 92.0, 92.28, 92.0]
network_10_node = [91.92, 92.97, 93.0, 93.3, 92.76, 93.54, 93.34, 93.61, 93.81, 93.92, 93.92, 94.1, 93.26, 94.31, 94.15, 94.46, 94.5, 94.1, 94.44, 94.39, 94.85, 94.83, 94.74, 94.1, 94.53, 94.95, 95.2, 94.67, 95.04, 94.7, 94.8, 95.08, 94.89, 94.81, 95.08, 94.59, 94.56, 93.91, 94.51, 94.75, 94.79, 94.89, 94.81, 95.05, 94.47, 94.59, 94.56, 94.21, 94.3, 94.61]
network_20_node = [92.39, 93.21, 93.3, 93.52, 93.61, 94.05, 93.84, 94.06, 94.22, 94.26, 94.5, 94.6, 94.33, 94.72, 94.31, 94.88, 94.78, 94.77, 94.83, 94.59, 94.8, 94.85, 94.63, 94.84, 95.06, 94.83, 94.97, 94.52, 94.87, 94.85, 95.21, 95.02, 94.89, 95.07, 95.04, 94.9, 95.0, 94.99, 94.88, 94.94, 94.79, 94.96, 94.62, 94.79, 94.73, 94.58, 94.75, 94.78, 94.72, 94.67]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("", network_5_node, network_10_node, network_20_node, save_path)
