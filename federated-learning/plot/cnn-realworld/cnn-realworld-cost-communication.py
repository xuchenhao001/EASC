import sys

from plot.utils.time_cost import plot_time_cost

fed_server = [58.51, 55.96, 60.74, 55.52, 39.37, 52.09, 45.84, 46.61, 41.54, 44.4, 54.46, 55.73, 54.34, 46.54, 53.96, 53.73, 42.19, 54.03, 38.2, 52.35, 49.75, 48.9, 43.46, 45.78, 54.61, 53.24, 52.05, 47.03, 53.0, 53.41, 48.96, 48.5, 56.01, 55.13, 59.32, 55.13, 58.37, 48.25, 49.74, 45.35, 46.89, 45.16, 57.95, 50.84, 58.67, 37.78, 57.57, 56.15, 55.24, 53.71]
main_fed_localA = [1.44, 21.21, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11.16, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.19, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
main_fed = [21.71, 15.52, 13.23, 12.09, 14.81, 12.03, 12.81, 11.27, 15.85, 15.0, 14.23, 15.59, 11.34, 13.25, 14.79, 12.83, 12.81, 10.98, 13.17, 12.74, 11.97, 13.12, 11.06, 8.2, 14.06, 12.77, 15.89, 13.78, 14.65, 13.71, 15.2, 12.71, 14.33, 9.57, 12.31, 12.09, 14.55, 15.06, 14.76, 16.65, 11.87, 12.91, 13.24, 11.81, 12.32, 14.6, 12.36, 12.82, 15.0, 14.69]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_cost("Communication Cost", fed_server, main_fed, main_fed_localA, None, save_path)
