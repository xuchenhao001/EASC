import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [90.27, 90.33, 90.67, 90.5, 91.07, 92.13, 91.67, 91.8, 92.0, 91.83, 91.53, 92.7, 92.3, 92.8, 92.57, 92.37, 92.53, 93.17, 91.93, 92.77, 92.7, 92.7, 92.8, 92.53, 93.27, 93.13, 92.17, 92.67, 92.3, 92.57, 91.33, 91.9, 92.57, 92.8, 91.8, 91.6, 92.93, 92.87, 92.43, 92.17, 92.33, 92.2, 92.23, 93.03, 92.63, 92.6, 92.73, 92.43, 92.8, 92.93]
network_10_node = [94.33, 95.27, 95.38, 95.48, 95.53, 95.27, 95.63, 95.63, 95.15, 95.67, 95.63, 95.62, 95.65, 95.58, 95.77, 95.68, 95.62, 95.42, 96.03, 96.15, 95.85, 95.62, 95.78, 95.57, 95.88, 95.83, 95.43, 96.08, 96.07, 95.8, 95.8, 95.85, 96.12, 96.1, 95.87, 95.9, 96.13, 95.93, 95.88, 96.2, 96.15, 96.25, 96.12, 96.18, 96.12, 96.27, 96.25, 96.1, 96.12, 96.2]
network_20_node = [70.67, 83.04, 86.27, 86.36, 87.28, 88.24, 88.77, 88.72, 90.55, 89.86, 90.47, 90.89, 91.12, 90.84, 91.11, 91.38, 91.52, 91.53, 91.31, 91.44, 91.88, 91.78, 92.15, 91.93, 91.77, 91.91, 92.37, 91.96, 91.74, 91.61, 91.37, 91.74, 91.62, 91.63, 91.48, 92.27, 91.72, 91.96, 91.61, 91.82, 91.62, 91.4, 91.38, 91.4, 91.27, 91.67, 91.8, 91.49, 91.56, 91.62]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("", network_5_node, network_10_node, network_20_node, save_path)