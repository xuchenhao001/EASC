import sys

from plot.utils.skew import plot_skew

fed_server = [73.62, 73.48, 75.81, 73.87, 74.19, 75.08, 75.48, 75.62, 76.58, 76.71, 77.06, 77.02, 75.77, 76.4, 76.56, 75.75, 77.06, 77.12, 77.27, 76.6, 78.23, 77.87, 76.98, 77.56, 78.85, 77.42, 78.77, 78.52, 79.17, 78.42]
main_nn = [70.42, 71.17, 70.67, 70.27, 70.48, 70.79, 70.4, 70.92, 71.06, 71.54, 71.0, 70.69, 70.73, 71.15, 71.04, 71.0, 71.02, 70.85, 71.0, 70.71, 71.31, 71.29, 71.54, 71.27, 71.29, 70.87, 71.1, 70.75, 71.0, 70.79]
main_fed_localA = [70.62, 70.83, 71.0, 70.81, 70.69, 70.37, 71.19, 70.98, 70.85, 70.58, 70.62, 70.48, 70.96, 71.56, 71.37, 70.98, 71.54, 71.65, 70.77, 70.92, 71.52, 71.31, 71.52, 71.48, 71.65, 72.15, 71.96, 71.92, 71.79, 71.62]
main_fed = [73.1, 73.94, 74.02, 73.23, 73.56, 74.71, 74.71, 73.6, 74.5, 75.08, 74.75, 74.83, 75.02, 75.33, 75.02, 75.29, 75.42, 74.96, 75.73, 75.5, 74.92, 76.08, 75.71, 75.5, 75.6, 75.85, 76.0, 75.44, 75.73, 75.69]

data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_skew("Skew 20%", data, save_path)
