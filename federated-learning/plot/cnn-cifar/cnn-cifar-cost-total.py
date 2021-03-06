import sys

from plot.utils.time_cost import plot_time_cost

fed_server = [14.86, 14.09, 14.23, 14.86, 14.17, 14.53, 14.79, 15.48, 15.6, 15.87, 15.46, 14.52, 13.98, 13.99, 14.97, 15.72, 16.35, 15.85, 16.37, 15.13, 15.72, 16.56, 16.06, 15.77, 14.83, 16.06, 16.0, 14.82, 15.66, 16.81, 15.46, 16.37, 16.01, 14.93, 16.04, 15.74, 17.64, 15.05, 16.21, 16.48, 15.84, 15.71, 16.36, 16.57, 16.04, 15.46, 16.04, 17.1, 15.79, 16.24]
main_fed_localA = [2.37, 23.09, 2.76, 2.73, 2.69, 2.46, 2.35, 2.49, 2.41, 2.33, 2.44, 40.22, 2.87, 2.88, 2.8, 2.43, 2.43, 2.54, 2.41, 2.47, 2.39, 40.56, 2.73, 2.72, 2.76, 2.56, 2.54, 2.44, 2.42, 2.49, 2.3, 39.7, 2.78, 2.77, 2.67, 2.52, 2.6, 2.46, 2.47, 2.49, 2.38, 39.23, 2.75, 2.74, 2.7, 2.5, 2.46, 2.48, 2.41, 2.39]
main_fed = [5.87, 2.65, 2.7, 2.69, 2.76, 2.7, 2.7, 2.72, 2.63, 2.65, 2.7, 2.65, 2.64, 2.69, 2.81, 2.66, 2.69, 2.67, 2.67, 2.73, 2.7, 2.67, 2.72, 2.64, 2.7, 2.69, 2.71, 2.73, 2.65, 2.69, 2.65, 2.69, 2.65, 2.73, 2.68, 2.85, 2.65, 2.63, 2.77, 2.68, 2.81, 2.64, 2.7, 2.75, 2.68, 2.72, 2.68, 2.66, 2.65, 2.69]
main_nn = [1.14, 1.21, 1.17, 1.24, 1.24, 1.28, 1.31, 1.29, 1.31, 1.31, 1.26, 1.21, 1.23, 1.27, 1.29, 1.28, 1.22, 1.19, 1.31, 1.31, 1.24, 1.25, 1.32, 1.26, 1.35, 1.38, 1.25, 1.34, 1.2, 1.18, 1.32, 1.17, 1.23, 1.28, 1.24, 1.3, 1.29, 1.21, 1.3, 1.24, 1.22, 1.23, 1.21, 1.27, 1.17, 1.22, 1.22, 1.26, 1.23, 1.15]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_cost("Total Cost", fed_server, main_fed, main_fed_localA, main_nn, save_path)
