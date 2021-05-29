from plot.utils.convergence import plot_convergence_skew

network_5_node = [0.0, 0.0, 0.0, 0.0, 0.0, 1.43, 0.0, 0.0, 0.0, 1.43, 5.71, 5.71, 7.14, 5.71, 14.29, 20.0, 8.57, 8.57, 14.29, 10.0, 10.0, 10.0, 11.43, 27.14, 12.86, 25.71, 27.14, 21.43, 14.29, 30.0, 32.86, 31.43, 35.71, 35.71, 31.43, 32.86, 37.14, 28.57, 24.29, 32.86, 40.0, 27.14, 24.29, 31.43, 31.43, 30.0, 27.14, 30.0, 34.29, 32.86]
network_10_node = [88.72, 89.02, 89.7, 89.45, 89.51, 89.7, 89.63, 89.63, 89.82, 89.76, 90.0, 89.76, 90.3, 90.55, 90.55, 90.67, 90.73, 90.73, 90.79, 90.73, 91.04, 91.1, 91.46, 91.4, 91.71, 91.59, 91.71, 91.77, 92.2, 92.2, 91.77, 92.13, 91.65, 92.38, 92.44, 93.35, 92.5, 93.17, 92.87, 92.74, 92.62, 94.02, 92.56, 94.02, 95.06, 93.84, 93.54, 94.09, 94.33, 94.21]
network_20_node = [13.57, 14.29, 19.29, 27.14, 37.5, 41.79, 48.21, 50.0, 50.36, 52.14, 57.5, 60.71, 63.57, 64.29, 66.43, 67.14, 68.57, 72.14, 74.64, 72.14, 74.29, 72.86, 76.07, 75.36, 76.43, 77.5, 79.64, 77.86, 80.0, 81.07, 78.93, 80.71, 81.07, 81.07, 78.93, 80.36, 81.07, 82.14, 80.71, 82.14, 83.93, 83.57, 83.57, 82.86, 84.64, 84.64, 86.43, 84.29, 85.0, 86.07]

plot_convergence_skew("Skew 5%", network_5_node, network_10_node, network_20_node)
