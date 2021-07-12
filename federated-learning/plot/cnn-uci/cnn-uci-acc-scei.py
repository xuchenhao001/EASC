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
fed_server_alpha_025 = [87.75, 89.45, 90.33, 90.66, 90.88, 90.76, 91.11, 91.01, 91.19, 91.39, 91.17, 91.46, 91.66, 91.33, 92.11, 91.75, 91.7, 92.31, 92.66, 92.62, 92.65, 92.61, 92.45, 92.59, 92.59, 92.66, 92.71, 92.64, 92.78, 92.34, 92.75, 92.59, 92.51, 92.62, 92.83, 92.54, 92.31, 92.17, 92.47, 92.4, 92.22, 92.44, 92.56, 92.45, 92.01, 92.44, 92.46, 92.45, 92.75, 92.51]
fed_server_alpha_050 = [89.79, 90.3, 90.8, 91.76, 91.47, 92.0, 92.53, 92.4, 92.59, 92.9, 93.0, 92.8, 93.01, 92.92, 93.29, 93.04, 92.81, 93.1, 93.05, 92.8, 93.09, 92.39, 92.79, 92.85, 92.89, 92.55, 93.01, 92.74, 93.28, 92.71, 93.44, 93.35, 93.19, 93.33, 92.91, 93.14, 93.3, 93.11, 93.35, 92.94, 93.24, 93.22, 93.0, 93.25, 92.76, 93.05, 92.84, 92.94, 93.2, 92.91]
fed_server_alpha_075 = [92.47, 92.65, 92.96, 93.0, 93.4, 93.72, 93.62, 93.69, 94.12, 94.08, 94.04, 94.21, 94.29, 94.54, 94.46, 94.22, 94.46, 94.24, 94.54, 94.29, 94.62, 94.3, 94.94, 94.38, 94.69, 94.36, 94.72, 94.76, 94.67, 94.69, 94.72, 94.72, 94.97, 94.38, 94.55, 94.72, 94.91, 94.33, 94.75, 94.55, 94.66, 94.67, 94.26, 93.84, 94.53, 94.6, 94.9, 94.38, 94.38, 94.6]
main_fed = [85.01, 87.5, 88.84, 89.81, 89.89, 90.28, 90.88, 90.71, 90.71, 91.34, 91.1, 91.46, 91.81, 91.85, 91.84, 91.55, 91.88, 91.97, 92.35, 92.25, 92.44, 92.06, 92.14, 92.44, 92.15, 92.29, 92.22, 91.89, 92.14, 91.89, 92.1, 91.8, 92.03, 92.22, 91.84, 91.67, 92.17, 91.64, 91.71, 91.97, 91.69, 91.88, 91.56, 91.54, 91.81, 91.91, 91.46, 91.66, 91.49, 91.66]
main_nn = [22.75, 92.12, 92.53, 92.45, 92.67, 92.85, 93.09, 92.89, 93.06, 93.64, 93.45, 93.12, 93.4, 93.45, 93.42, 93.19, 93.64, 93.34, 93.42, 93.58, 93.09, 93.39, 93.44, 93.55, 93.61, 93.11, 93.1, 93.3, 93.28, 93.53, 93.49, 93.4, 93.04, 93.36, 93.22, 93.38, 93.42, 93.54, 93.09, 93.28, 93.28, 93.38, 93.51, 93.36, 93.39, 93.39, 93.3, 93.38, 93.26, 93.58]

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
plt.ylim(80, 98)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
