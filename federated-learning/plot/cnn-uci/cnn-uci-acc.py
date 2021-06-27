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

fed_server = [95.78, 96.3, 96.4, 96.22, 96.47, 96.45, 96.25, 96.57, 96.72, 96.93, 96.5, 97.03, 96.8, 96.7, 96.87, 96.95, 97.03, 96.9, 96.87, 96.93, 97.23, 97.4, 97.13, 96.82, 97.2, 97.4, 97.25, 96.77, 97.2, 96.5, 96.95, 97.3, 97.15, 96.97, 97.23, 97.28, 97.32, 96.83, 97.33, 97.25, 97.28, 97.32, 96.93, 96.72, 97.13, 97.38, 97.37, 96.93, 97.18, 97.12]
main_fed_localA = [13.68, 86.23, 91.95, 92.48, 92.3, 92.78, 92.93, 92.77, 92.72, 92.93, 93.23, 92.82, 93.53, 93.58, 93.48, 93.4, 93.82, 93.38, 93.57, 93.45, 93.88, 93.2, 93.48, 93.8, 93.6, 93.55, 93.65, 93.7, 93.5, 93.32, 93.67, 93.43, 93.62, 93.45, 93.58, 93.72, 93.57, 93.58, 93.7, 93.57, 93.48, 93.1, 93.47, 93.52, 93.67, 93.68, 93.73, 93.62, 93.13, 93.2]
main_fed = [68.48, 78.03, 78.62, 80.47, 81.5, 82.0, 83.93, 84.25, 84.8, 85.13, 85.82, 85.78, 86.2, 86.37, 86.8, 86.98, 86.88, 87.3, 87.35, 87.55, 87.53, 87.97, 88.2, 87.85, 88.08, 88.65, 88.23, 88.5, 88.5, 88.95, 88.6, 88.97, 89.12, 89.32, 89.1, 88.78, 89.38, 88.97, 89.2, 89.6, 90.17, 89.55, 89.75, 90.18, 89.8, 90.17, 90.28, 89.88, 90.2, 90.32]
main_nn = [18.35, 94.75, 95.02, 95.13, 95.63, 95.45, 95.47, 95.62, 95.73, 95.47, 95.53, 95.5, 95.85, 95.6, 95.7, 95.88, 95.9, 95.48, 95.37, 95.73, 95.88, 95.68, 95.45, 95.57, 95.65, 95.42, 95.57, 95.55, 95.53, 95.7, 95.85, 95.43, 95.48, 95.72, 95.92, 95.85, 95.92, 95.62, 95.75, 95.67, 95.55, 95.53, 95.62, 95.67, 95.62, 95.47, 95.53, 95.68, 95.5, 95.38]

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
plt.ylim(80, 98)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
