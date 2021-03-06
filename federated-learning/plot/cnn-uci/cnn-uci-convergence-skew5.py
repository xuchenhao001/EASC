import sys

from plot.utils.convergence import plot_convergence_skew

network_5_node = [0.0, 0.0, 0.0, 0.0, 0.67, 2.0, 2.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.67, 6.67, 5.33, 6.67, 8.67, 6.67, 7.33, 8.0, 8.67, 9.33, 10.0, 10.0, 14.0, 10.0, 11.33, 11.33, 18.0, 15.33, 14.0, 15.33, 16.67, 15.33, 15.33, 13.33, 16.0, 16.67, 14.0, 18.67, 18.67, 18.67, 15.33, 18.0, 20.0, 16.0, 17.33, 20.0]
network_10_node = [87.48, 88.65, 88.83, 89.25, 89.16, 89.54, 89.73, 90.38, 90.43, 91.17, 91.29, 91.67, 90.97, 91.44, 91.95, 91.76, 91.84, 92.16, 92.38, 92.08, 92.3, 92.3, 92.43, 92.16, 92.43, 92.54, 92.76, 92.75, 93.13, 93.11, 93.25, 93.03, 93.32, 93.3, 93.38, 93.19, 92.98, 93.11, 93.41, 93.13, 93.24, 93.25, 93.29, 93.16, 93.38, 93.46, 92.92, 93.35, 93.37, 93.21]
network_20_node = [21.83, 21.33, 29.17, 35.83, 42.83, 45.0, 53.0, 56.33, 65.83, 66.0, 70.67, 75.0, 77.33, 78.0, 77.5, 80.17, 77.17, 78.5, 79.67, 79.17, 79.17, 81.17, 80.67, 77.5, 79.5, 77.5, 77.5, 80.33, 81.83, 75.0, 80.67, 78.67, 81.33, 82.67, 83.33, 81.67, 84.83, 82.0, 83.0, 83.67, 83.0, 80.83, 80.67, 82.83, 84.83, 84.67, 83.83, 85.33, 85.33, 80.5]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_convergence_skew("Skew 5%", network_5_node, network_10_node, network_20_node, save_path)
