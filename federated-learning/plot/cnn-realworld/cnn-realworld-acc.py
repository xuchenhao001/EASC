# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```
import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import cycler

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

fed_server = [79.53, 82.25, 83.08, 83.47, 84.1, 84.38, 83.97, 84.58, 85.85, 86.15, 85.4, 86.6, 86.0, 86.75, 86.28, 86.88, 86.33, 87.25, 87.08, 87.47, 87.53, 87.7, 88.03, 88.17, 88.12, 87.78, 87.97, 88.78, 88.35, 88.17, 87.75, 88.33, 88.6, 89.03, 88.65, 88.25, 88.03, 88.55, 88.78, 89.03, 88.9, 88.28, 88.85, 88.95, 89.17, 88.67, 88.9, 88.67, 89.22, 89.2]
main_fed_localA = [8.53, 71.88, 79.8, 81.4, 82.5, 82.88, 83.1, 82.58, 82.78, 83.45, 82.42, 83.22, 84.42, 84.05, 85.12, 84.28, 84.03, 84.08, 84.35, 84.58, 84.75, 85.0, 85.2, 84.97, 84.83, 84.45, 85.42, 85.17, 85.03, 84.7, 84.75, 84.58, 85.15, 85.88, 85.65, 85.17, 85.83, 85.97, 84.9, 85.1, 85.83, 85.58, 85.8, 85.75, 85.9, 86.55, 86.25, 86.25, 86.08, 85.9]
main_fed = [51.12, 57.62, 62.95, 68.6, 70.03, 69.95, 71.45, 72.2, 71.7, 72.67, 72.55, 72.53, 73.85, 74.33, 74.12, 74.03, 75.1, 74.5, 75.25, 75.42, 74.92, 75.62, 75.58, 75.03, 75.22, 76.58, 76.42, 75.35, 76.33, 76.8, 76.42, 76.53, 76.72, 77.1, 76.62, 76.85, 77.1, 76.83, 77.33, 77.25, 76.62, 77.65, 77.42, 77.03, 77.22, 77.45, 77.53, 77.08, 77.15, 77.2]
main_nn = [14.68, 78.47, 80.78, 81.95, 82.88, 83.25, 83.85, 82.88, 83.55, 83.83, 83.8, 83.85, 83.15, 84.17, 84.25, 84.12, 84.83, 84.45, 83.95, 84.88, 84.5, 85.4, 84.8, 84.33, 84.58, 84.95, 84.47, 85.1, 85.28, 85.85, 85.2, 84.83, 84.88, 85.38, 85.25, 85.2, 85.22, 85.03, 85.2, 84.85, 85.58, 85.55, 85.85, 85.53, 85.55, 85.05, 85.33, 84.9, 85.2, 84.95]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}
titleFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csTitleFont = {'fontproperties': titleFont}
plt.title("No Skew (α=0.5~0.8)", **csTitleFont)

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_nn, label="Local Training", alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", alpha=0.5)
axes.plot(x, main_fed, label="FedAvg", alpha=0.5)

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(60, 94)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
