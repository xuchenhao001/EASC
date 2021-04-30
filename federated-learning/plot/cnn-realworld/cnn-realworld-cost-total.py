# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

fed_server = [190.56, 190.27, 201.81, 194.25, 190.62, 196.07, 194.65, 187.69, 188.32, 188.31, 183.08, 189.18, 184.66, 189.78, 196.87, 190.4, 201.34, 192.5, 191.05, 194.5, 189.67, 191.49, 196.68, 190.42, 194.22, 192.9, 182.71, 186.06, 190.59, 193.5, 190.26, 198.55, 185.89, 187.3, 187.6, 183.61, 192.36, 188.79, 182.66, 195.22, 182.21, 190.62, 178.46, 197.63, 186.05, 197.81, 191.29, 190.97, 192.16, 197.03]
main_fed_localA = [22.26, 288.56, 26.03, 25.51, 24.9, 23.01, 24.25, 22.58, 23.06, 20.29, 18.82, 323.12, 23.35, 25.4, 23.94, 25.28, 24.06, 25.02, 23.54, 24.41, 20.48, 290.97, 26.09, 25.88, 25.54, 24.25, 22.6, 23.88, 23.99, 22.81, 20.13, 307.91, 29.37, 28.47, 26.78, 24.42, 23.95, 23.2, 22.49, 23.22, 19.67, 315.1, 25.55, 25.1, 24.55, 23.64, 22.39, 23.93, 21.61, 19.75]
main_fed = [233.02, 222.08, 215.7, 213.85, 209.95, 200.89, 201.05, 204.96, 213.32, 207.1, 216.29, 204.33, 208.95, 202.07, 215.96, 204.68, 208.69, 213.15, 209.04, 208.78, 214.66, 214.37, 209.51, 211.92, 199.92, 209.21, 206.13, 203.69, 201.45, 206.67, 208.58, 207.56, 208.4, 212.18, 208.85, 209.67, 208.2, 208.99, 208.89, 205.76, 201.58, 202.97, 205.88, 209.59, 207.14, 204.28, 197.72, 208.05, 203.42, 167.17]
main_nn = [9.47, 9.91, 11.59, 10.68, 10.17, 11.46, 10.82, 10.07, 11.09, 10.81, 10.21, 10.62, 10.53, 10.49, 11.26, 10.98, 10.71, 11.35, 11.49, 10.34, 10.94, 10.86, 10.75, 11.35, 11.44, 10.96, 11.16, 10.58, 10.7, 11.35, 11.62, 11.49, 11.39, 11.22, 11.07, 11.37, 11.27, 10.32, 11.05, 10.51, 9.81, 10.11, 9.92, 9.45, 9.78, 9.7, 8.91, 8.88, 8.73, 8.28]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_nn, label="Local Training", linestyle='--', alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", linestyle='--', alpha=0.5)
axes.plot(x, main_fed, label="FedAvg", linestyle='--', alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Total Time Consumption (s)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
