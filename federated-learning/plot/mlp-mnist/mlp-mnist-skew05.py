from plot.utils.skew import plot_skew

fed_server = [88.41, 88.6, 88.72, 89.02, 89.33, 88.9, 88.96, 89.09, 89.15, 89.21, 89.27, 89.63, 89.63, 90.0, 89.51, 90.18, 90.24, 90.3, 90.49, 90.0, 90.24, 89.88, 89.7, 90.61, 90.61, 90.98, 90.85, 90.79, 90.49, 90.73]
main_nn = [88.84, 88.84, 88.84, 88.96, 88.84, 88.9, 88.96, 88.96, 88.84, 88.96, 89.02, 89.09, 89.02, 88.78, 89.02, 88.96, 88.84, 88.96, 88.84, 88.96, 88.9, 88.9, 88.84, 88.9, 88.84, 88.78, 88.72, 88.78, 88.84, 88.72]
main_fed_localA = [88.41, 87.99, 88.29, 88.29, 88.23, 88.6, 88.48, 88.48, 88.23, 88.35, 88.35, 88.41, 88.48, 88.54, 88.48, 88.29, 88.35, 88.23, 88.29, 88.23, 88.48, 88.23, 88.35, 88.48, 88.41, 88.29, 88.48, 88.48, 88.41, 88.54]
main_fed = [85.98, 86.16, 86.34, 86.4, 86.46, 86.59, 86.83, 87.32, 87.26, 87.07, 87.2, 87.32, 87.44, 87.2, 87.62, 87.62, 87.87, 87.62, 87.8, 88.05, 87.99, 88.29, 88.41, 88.29, 88.78, 88.6, 88.84, 88.66, 88.6, 88.48]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}
plot_skew(data)
