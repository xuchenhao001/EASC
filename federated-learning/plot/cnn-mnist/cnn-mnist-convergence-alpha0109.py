import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [93.47, 95.2, 96.8, 98.0, 97.2, 97.47, 97.87, 98.13, 98.13, 98.13, 98.4, 98.53, 98.13, 97.87, 98.0, 98.0, 98.0, 98.0, 98.27, 98.0, 98.13, 98.27, 98.13, 97.87, 98.27, 98.27, 98.4, 98.13, 98.27, 98.27, 98.0, 98.4, 98.13, 98.27, 98.27, 98.13, 98.53, 98.53, 98.93, 98.0, 98.53, 98.93, 98.8, 98.67, 98.53, 98.67, 98.4, 98.67, 98.27, 98.4]
network_10_node = [96.13, 97.6, 98.27, 97.93, 98.13, 98.47, 98.67, 98.33, 98.6, 98.67, 98.4, 98.87, 98.8, 98.6, 98.67, 98.8, 98.87, 98.73, 98.93, 98.93, 99.0, 99.0, 98.87, 98.87, 99.07, 98.93, 99.27, 99.27, 98.8, 99.0, 99.2, 99.0, 99.2, 99.33, 99.13, 99.07, 99.0, 99.2, 99.07, 99.13, 99.13, 99.13, 99.2, 99.27, 99.07, 99.27, 99.2, 99.2, 99.13, 99.07]
network_20_node = [61.5, 74.57, 83.57, 85.0, 87.9, 87.97, 90.47, 91.83, 92.77, 93.27, 94.43, 94.47, 94.4, 94.7, 95.2, 95.03, 95.03, 95.73, 95.07, 95.8, 95.4, 95.7, 95.6, 95.8, 95.97, 95.83, 95.67, 95.8, 96.2, 96.37, 96.1, 96.07, 96.1, 96.07, 96.57, 96.87, 96.13, 96.53, 96.87, 96.43, 96.5, 96.63, 96.83, 96.37, 96.77, 96.93, 97.03, 96.83, 96.87, 96.77]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("No Skew (α=0.1~0.9)", network_5_node, network_10_node, network_20_node, save_path)
