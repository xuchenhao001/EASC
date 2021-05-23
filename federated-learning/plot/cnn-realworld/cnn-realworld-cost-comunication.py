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
fed_server = [67.84, 50.12, 56.74, 53.36, 56.58, 39.2, 34.84, 60.94, 56.23, 56.33, 51.8, 48.42, 61.3, 55.3, 57.12, 50.9, 50.98, 29.77, 61.34, 60.42, 55.29, 53.06, 65.61, 57.92, 57.89, 63.92, 58.58, 53.24, 60.03, 50.85, 64.74, 52.45, 63.46, 43.92, 53.12, 65.31, 41.5, 58.84, 52.28, 51.35, 59.71, 60.34, 52.26, 61.74, 65.67, 54.75, 55.96, 50.21, 58.76, 47.1]
main_fed_localA = [5.78, 26.62, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.65, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.67, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.48, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
main_fed = [23.0, 13.33, 9.29, 7.66, 8.23, 9.18, 12.94, 10.24, 14.34, 7.89, 13.45, 7.2, 9.65, 12.81, 8.34, 11.21, 12.49, 9.03, 10.94, 10.63, 12.28, 11.55, 13.31, 8.44, 9.58, 12.93, 8.14, 13.68, 13.38, 12.02, 14.55, 7.88, 9.17, 8.01, 13.31, 10.91, 10.08, 11.1, 8.67, 7.99, 10.41, 12.04, 13.07, 11.91, 7.44, 9.91, 16.16, 10.48, 14.32, 11.71]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_fed, label="FedAvg", alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Communication Time Consumption (s)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
