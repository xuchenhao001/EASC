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

fed_server = [95.6, 96.75, 96.9, 97.7, 97.45, 97.55, 97.6, 97.7, 97.85, 97.8, 97.95, 98.05, 97.65, 98.2, 98.1, 98.3, 98.15, 98.3, 98.2, 97.9, 98.45, 98.4, 98.15, 98.6, 98.35, 98.3, 98.5, 98.55, 98.6, 98.5, 98.5, 98.45, 98.45, 98.35, 98.3, 98.5, 98.65, 98.45, 98.4, 98.4, 98.7, 98.5, 98.6, 98.4, 98.75, 98.65, 98.6, 98.55, 98.55, 98.55]
main_fed_localA = [5.2, 84.15, 96.1, 97.0, 97.3, 97.4, 97.6, 97.8, 97.25, 97.9, 97.65, 97.9, 97.9, 97.85, 97.8, 97.8, 97.9, 98.0, 97.95, 97.9, 97.95, 97.95, 97.85, 97.95, 97.9, 98.05, 98.05, 97.95, 98.2, 97.8, 98.15, 97.95, 97.85, 97.8, 97.9, 98.1, 97.85, 97.9, 97.9, 98.15, 97.95, 98.0, 98.0, 98.2, 98.0, 98.0, 97.95, 98.15, 98.05, 97.85]
main_fed = [47.75, 77.9, 87.9, 90.5, 92.5, 92.65, 93.65, 94.3, 94.5, 94.7, 94.65, 95.1, 95.65, 95.75, 95.75, 95.65, 96.15, 95.9, 96.3, 96.2, 96.25, 96.3, 96.2, 96.7, 96.4, 96.65, 96.6, 96.55, 96.45, 97.05, 96.8, 96.9, 97.05, 96.95, 97.0, 97.15, 96.95, 97.2, 97.25, 97.35, 97.25, 97.05, 97.3, 97.3, 97.45, 97.3, 97.6, 97.65, 97.45, 97.45]
main_nn = [7.0, 93.55, 96.05, 96.65, 96.85, 97.4, 97.3, 97.35, 97.7, 97.5, 97.55, 97.75, 97.5, 97.9, 97.8, 97.75, 97.7, 97.8, 97.75, 97.85, 97.75, 97.8, 97.95, 97.75, 97.7, 98.05, 97.95, 97.9, 97.95, 98.1, 98.0, 98.2, 98.05, 97.8, 98.0, 97.8, 98.0, 98.15, 97.95, 98.05, 97.95, 97.95, 98.15, 97.7, 98.15, 98.05, 98.1, 97.85, 98.0, 97.85]

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
# axes.plot(x, scei, label="SCEI with negotiated α", linewidth=3, color='#1f77b4')


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
