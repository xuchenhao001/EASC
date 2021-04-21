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
local_train = [1.2, 1.22, 1.19, 1.25, 1.29, 1.31, 1.28, 1.29, 1.27, 1.26, 1.29, 1.24, 1.26, 1.28, 1.27, 1.29, 1.34, 1.3, 1.3, 1.26, 1.27, 1.29, 1.29, 1.25, 1.31, 1.3, 1.25, 1.3, 1.28, 1.31, 1.29, 1.25, 1.25, 1.31, 1.27, 1.3, 1.25, 1.25, 1.31, 1.23, 1.24, 1.27, 1.28, 1.24, 1.23, 1.25, 1.21, 1.16, 1.14, 1.17]
fed_avg = [5.48, 3.57, 3.47, 3.65, 3.58, 3.53, 3.58, 3.44, 3.44, 3.50, 3.59, 3.70, 3.47, 3.47, 3.50, 3.50, 3.51, 3.72, 3.51, 3.58, 3.66, 3.54, 3.54, 3.66, 3.54, 3.49, 3.68, 3.52, 3.60, 3.59, 3.55, 3.62, 3.72, 3.53, 3.64, 3.44, 3.51, 3.74, 3.57, 3.50, 3.55, 3.49, 3.52, 3.66, 3.52, 3.52, 3.49, 3.68, 3.49, 2.66]
apfl = [2.21, 21.06, 2.56, 2.50, 2.52, 2.54, 2.46, 2.49, 2.53, 2.45, 2.32, 23.79, 2.47, 2.45, 2.45, 2.47, 2.49, 2.54, 2.50, 2.42, 2.49, 23.73, 2.50, 2.57, 2.52, 2.46, 2.48, 2.52, 2.45, 2.50, 2.41, 23.98, 2.54, 2.57, 2.49, 2.45, 2.45, 2.54, 2.55, 2.48, 2.39, 23.45, 2.53, 2.52, 2.49, 2.53, 2.54, 2.56, 2.67, 2.60]
scei = [12.79, 12.23, 12.96, 12.71, 14.19, 14.37, 13.83, 14.25, 13.35, 12.51, 13.17, 14.26, 14.52, 14.09, 13.03, 13.97, 14.74, 14.36, 15.48, 18.23, 15.68, 14.18, 13.23, 14.01, 15.39, 15.03, 14.73, 15.22, 14.75, 14.60, 14.58, 15.45, 15.76, 15.93, 20.96, 14.24, 13.73, 14.57, 13.74, 16.42, 16.56, 15.81, 16.11, 17.32, 14.29, 15.98, 16.22, 16.03, 15.79, 17.76]

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
