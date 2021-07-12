import sys

from plot.utils.skew import plot_skew

fed_server = [91.84, 92.03, 92.03, 92.08, 92.5, 92.64, 92.26, 92.59, 92.5, 93.07, 92.74, 93.02, 93.02, 93.02, 93.02, 93.44, 93.02, 93.25, 93.16, 93.25, 92.97, 93.44, 93.63, 93.4, 93.63, 93.21, 93.63, 93.68, 93.58, 93.49]
main_nn = [88.87, 88.96, 88.87, 89.1, 88.96, 89.15, 89.1, 88.82, 89.2, 89.15, 89.29, 89.01, 88.87, 89.1, 89.1, 89.06, 89.1, 89.06, 89.01, 89.01, 89.01, 89.1, 88.82, 89.1, 88.87, 88.68, 88.87, 89.01, 89.06, 89.1]
main_fed_localA = [89.58, 89.39, 89.58, 89.39, 89.43, 89.48, 89.39, 89.43, 89.39, 89.25, 89.48, 89.43, 89.48, 89.48, 89.29, 89.48, 89.53, 89.43, 89.43, 89.43, 89.43, 89.53, 89.48, 89.39, 89.58, 89.62, 89.43, 89.43, 89.67, 89.39]
main_fed = [88.82, 88.92, 89.01, 89.1, 89.2, 89.29, 89.48, 89.81, 89.67, 89.62, 89.81, 90.05, 90.24, 90.09, 90.24, 90.47, 90.38, 90.24, 90.38, 90.66, 90.66, 90.57, 90.8, 90.8, 90.71, 90.8, 90.8, 90.8, 90.85, 90.94]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("Skew 5%", data, save_path)
