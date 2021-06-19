import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [0.0, 0.0, 0.0, 0.0, 0.0, 2.86, 0.0, 0.0, 0.57, 1.14, 1.14, 5.71, 5.71, 7.43, 13.14, 18.29, 13.71, 14.86, 17.14, 14.29, 15.43, 13.14, 12.0, 33.71, 16.0, 29.14, 32.57, 28.57, 20.57, 38.29, 39.43, 39.43, 40.0, 42.29, 37.14, 37.14, 41.71, 33.71, 27.43, 41.71, 44.57, 33.14, 31.43, 36.0, 32.57, 32.57, 32.57, 32.57, 39.43, 37.14]
network_10_node = [78.65, 78.92, 79.51, 79.3, 79.35, 79.51, 79.46, 79.62, 79.73, 80.11, 80.22, 80.16, 80.86, 81.46, 81.19, 81.41, 81.46, 81.84, 81.73, 81.95, 82.43, 82.59, 82.65, 83.08, 83.51, 83.03, 83.03, 83.62, 84.38, 84.32, 83.62, 84.27, 83.68, 85.57, 84.59, 87.03, 85.08, 86.43, 86.22, 85.51, 85.3, 88.11, 86.16, 87.89, 89.41, 87.19, 87.24, 87.73, 88.11, 88.54]
network_20_node = [13.71, 14.57, 18.14, 25.57, 36.43, 41.86, 49.43, 48.29, 51.0, 54.0, 56.29, 62.57, 61.14, 63.71, 67.14, 67.29, 68.71, 71.29, 73.86, 72.43, 74.0, 72.71, 74.0, 74.57, 76.86, 77.86, 80.43, 76.57, 79.86, 80.57, 80.0, 80.57, 81.86, 82.0, 80.14, 80.71, 82.57, 83.14, 82.86, 84.0, 84.14, 84.14, 84.0, 83.43, 85.0, 85.29, 87.0, 84.86, 86.0, 85.14]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("Skew 10%", network_5_node, network_10_node, network_20_node, save_path)
