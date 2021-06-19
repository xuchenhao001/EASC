import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [83.93, 86.4, 87.27, 87.2, 87.67, 88.2, 88.53, 88.93, 89.0, 88.8, 88.53, 89.47, 89.73, 89.2, 89.53, 89.53, 89.73, 89.93, 89.67, 89.93, 90.2, 89.87, 90.27, 88.67, 90.13, 90.8, 90.4, 89.2, 90.13, 90.13, 90.27, 90.33, 90.0, 90.47, 89.93, 89.67, 90.33, 90.2, 89.93, 89.33, 90.27, 90.4, 90.53, 90.53, 90.6, 90.13, 89.8, 91.0, 89.87, 90.8]
network_10_node = [84.53, 86.03, 87.4, 88.4, 87.93, 88.77, 88.67, 88.33, 88.63, 89.4, 89.5, 89.37, 89.47, 89.5, 88.73, 89.47, 89.37, 90.07, 89.57, 90.23, 89.83, 90.5, 90.3, 90.47, 90.37, 90.17, 90.17, 90.23, 90.03, 90.67, 90.3, 90.73, 90.6, 90.27, 90.47, 90.9, 90.9, 90.67, 90.4, 90.43, 90.5, 90.43, 90.43, 90.93, 90.73, 91.23, 91.73, 91.13, 91.07, 90.83]
network_20_node = [82.15, 85.88, 86.97, 87.52, 87.78, 87.47, 88.25, 88.15, 88.28, 89.42, 88.93, 89.07, 89.03, 89.4, 89.18, 89.58, 89.93, 89.88, 89.78, 89.8, 89.28, 90.35, 89.85, 90.27, 90.35, 89.97, 90.8, 90.52, 90.88, 90.57, 90.83, 91.18, 91.05, 90.47, 91.15, 90.42, 90.95, 90.82, 90.9, 90.9, 91.4, 91.28, 91.42, 91.17, 91.62, 91.05, 91.42, 90.93, 91.17, 91.38]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("No Skew (α=0.5~0.8)", network_5_node, network_10_node, network_20_node, save_path)
