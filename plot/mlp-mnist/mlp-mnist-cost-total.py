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
local_train = [0.6, 0.6, 0.6, 0.62, 0.64, 0.64, 0.67, 0.66, 0.63, 0.64, 0.63, 0.61, 0.64, 0.65, 0.66, 0.66, 0.61, 0.64, 0.69, 0.65, 0.68, 0.71, 0.62, 0.65, 0.65, 0.65, 0.63, 0.71, 0.63, 0.63, 0.62, 0.67, 0.66, 0.64, 0.63, 0.61, 0.58, 0.6, 0.6, 0.59, 0.6, 0.61, 0.62, 0.62, 0.63, 0.63, 0.62, 0.61, 0.61, 0.61]
fed_avg = [4.81, 2.88, 2.89, 2.96, 2.91, 2.94, 3.08, 2.87, 2.89, 2.88, 2.93, 3.05, 2.88, 2.85, 2.86, 2.91, 2.87, 2.85, 2.86, 2.86, 2.85, 2.85, 2.85, 2.89, 2.84, 2.87, 2.88, 2.89, 2.88, 2.86, 3.36, 3.06, 2.86, 3.02, 2.98, 2.87, 2.88, 2.85, 2.86, 2.88, 2.83, 2.88, 2.85, 2.90, 2.94, 2.87, 2.87, 3.03, 2.90, 2.25]
apfl = [1.25, 21.23, 1.31, 1.31, 1.36, 1.28, 1.29, 1.29, 1.28, 1.30, 1.28, 35.53, 1.35, 1.33, 1.37, 1.30, 1.31, 1.32, 1.32, 1.32, 1.32, 36.22, 1.36, 1.36, 1.38, 1.30, 1.34, 1.33, 1.33, 1.34, 1.31, 36.84, 1.36, 1.35, 1.35, 1.31, 1.27, 1.26, 1.25, 1.29, 1.29, 33.22, 1.36, 1.36, 1.32, 1.32, 1.31, 1.30, 1.31, 1.31]
scei = [15.13, 14.40, 14.69, 14.33, 14.08, 15.14, 14.74, 15.12, 15.24, 16.06, 15.75, 15.56, 14.09, 14.82, 14.57, 15.09, 15.63, 15.37, 20.22, 18.65, 16.88, 16.21, 17.48, 16.12, 16.63, 21.50, 17.17, 16.20, 16.89, 17.33, 17.62, 21.35, 20.96, 22.05, 19.75, 20.74, 17.77, 17.40, 20.78, 20.97, 22.31, 21.68, 18.02, 20.06, 20.30, 19.86, 20.20, 18.65, 18.15, 18.78]

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
