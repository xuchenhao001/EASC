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

fed_server = [93.7, 94.6, 95.15, 95.3, 95.3, 95.35, 95.35, 95.65, 95.75, 95.7, 95.65, 95.75, 95.6, 95.75, 95.95, 95.8, 95.85, 95.9, 95.85, 95.9, 95.75, 95.95, 95.8, 95.65, 95.85, 95.9, 95.95, 96.05, 95.95, 96.05, 96.1, 96.4, 96.1, 96.0, 95.8, 96.1, 95.9, 95.95, 95.95, 95.9, 95.85, 96.05, 96.05, 96.1, 96.0, 96.0, 96.15, 96.0, 96.15, 95.95]
fed_server_alpha_025 = [82.15, 87.45, 88.25, 89.6, 90.2, 91.05, 91.75, 92.0, 92.5, 92.9, 93.1, 93.15, 93.45, 93.5, 93.55, 93.35, 93.8, 93.8, 93.7, 93.75, 93.9, 93.95, 93.9, 94.0, 93.9, 94.1, 94.2, 94.0, 94.4, 94.45, 94.4, 94.25, 94.45, 94.5, 94.6, 94.55, 94.7, 94.6, 94.5, 94.65, 94.75, 94.75, 94.6, 94.75, 94.8, 94.75, 94.8, 94.9, 94.9, 94.95]
fed_server_alpha_050 = [90.95, 93.05, 93.75, 94.6, 94.6, 94.7, 95.0, 95.0, 95.2, 95.3, 95.2, 95.6, 95.4, 95.3, 95.5, 95.6, 95.3, 95.5, 95.5, 95.7, 95.6, 95.45, 95.7, 95.4, 95.5, 95.4, 95.6, 95.85, 95.65, 95.5, 95.6, 95.6, 95.7, 95.45, 95.55, 95.55, 95.45, 95.65, 95.95, 95.75, 95.8, 95.55, 95.7, 95.75, 95.6, 95.8, 95.9, 95.75, 95.95, 95.9]
fed_server_alpha_075 = [92.75, 94.2, 94.25, 94.25, 94.4, 94.4, 94.85, 94.8, 94.75, 94.95, 94.75, 94.65, 94.95, 94.8, 95.05, 94.85, 95.25, 95.05, 95.3, 95.25, 95.45, 95.55, 95.75, 95.55, 95.35, 95.4, 95.6, 95.7, 95.45, 95.65, 95.8, 95.8, 95.7, 95.55, 95.7, 95.8, 95.8, 95.75, 95.85, 95.85, 95.95, 95.7, 95.9, 95.9, 96.0, 95.75, 95.9, 95.8, 95.9, 95.55]
main_fed = [57.65, 70.2, 74.25, 77.6, 80.4, 82.7, 83.55, 85.1, 85.25, 86.15, 86.8, 87.0, 87.0, 87.5, 87.6, 87.8, 87.8, 88.2, 88.4, 88.75, 88.95, 89.0, 89.1, 89.2, 89.3, 89.4, 89.6, 89.9, 89.8, 89.75, 89.9, 90.15, 90.3, 90.15, 90.25, 90.45, 90.35, 90.25, 90.3, 90.6, 90.6, 90.6, 90.8, 90.75, 90.7, 90.75, 90.75, 90.75, 90.8, 90.9]
main_nn = [9.8, 91.2, 93.1, 93.75, 93.65, 93.8, 93.85, 94.1, 94.2, 94.05, 93.95, 93.75, 94.2, 94.1, 94.0, 94.2, 94.05, 94.25, 94.1, 94.35, 94.2, 94.3, 94.2, 94.45, 94.3, 94.5, 94.45, 94.15, 94.55, 94.5, 94.65, 94.35, 94.2, 94.45, 94.45, 94.4, 94.45, 94.4, 94.35, 94.35, 94.35, 94.45, 94.15, 94.45, 94.2, 94.0, 94.2, 94.35, 94.4, 94.45]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}
titleFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csTitleFont = {'fontproperties': titleFont}
plt.title("No Skew (α=0.5~0.8)", **csTitleFont)

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, fed_server, label="negotiated α (0.5-0.8)", linewidth=3)
axes.plot(x, main_fed, label="α=0.0 (i.e. FedAvg)",  alpha=0.5)
axes.plot(x, fed_server_alpha_025, label="α=0.25",  alpha=0.5)
axes.plot(x, fed_server_alpha_050, label="α=0.5",  alpha=0.5)
axes.plot(x, fed_server_alpha_075, label="α=0.75",  alpha=0.5)
axes.plot(x, main_nn, label="α=1.0 (i.e. Local Training)",  alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(75, 99)
plt.legend(loc="lower right", prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
