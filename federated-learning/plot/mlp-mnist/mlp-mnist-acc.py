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

fed_server = [96.4, 97.13, 97.4, 97.4, 97.27, 97.4, 97.53, 97.6, 97.67, 97.6, 97.8, 97.53, 97.73, 97.6, 97.67, 97.67, 97.53, 97.6, 97.33, 97.67, 97.47, 97.67, 97.73, 97.73, 97.8, 97.67, 97.6, 97.8, 97.73, 97.73, 97.6, 97.53, 97.47, 97.73, 97.6, 97.6, 97.6, 97.73, 97.8, 97.73, 97.73, 97.73, 97.6, 97.6, 97.67, 97.6, 97.6, 97.8, 97.67, 97.47]
main_fed_localA = [8.33, 89.4, 96.4, 96.93, 97.13, 97.27, 97.6, 97.53, 97.67, 97.67, 97.6, 95.87, 97.67, 97.4, 97.67, 97.67, 97.67, 97.67, 97.67, 97.73, 97.6, 97.47, 97.73, 97.67, 97.6, 97.6, 97.8, 97.67, 97.6, 97.73, 97.73, 97.67, 97.6, 97.6, 97.87, 97.67, 97.73, 97.6, 97.67, 97.53, 97.67, 97.53, 97.73, 97.67, 97.73, 97.67, 97.8, 97.8, 97.8, 97.73]
main_fed = [52.27, 62.73, 69.6, 72.67, 74.27, 76.4, 78.33, 79.4, 80.47, 81.8, 82.0, 82.33, 83.07, 83.93, 83.8, 84.53, 84.8, 85.67, 86.53, 86.67, 86.6, 86.8, 87.27, 87.0, 87.33, 87.33, 87.8, 87.73, 88.4, 88.13, 88.4, 88.2, 87.93, 88.4, 88.47, 88.8, 89.07, 89.07, 89.2, 89.0, 89.2, 89.47, 89.53, 89.73, 89.67, 89.67, 89.73, 89.73, 89.73, 89.53]
main_nn = [6.93, 93.07, 96.73, 96.8, 96.93, 96.87, 96.87, 96.8, 96.8, 96.73, 96.6, 96.8, 96.73, 96.8, 96.87, 96.8, 96.87, 96.73, 96.8, 97.0, 96.93, 96.93, 96.73, 97.13, 96.93, 96.8, 97.07, 97.0, 97.0, 96.87, 97.0, 97.07, 97.13, 97.13, 97.07, 97.07, 96.8, 96.87, 96.87, 96.87, 96.87, 96.8, 96.8, 96.87, 96.73, 96.73, 96.93, 96.8, 96.8, 96.93]

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
plt.ylim(85, 98)
plt.legend(loc="lower left", prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
