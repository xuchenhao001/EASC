import sys

from plot.utils.convergence import plot_main_fed_convergence

main_fed = [43.83, 45.1, 48.8, 49.53, 50.93, 51.57, 51.3, 53.97, 52.93, 54.87, 54.4, 57.17, 57.13, 58.2, 59.93, 60.57, 60.77, 62.47, 62.43, 61.8, 63.13, 63.1, 63.03, 63.77, 63.43, 64.63, 64.7, 63.1, 64.37, 64.83, 64.73, 65.3, 66.07, 65.67, 65.87, 66.03, 65.57, 66.83, 66.6, 66.57, 66.17, 67.73, 67.3, 67.43, 67.63, 67.63, 68.63, 67.67, 68.37, 69.9, 68.03, 68.83, 69.9, 69.13, 68.83, 70.2, 69.63, 69.77, 71.67, 70.2, 70.77, 70.17, 70.9, 71.13, 70.6, 70.77, 71.4, 70.2, 71.8, 71.13, 71.27, 70.8, 70.83, 71.07, 71.2, 71.87, 70.9, 71.7, 71.1, 72.07, 71.43, 70.7, 72.07, 71.93, 73.73, 72.9, 71.33, 70.97, 72.77, 72.4, 73.77, 71.5, 72.47, 72.8, 74.27, 74.27, 73.83, 71.4, 72.97, 74.47, 74.07, 73.27, 73.7, 73.83, 74.2, 74.33, 73.23, 73.77, 74.77, 73.57, 72.57, 74.23, 74.6, 73.8, 74.53, 73.57, 73.73, 74.47, 73.0, 74.33, 74.4, 73.83, 72.53, 74.57, 74.87, 73.8, 74.63, 73.77, 74.4, 74.53, 75.4, 74.93, 75.27, 74.47, 74.87, 73.03, 74.53, 75.37, 75.17, 76.17, 75.8, 72.83, 74.63, 74.97, 75.23, 74.83, 73.13, 74.67, 75.0, 74.9, 74.83, 75.83, 77.03, 75.93, 75.1, 75.2, 74.73, 75.17, 74.5, 75.47, 74.53, 75.2, 74.97, 75.67, 75.27, 75.2, 75.2, 73.47, 75.37, 75.47, 75.03, 75.27, 74.63, 74.83, 74.97, 75.2, 76.07, 75.93, 76.5, 76.23, 74.83, 76.03, 75.47, 75.7, 76.13, 75.33, 76.3, 76.3, 74.77, 75.2, 75.77, 76.6, 75.4, 75.33, 76.13, 75.7, 75.97, 75.7, 75.1, 76.3]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_main_fed_convergence("", main_fed, save_path)
