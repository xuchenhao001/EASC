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

fed_server = [93.41, 94.05, 94.5, 94.25, 94.51, 94.3, 94.19, 94.45, 94.81, 94.79, 94.91, 94.85, 93.91, 94.81, 94.9, 95.33, 95.1, 95.14, 95.1, 95.11, 95.51, 95.54, 95.35, 95.54, 95.81, 95.61, 95.58, 95.35, 95.4, 95.61, 95.66, 95.8, 95.39, 95.78, 95.71, 95.35, 95.65, 95.71, 95.71, 95.71, 95.86, 95.54, 95.55, 95.71, 95.54, 95.8, 95.72, 95.36, 95.6, 95.56]
main_fed_localA = [15.06, 90.83, 91.69, 92.89, 92.96, 93.29, 93.25, 93.34, 93.15, 93.8, 94.06, 93.67, 93.94, 93.99, 93.84, 93.9, 94.08, 93.86, 94.11, 94.0, 93.62, 93.72, 93.86, 94.04, 94.16, 93.92, 94.08, 94.08, 93.91, 94.04, 93.95, 93.99, 93.96, 93.83, 93.84, 93.91, 93.86, 93.86, 94.01, 93.84, 93.94, 93.86, 93.78, 93.85, 93.85, 93.88, 94.2, 93.81, 93.78, 93.8]
main_fed = [85.01, 87.5, 88.84, 89.81, 89.89, 90.28, 90.88, 90.71, 90.71, 91.34, 91.1, 91.46, 91.81, 91.85, 91.84, 91.55, 91.88, 91.97, 92.35, 92.25, 92.44, 92.06, 92.14, 92.44, 92.15, 92.29, 92.22, 91.89, 92.14, 91.89, 92.1, 91.8, 92.03, 92.22, 91.84, 91.67, 92.17, 91.64, 91.71, 91.97, 91.69, 91.88, 91.56, 91.54, 91.81, 91.91, 91.46, 91.66, 91.49, 91.66]
main_nn = [22.75, 92.12, 92.53, 92.45, 92.67, 92.85, 93.09, 92.89, 93.06, 93.64, 93.45, 93.12, 93.4, 93.45, 93.42, 93.19, 93.64, 93.34, 93.42, 93.58, 93.09, 93.39, 93.44, 93.55, 93.61, 93.11, 93.1, 93.3, 93.28, 93.53, 93.49, 93.4, 93.04, 93.36, 93.22, 93.38, 93.42, 93.54, 93.09, 93.28, 93.28, 93.38, 93.51, 93.36, 93.39, 93.39, 93.3, 93.38, 93.26, 93.58]

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
plt.ylim(80, 98)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
