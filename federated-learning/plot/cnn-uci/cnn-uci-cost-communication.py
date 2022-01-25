import sys

from plot.utils.time_cost import plot_time_cost

fed_server = [57.07, 47.12, 60.51, 60.63, 48.64, 48.09, 56.18, 45.12, 37.16, 57.97, 58.4, 50.76, 49.03, 48.47, 57.09, 50.37, 36.55, 48.2, 59.43, 50.96, 55.53, 52.25, 46.7, 50.64, 58.05, 48.71, 48.41, 53.1, 57.56, 38.44, 65.3, 58.7, 31.62, 61.14, 46.63, 48.74, 38.93, 55.68, 28.33, 49.13, 45.89, 47.44, 49.45, 49.25, 58.12, 47.73, 47.71, 48.03, 50.51, 33.29]
main_fed_localA = [4.81, 26.33, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.89, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.88, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
main_fed = [30.61, 16.8, 10.67, 15.34, 12.12, 14.46, 18.43, 19.06, 15.03, 15.29, 14.32, 17.15, 14.79, 14.48, 14.67, 17.99, 13.07, 9.57, 16.49, 12.88, 15.18, 15.62, 14.07, 16.36, 11.18, 13.23, 15.01, 14.72, 15.11, 12.45, 15.62, 15.01, 14.59, 12.74, 15.88, 14.7, 13.26, 15.6, 16.33, 14.42, 14.64, 15.52, 14.91, 12.3, 17.59, 16.12, 14.56, 16.25, 17.04, 14.16]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_cost("", fed_server, main_fed, main_fed_localA, None, save_path)