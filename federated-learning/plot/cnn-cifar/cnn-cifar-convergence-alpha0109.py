import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [45.6, 52.27, 55.07, 60.4, 61.73, 62.67, 64.93, 67.73, 66.67, 65.07, 65.47, 65.6, 68.4, 68.27, 67.6, 68.13, 68.27, 67.47, 66.93, 68.4, 68.53, 67.73, 68.27, 68.4, 68.8, 69.2, 68.53, 68.13, 68.13, 68.13, 68.8, 68.27, 68.53, 68.13, 68.0, 67.73, 68.67, 67.87, 67.6, 68.0, 68.27, 68.27, 67.73, 67.87, 68.0, 68.4, 67.73, 67.6, 67.07, 66.93]
network_10_node = [48.27, 57.27, 61.8, 66.13, 67.07, 69.8, 69.93, 68.4, 69.8, 69.8, 69.73, 69.53, 69.0, 69.07, 69.4, 70.0, 69.27, 69.53, 69.53, 69.67, 69.27, 69.8, 69.67, 69.4, 68.87, 69.87, 70.07, 70.0, 69.93, 69.67, 70.0, 70.2, 70.4, 70.13, 69.73, 69.33, 69.87, 69.67, 69.4, 70.07, 70.2, 70.07, 69.73, 70.33, 70.2, 70.2, 70.13, 70.07, 69.6, 70.2]
network_20_node = [29.57, 36.3, 38.4, 37.6, 40.53, 39.87, 44.0, 42.03, 43.8, 41.23, 45.17, 44.03, 42.47, 44.27, 48.3, 45.1, 48.0, 48.13, 49.17, 50.9, 52.17, 50.4, 50.3, 51.07, 50.9, 50.17, 52.97, 49.93, 52.27, 52.13, 51.47, 49.6, 50.63, 52.33, 52.1, 52.27, 51.9, 51.97, 52.43, 50.6, 52.13, 51.57, 51.47, 51.77, 51.27, 52.23, 51.8, 50.17, 52.73, 51.73]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("No Skew (α=0.1~0.9)", network_5_node, network_10_node, network_20_node, save_path)
