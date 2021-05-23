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

fed_server = [234.68, 200.24, 211.44, 202.35, 211.73, 191.78, 206.75, 211.62, 213.14, 210.16, 207.31, 200.69, 213.0, 205.81, 206.37, 210.14, 202.81, 188.88, 214.39, 210.13, 209.71, 206.5, 216.81, 209.61, 210.02, 211.97, 209.91, 209.99, 212.45, 204.09, 220.55, 200.46, 212.27, 197.82, 209.65, 212.65, 187.25, 206.04, 202.49, 206.02, 205.99, 211.91, 210.75, 217.42, 215.32, 202.27, 208.48, 203.77, 216.02, 203.16]
main_fed_localA = [41.2, 276.3, 26.04, 24.33, 24.88, 23.13, 21.76, 21.42, 22.78, 23.37, 21.36, 372.61, 23.14, 24.62, 23.41, 21.81, 20.61, 21.24, 24.12, 21.29, 20.01, 367.21, 24.58, 25.2, 22.19, 22.19, 21.41, 25.09, 21.17, 18.73, 20.07, 379.56, 23.89, 23.68, 23.24, 22.84, 21.47, 23.12, 21.84, 18.01, 19.44, 358.3, 23.7, 23.07, 23.0, 21.15, 20.29, 21.03, 19.95, 17.35]
main_fed = [165.37, 156.42, 145.84, 144.95, 147.59, 145.44, 150.89, 148.69, 154.47, 146.65, 156.33, 146.52, 148.5, 148.55, 144.05, 148.74, 151.57, 145.98, 148.01, 150.78, 153.93, 153.49, 151.99, 143.73, 149.99, 154.14, 146.02, 147.77, 149.77, 147.1, 150.42, 143.38, 147.45, 143.88, 151.48, 148.72, 148.07, 149.53, 152.0, 145.1, 147.77, 146.42, 148.85, 148.94, 142.91, 150.38, 153.29, 146.39, 157.13, 154.95]
main_nn = [9.87, 10.94, 11.77, 11.97, 11.33, 11.86, 12.04, 11.65, 11.69, 11.71, 11.01, 12.0, 11.76, 11.43, 11.9, 11.7, 11.76, 11.81, 11.92, 11.33, 11.66, 11.94, 11.16, 11.82, 11.84, 11.81, 12.11, 12.45, 12.07, 11.77, 12.01, 11.73, 11.92, 11.69, 11.92, 11.58, 11.01, 10.49, 10.67, 10.86, 9.98, 10.39, 10.09, 9.85, 10.29, 10.07, 9.28, 9.05, 9.36, 8.7]

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
plt.tight_layout()
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
