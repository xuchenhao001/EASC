import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [95.73, 96.8, 96.93, 97.33, 97.47, 97.33, 97.33, 97.33, 97.2, 97.2, 97.2, 97.33, 97.2, 97.33, 97.33, 97.33, 97.33, 97.47, 97.47, 97.47, 97.73, 97.47, 97.47, 97.2, 97.33, 97.73, 97.47, 97.6, 97.47, 97.73, 97.6, 97.47, 97.33, 97.6, 97.6, 97.47, 97.47, 97.33, 97.47, 97.47, 97.2, 97.33, 97.33, 97.47, 97.6, 97.47, 97.47, 97.47, 97.33, 97.2]
network_10_node = [95.53, 96.47, 96.73, 97.07, 97.13, 97.2, 97.13, 97.27, 97.07, 97.33, 97.0, 97.13, 97.4, 97.07, 97.47, 97.07, 97.2, 97.13, 97.13, 97.6, 97.13, 97.47, 97.33, 97.47, 97.47, 97.2, 97.13, 97.53, 97.53, 97.4, 97.27, 97.27, 97.4, 97.47, 97.2, 97.47, 97.33, 97.47, 97.2, 97.2, 97.2, 97.2, 97.13, 97.2, 97.47, 97.47, 97.47, 97.33, 97.53, 97.47]
network_20_node = [61.3, 72.33, 75.17, 80.5, 81.27, 84.23, 84.37, 86.07, 86.07, 87.03, 87.47, 88.5, 87.63, 89.8, 88.5, 89.93, 88.83, 89.27, 88.93, 89.4, 89.2, 89.73, 89.83, 90.33, 90.0, 89.5, 90.33, 90.73, 90.13, 90.47, 90.07, 90.77, 90.4, 90.57, 90.73, 91.1, 90.97, 90.9, 90.8, 90.97, 90.73, 91.47, 91.27, 91.2, 91.33, 91.2, 91.47, 91.67, 91.53, 91.17]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("No Skew (α=0.1~0.9)", network_5_node, network_10_node, network_20_node, save_path)
