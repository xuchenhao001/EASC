# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import cycler

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
fed_server = [19.3, 19.02, 18.99, 19.02, 18.96, 19.03, 19.41, 19.04, 18.96, 18.91, 19.0, 19.09, 18.91, 19.21, 16.97, 19.31, 18.93, 18.56, 19.0, 18.82, 18.86, 18.81, 18.75, 19.09, 17.0, 19.37, 19.22, 17.26, 19.12, 19.37, 19.43, 17.3, 19.21, 19.19, 19.07, 19.14, 19.09, 19.01, 17.19, 19.68, 19.51, 18.94, 16.83, 19.47, 19.01, 19.05, 19.2, 19.3, 19.19, 19.06]
main_fed_localA = [1.78, 22.76, 2.49, 2.45, 2.22, 1.94, 2.01, 2.01, 1.85, 1.89, 1.94, 38.54, 1.94, 1.9, 1.92, 1.93, 1.81, 1.78, 1.71, 1.73, 1.74, 30.83, 1.81, 1.84, 1.9, 1.92, 1.97, 1.9, 1.87, 1.83, 1.72, 28.41, 2.04, 1.93, 1.89, 1.83, 1.79, 1.78, 1.81, 1.83, 1.8, 28.64, 1.8, 1.83, 1.87, 1.95, 1.91, 1.87, 1.81, 1.73]
main_fed = [5.54, 2.41, 2.37, 2.41, 2.42, 2.36, 2.41, 2.37, 2.39, 2.39, 2.39, 2.38, 2.34, 2.47, 2.35, 2.36, 2.37, 2.33, 2.33, 2.4, 2.47, 2.37, 2.38, 2.35, 2.35, 2.34, 2.38, 2.46, 2.35, 2.41, 2.34, 2.34, 2.41, 2.37, 2.39, 2.39, 2.37, 2.36, 2.39, 2.45, 2.42, 2.33, 2.38, 2.39, 2.34, 2.39, 2.4, 2.39, 2.35, 2.38]
main_nn = [0.88, 0.86, 0.88, 0.87, 0.95, 0.9, 0.84, 0.91, 0.88, 0.85, 0.86, 0.87, 0.95, 0.9, 0.9, 0.89, 0.91, 0.92, 0.92, 0.89, 0.86, 0.87, 0.88, 0.85, 0.86, 0.85, 0.87, 0.86, 0.87, 0.9, 0.92, 0.88, 0.9, 0.87, 0.92, 0.85, 0.87, 0.84, 0.89, 0.9, 0.88, 0.89, 0.88, 0.89, 0.94, 0.86, 0.83, 0.84, 0.83, 0.82]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_nn, label="Local Training", alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", alpha=0.5)
axes.plot(x, main_fed, label="FedAvg", alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Total Time Consumption (s)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
