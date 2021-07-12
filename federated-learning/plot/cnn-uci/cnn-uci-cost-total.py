import sys

from plot.utils.time_cost import plot_time_cost

fed_server = [217.68, 205.53, 215.87, 216.16, 204.21, 201.92, 214.38, 204.56, 187.9, 212.25, 211.23, 205.98, 202.81, 204.29, 210.44, 208.58, 190.94, 204.53, 212.18, 207.07, 213.53, 204.64, 201.18, 213.15, 212.72, 203.97, 204.81, 205.6, 211.86, 202.87, 218.36, 210.02, 185.26, 216.68, 203.2, 203.59, 186.9, 204.27, 187.04, 205.2, 205.37, 200.31, 204.01, 206.24, 215.59, 201.4, 203.07, 202.91, 202.74, 184.01]
main_fed_localA = [49.36, 285.18, 33.32, 33.26, 33.07, 33.94, 34.41, 31.17, 30.14, 29.05, 23.87, 474.62, 36.32, 35.62, 36.6, 37.36, 33.81, 30.0, 29.85, 31.51, 26.84, 461.82, 36.0, 35.85, 34.14, 33.32, 33.95, 33.34, 33.86, 33.68, 28.8, 415.99, 34.48, 34.01, 33.64, 33.21, 34.14, 32.89, 32.11, 30.2, 28.6, 334.92, 32.93, 33.14, 31.02, 32.0, 32.45, 30.9, 31.65, 27.56]
main_fed = [190.36, 168.52, 153.91, 157.51, 155.8, 169.01, 173.0, 172.0, 166.11, 168.12, 166.82, 170.41, 167.83, 170.1, 170.77, 171.2, 164.04, 163.03, 163.56, 161.86, 164.61, 166.14, 159.98, 164.04, 158.38, 159.15, 162.43, 162.72, 161.13, 158.24, 160.42, 159.93, 161.73, 158.61, 164.59, 159.65, 157.51, 161.58, 163.96, 159.05, 153.26, 153.27, 153.13, 153.27, 158.12, 155.57, 153.36, 155.38, 155.38, 152.48]
main_nn = [14.71, 16.15, 15.49, 15.44, 15.49, 15.25, 15.48, 15.42, 15.25, 15.46, 15.27, 15.48, 15.38, 15.45, 15.8, 15.59, 15.58, 15.84, 15.72, 15.99, 16.0, 16.15, 16.1, 16.0, 16.11, 16.15, 16.15, 16.07, 16.03, 16.09, 16.12, 15.94, 16.15, 16.02, 16.04, 16.02, 16.1, 16.19, 15.76, 14.63, 14.62, 14.05, 13.62, 12.91, 12.92, 12.81, 12.9, 12.89, 12.93, 12.94]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_cost("Total Cost", fed_server, main_fed, main_fed_localA, main_nn, save_path)
