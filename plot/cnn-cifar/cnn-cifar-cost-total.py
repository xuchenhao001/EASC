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
local_train = [1.51, 1.36, 1.42, 1.42, 1.44, 1.39, 1.4, 1.4, 1.5, 1.46, 1.52, 1.36, 1.39, 1.44, 1.45, 1.44, 1.4, 1.45, 1.48, 1.42, 1.37, 1.48, 1.4, 1.41, 1.44, 1.38, 1.44, 1.47, 1.38, 1.41, 1.36, 1.52, 1.43, 1.44, 1.4, 1.37, 1.43, 1.46, 1.48, 1.46, 1.33, 1.36, 1.46, 1.44, 1.4, 1.34, 1.42, 1.4, 1.33, 1.38]
fed_avg = [8.01, 5.25, 5.34, 5.32, 5.20, 5.46, 5.51, 5.31, 5.32, 5.15, 5.13, 5.20, 5.35, 5.31, 5.26, 5.18, 5.08, 5.09, 5.36, 5.24, 5.48, 5.17, 5.25, 5.16, 5.21, 5.43, 5.34, 5.26, 5.20, 5.04, 5.31, 5.13, 5.25, 5.14, 5.18, 5.39, 5.15, 5.21, 5.10, 5.05, 5.15, 5.22, 5.21, 5.20, 5.15, 5.22, 5.51, 5.42, 5.27, 3.77]
apfl = [3.92, 23.06, 2.87, 2.91, 2.85, 2.75, 2.69, 2.68, 2.60, 2.64, 2.43, 33.06, 2.76, 2.64, 2.70, 2.62, 2.69, 2.82, 2.82, 2.50, 2.66, 32.13, 2.72, 2.91, 2.62, 2.66, 2.77, 2.70, 2.57, 2.65, 2.55, 34.43, 2.74, 2.57, 2.86, 2.78, 2.63, 2.70, 2.60, 2.68, 2.48, 33.76, 2.71, 2.75, 2.55, 2.71, 2.53, 2.71, 2.85, 2.64]
scei = [16.34, 16.28, 16.54, 20.59, 17.13, 16.88, 16.94, 16.87, 17.85, 18.12, 16.73, 17.78, 17.93, 17.13, 18.60, 19.60, 18.37, 17.89, 21.67, 19.83, 19.27, 18.29, 18.98, 18.88, 18.62, 19.12, 19.29, 20.41, 19.41, 19.70, 20.80, 18.71, 19.60, 23.98, 23.77, 21.13, 19.83, 22.97, 20.19, 21.02, 20.47, 19.96, 19.47, 21.90, 21.54, 20.71, 21.18, 24.30, 23.12, 22.10]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, scei, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, local_train, label="Local Training", linestyle='--', alpha=0.5)
axes.plot(x, apfl, label="APFL", linestyle='--', alpha=0.5)
axes.plot(x, fed_avg, label="FedAvg", linestyle='--', alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Total Time Consumption (s)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
