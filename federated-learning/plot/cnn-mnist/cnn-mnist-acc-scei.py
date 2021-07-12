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

fed_server = [94.85, 96.0, 96.6, 97.3, 97.3, 97.3, 97.65, 97.5, 97.75, 97.95, 97.95, 97.95, 97.85, 98.15, 97.95, 98.3, 98.3, 98.3, 98.25, 98.35, 98.25, 98.45, 98.5, 98.6, 98.65, 98.35, 98.25, 98.55, 98.8, 98.75, 98.65, 98.55, 98.55, 98.6, 98.7, 98.65, 98.6, 98.7, 98.65, 98.95, 98.65, 98.75, 98.65, 98.85, 98.85, 98.75, 98.8, 98.8, 98.75, 98.75]
fed_server_alpha_025 = [80.25, 85.65, 88.75, 89.95, 92.85, 93.65, 93.55, 94.15, 95.15, 95.3, 95.1, 95.35, 95.75, 95.95, 96.25, 96.35, 96.25, 96.75, 96.55, 96.8, 97.3, 96.85, 97.05, 97.15, 97.15, 97.2, 97.35, 97.2, 97.6, 97.25, 97.45, 97.45, 97.5, 97.35, 97.45, 97.75, 97.85, 97.65, 97.6, 97.85, 97.75, 97.95, 97.95, 98.2, 97.8, 98.15, 98.05, 98.0, 98.05, 98.0]
fed_server_alpha_050 = [94.2, 94.25, 95.9, 96.2, 96.75, 96.45, 96.95, 97.05, 97.45, 97.25, 97.35, 97.65, 97.7, 98.0, 97.8, 97.85, 97.7, 97.65, 97.85, 98.3, 98.15, 98.6, 98.45, 98.4, 98.65, 98.35, 98.3, 98.2, 98.5, 98.55, 98.35, 98.55, 98.6, 98.7, 98.55, 98.4, 98.45, 98.45, 98.65, 98.65, 98.6, 98.45, 98.75, 98.6, 98.55, 98.7, 98.5, 98.8, 98.6, 98.75]
fed_server_alpha_075 = [95.3, 96.4, 96.85, 97.2, 97.7, 97.75, 97.75, 98.05, 97.95, 98.1, 98.1, 98.25, 98.0, 98.4, 98.45, 98.3, 98.3, 98.25, 98.4, 98.4, 98.35, 98.3, 98.5, 98.65, 98.4, 98.6, 98.6, 98.45, 98.65, 98.7, 98.35, 98.65, 98.6, 98.75, 98.85, 98.85, 98.6, 98.7, 98.85, 98.75, 98.7, 98.8, 98.55, 98.95, 98.7, 98.75, 98.7, 98.85, 98.75, 98.75]
main_fed = [64.7, 78.8, 84.0, 87.9, 90.25, 90.85, 91.6, 92.35, 92.9, 93.2, 93.4, 93.75, 94.0, 94.0, 94.25, 94.55, 94.55, 94.55, 94.85, 94.85, 95.2, 95.4, 95.4, 95.35, 95.2, 95.45, 95.55, 95.5, 95.65, 95.85, 96.15, 96.1, 95.85, 96.0, 96.0, 96.25, 96.05, 96.3, 96.3, 96.1, 96.45, 96.9, 96.7, 96.55, 96.6, 96.5, 96.8, 96.85, 96.8, 96.75]
main_nn = [3.75, 94.45, 96.65, 96.95, 97.4, 97.85, 97.75, 97.95, 97.75, 97.75, 97.75, 97.75, 97.85, 98.05, 98.0, 97.8, 98.05, 98.05, 98.45, 98.0, 98.2, 98.05, 97.9, 98.0, 97.95, 97.9, 98.0, 98.2, 98.15, 97.8, 98.1, 98.0, 98.1, 98.35, 98.3, 98.1, 98.0, 98.25, 98.05, 98.15, 98.2, 98.05, 98.1, 98.4, 98.3, 98.15, 98.2, 98.3, 98.4, 98.15]

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
plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
