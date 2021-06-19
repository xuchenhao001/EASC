from plot.utils.time_cost import plot_time_cost

fed_server = [18.25, 18.1, 16.24, 18.07, 17.97, 18.13, 18.03, 17.14, 18.71, 18.49, 18.96, 18.95, 17.08, 18.8, 18.5, 18.3, 18.71, 18.4, 16.66, 16.37, 17.68, 19.51, 18.92, 17.62, 18.64, 18.81, 18.57, 18.39, 16.8, 18.66, 19.43, 17.15, 18.72, 18.4, 18.21, 18.45, 18.37, 18.34, 18.47, 18.59, 18.22, 18.62, 18.3, 18.81, 18.37, 18.22, 18.42, 18.52, 17.12, 18.6]
main_fed_localA = [1.52, 20.9, 1.56, 1.52, 1.51, 1.54, 1.53, 1.53, 1.52, 1.52, 1.48, 18.3, 1.56, 1.6, 1.58, 1.53, 1.52, 1.51, 1.5, 1.54, 1.48, 19.39, 1.51, 1.47, 1.52, 1.46, 1.49, 1.54, 1.49, 1.49, 1.52, 18.5, 1.49, 1.53, 1.54, 1.53, 1.47, 1.49, 1.52, 1.52, 1.43, 19.03, 1.57, 1.55, 1.54, 1.53, 1.55, 1.54, 1.55, 1.56]
main_fed = [4.87, 1.47, 1.46, 1.4, 1.47, 1.41, 1.49, 1.55, 1.45, 1.47, 1.48, 1.41, 1.44, 1.54, 1.49, 1.43, 1.43, 1.42, 1.4, 1.45, 1.42, 1.43, 1.4, 1.52, 1.42, 1.44, 1.45, 1.4, 1.42, 1.4, 1.45, 1.45, 1.43, 1.42, 1.42, 1.46, 1.44, 1.43, 1.42, 1.45, 1.46, 1.48, 1.45, 1.43, 1.46, 1.53, 1.43, 1.4, 1.46, 1.44]
main_nn = [0.76, 0.76, 0.74, 0.75, 0.77, 0.76, 0.77, 0.8, 0.76, 0.77, 0.8, 0.78, 0.75, 0.77, 0.76, 0.75, 0.78, 0.78, 0.78, 0.79, 0.77, 0.81, 0.77, 0.82, 0.81, 0.79, 0.79, 0.78, 0.78, 0.78, 0.79, 0.78, 0.76, 0.8, 0.76, 0.79, 0.81, 0.8, 0.79, 0.78, 0.78, 0.8, 0.77, 0.77, 0.79, 0.79, 0.79, 0.79, 0.76, 0.75]

plot_time_cost("Total Cost", fed_server, main_fed, main_fed_localA, main_nn)
