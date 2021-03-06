import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.43, 1.43, 1.43, 22.86, 17.14, 15.71, 18.57, 20.0, 21.43, 24.29, 24.29, 21.43, 22.86, 25.71, 24.29, 24.29, 30.0, 22.86, 21.43, 28.57, 30.0, 27.14, 30.0, 32.86, 27.14, 25.71, 34.29, 28.57, 28.57, 28.57, 27.14, 25.71, 30.0, 30.0, 30.0, 28.57, 30.0, 28.57, 28.57, 30.0, 28.57, 30.0, 28.57, 30.0]
network_10_node = [85.61, 86.59, 86.95, 86.83, 86.83, 86.77, 87.38, 87.5, 87.56, 87.5, 88.23, 87.8, 87.93, 87.93, 88.35, 88.54, 88.41, 88.17, 88.29, 88.41, 88.41, 88.6, 88.72, 89.02, 89.33, 88.9, 88.96, 89.09, 89.15, 89.21, 89.27, 89.63, 89.63, 90.0, 89.51, 90.18, 90.24, 90.3, 90.49, 90.0, 90.24, 89.88, 89.7, 90.61, 90.61, 90.98, 90.85, 90.79, 90.49, 90.73]
network_20_node = [13.93, 14.64, 19.29, 22.14, 31.07, 32.86, 36.07, 39.64, 39.29, 43.21, 48.21, 49.29, 52.86, 50.0, 53.93, 55.71, 56.43, 58.57, 57.14, 58.21, 58.93, 60.71, 60.36, 60.36, 63.21, 62.86, 64.64, 62.5, 63.21, 66.07, 63.57, 63.93, 66.43, 66.79, 66.43, 65.0, 65.0, 67.86, 64.29, 67.86, 66.79, 67.5, 63.93, 67.14, 70.0, 71.07, 69.29, 66.79, 69.29, 68.93]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("Skew 5%", network_5_node, network_10_node, network_20_node, save_path)
