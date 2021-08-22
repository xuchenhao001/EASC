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

fed_server = [40.35, 50.6, 55.7, 59.2, 61.8, 63.0, 64.1, 63.3, 64.85, 64.65, 64.8, 64.95, 65.1, 65.05, 65.5, 66.0, 65.95, 65.3, 66.4, 66.3, 66.05, 64.95, 66.0, 65.2, 65.85, 66.0, 65.55, 67.0, 67.1, 65.6, 66.6, 66.55, 66.55, 66.3, 66.35, 66.2, 66.8, 66.35, 66.95, 66.6, 66.9, 67.1, 66.35, 66.05, 66.25, 66.8, 66.9, 66.75, 66.7, 66.95]
main_fed_localA = [7.5, 37.3, 51.1, 57.2, 58.85, 60.7, 58.8, 60.55, 60.3, 60.95, 61.0, 56.65, 58.4, 61.15, 60.25, 60.9, 60.75, 60.85, 61.2, 61.0, 61.15, 61.2, 61.25, 61.1, 61.2, 61.25, 60.8, 61.05, 61.1, 60.9, 60.9, 61.0, 60.9, 60.95, 60.9, 60.85, 60.85, 60.95, 60.8, 60.9, 60.8, 60.9, 60.9, 61.0, 61.0, 61.0, 60.9, 60.9, 60.85, 60.9]
main_fed = [20.55, 27.6, 30.55, 32.5, 34.05, 36.3, 38.9, 40.8, 40.65, 41.15, 42.05, 42.5, 43.6, 43.9, 43.25, 43.95, 43.25, 43.05, 43.7, 43.7, 43.85, 44.1, 43.75, 44.05, 43.0, 43.4, 42.55, 42.85, 43.0, 43.65, 43.6, 43.0, 42.5, 43.5, 43.35, 43.45, 42.85, 44.9, 43.95, 44.5, 44.1, 43.65, 44.0, 43.6, 43.7, 43.1, 43.6, 43.9, 43.2, 43.65]
main_nn = [12.25, 43.15, 48.5, 55.1, 59.35, 57.55, 58.9, 60.3, 59.3, 59.4, 60.15, 60.0, 59.85, 59.85, 59.8, 59.75, 59.8, 59.75, 59.85, 59.8, 59.65, 59.65, 59.8, 59.85, 59.7, 59.75, 59.7, 59.75, 59.65, 59.55, 59.65, 59.75, 59.65, 59.65, 59.55, 59.6, 59.55, 59.55, 59.5, 59.6, 59.5, 59.5, 59.5, 59.5, 59.45, 59.45, 59.45, 59.5, 59.4, 59.5]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}
titleFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csTitleFont = {'fontproperties': titleFont}
# plt.title("No Skew (α=0.5~0.8)", **csTitleFont)

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_nn, label="Local Training", alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", alpha=0.5)
axes.plot(x, main_fed, label="FedAvg", alpha=0.5)

axes.set_xlabel("Training Round", **csXYLabelFont)
axes.set_ylabel("Average Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(30)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
