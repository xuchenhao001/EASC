from plot.utils.skew import plot_skew

fed_server = [75.23, 75.38, 75.88, 75.93, 76.73, 76.28, 76.33, 76.48, 76.53, 76.83, 76.83, 76.78, 77.39, 78.39, 77.94, 78.74, 79.4, 79.6, 79.65, 78.39, 78.89, 78.24, 78.04, 79.9, 80.2, 80.9, 80.75, 80.95, 80.55, 80.45]
main_nn = [73.22, 73.22, 73.22, 73.32, 73.22, 73.27, 73.32, 73.32, 73.22, 73.32, 73.37, 73.42, 73.37, 73.17, 73.37, 73.32, 73.22, 73.32, 73.22, 73.32, 73.27, 73.27, 73.22, 73.27, 73.22, 73.17, 73.12, 73.17, 73.22, 73.12]
main_fed_localA = [72.86, 72.66, 72.96, 72.96, 72.86, 73.17, 73.07, 73.07, 72.86, 72.91, 72.96, 73.07, 73.12, 73.17, 73.12, 72.96, 73.02, 72.91, 72.96, 72.91, 73.12, 72.91, 72.96, 73.07, 73.07, 72.91, 73.12, 73.12, 73.07, 73.17]
main_fed = [84.52, 84.92, 85.13, 85.23, 85.23, 85.43, 85.53, 86.23, 86.03, 85.83, 86.13, 86.18, 86.28, 86.18, 86.68, 86.58, 86.68, 86.53, 86.73, 86.98, 86.83, 87.24, 87.39, 87.34, 87.79, 87.54, 87.59, 87.44, 87.49, 87.44]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}
plot_skew(data)
