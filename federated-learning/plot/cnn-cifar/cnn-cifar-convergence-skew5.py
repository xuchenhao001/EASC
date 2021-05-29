from plot.utils.convergence import plot_convergence_skew

network_5_node = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.86, 0.0, 1.43, 1.43, 0.0, 2.86, 0.0, 2.86, 2.86, 2.86, 2.86, 2.86, 2.86, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 2.86, 2.86, 2.86, 2.86, 1.43, 1.43]
network_10_node = [45.0, 53.05, 57.56, 59.33, 59.45, 61.83, 60.55, 61.16, 61.77, 63.35, 61.34, 61.34, 61.77, 62.87, 62.62, 63.11, 62.93, 63.17, 62.93, 63.78, 63.6, 63.78, 63.9, 63.48, 63.6, 64.63, 64.09, 64.15, 64.45, 64.15, 64.45, 64.94, 64.27, 64.09, 63.72, 64.27, 63.54, 63.9, 63.9, 63.48, 63.54, 63.41, 63.72, 64.27, 64.02, 63.35, 63.6, 63.9, 63.9, 63.84]
network_20_node = [6.79, 7.5, 11.07, 10.36, 10.0, 12.86, 12.86, 12.86, 15.0, 13.21, 15.71, 15.0, 15.71, 16.79, 16.43, 17.86, 18.57, 19.29, 19.29, 19.64, 20.36, 19.64, 20.36, 21.43, 21.79, 21.07, 22.5, 22.86, 22.5, 25.36, 23.93, 23.21, 24.64, 25.71, 23.93, 22.14, 24.64, 22.86, 22.5, 23.21, 24.64, 23.93, 21.79, 25.36, 24.29, 27.14, 25.36, 24.64, 25.71, 24.64]

plot_convergence_skew("Skew 5%", network_5_node, network_10_node, network_20_node)
