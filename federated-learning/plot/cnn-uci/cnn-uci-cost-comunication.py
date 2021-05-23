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
fed_server = [73.7, 54.04, 47.94, 65.16, 59.47, 38.33, 54.3, 58.36, 54.49, 64.13, 52.46, 57.66, 51.83, 52.02, 65.83, 66.5, 51.79, 60.03, 59.72, 62.03, 54.57, 37.48, 33.72, 55.61, 60.31, 42.84, 54.46, 61.02, 54.79, 58.87, 63.05, 62.67, 56.11, 69.06, 54.11, 56.71, 52.53, 47.74, 42.04, 56.7, 66.34, 54.68, 60.3, 59.49, 53.8, 61.12, 36.98, 58.8, 61.69, 61.16]
main_fed_localA = [4.27, 25.18, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.89, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.17, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.44, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.65, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
main_fed = [31.56, 38.97, 43.45, 39.17, 33.96, 40.61, 40.9, 36.22, 41.57, 42.48, 40.69, 38.39, 36.16, 39.83, 36.94, 35.32, 42.83, 39.64, 41.34, 40.51, 45.49, 39.61, 34.34, 37.42, 39.85, 39.57, 43.7, 39.44, 36.85, 36.02, 40.15, 39.98, 35.54, 36.8, 36.4, 35.83, 36.59, 36.3, 36.81, 39.26, 36.62, 34.78, 40.46, 39.63, 31.92, 35.95, 41.98, 44.03, 36.8, 42.69]

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
