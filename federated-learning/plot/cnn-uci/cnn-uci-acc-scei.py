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
fed_server_alpha_025 = [86.57, 89.3, 91.88, 92.57, 92.72, 92.25, 92.78, 92.75, 92.92, 93.02, 92.83, 93.37, 93.18, 93.2, 93.03, 93.32, 93.23, 93.47, 93.28, 93.23, 93.4, 93.5, 93.22, 93.38, 93.53, 93.4, 93.43, 93.32, 93.5, 93.53, 93.67, 93.65, 93.92, 93.95, 93.53, 93.77, 93.45, 93.75, 93.85, 93.72, 94.3, 94.1, 93.87, 94.15, 94.1, 94.22, 94.08, 93.9, 94.27, 93.95]
fed_server_alpha_050 = [93.37, 94.12, 94.47, 94.55, 95.12, 95.22, 95.05, 95.13, 95.2, 95.28, 95.25, 94.98, 95.2, 95.5, 95.4, 95.28, 95.28, 95.5, 95.2, 95.42, 95.27, 95.43, 95.52, 95.37, 95.3, 95.63, 95.28, 95.48, 95.53, 95.17, 95.23, 95.53, 95.38, 95.53, 95.12, 95.45, 95.38, 95.45, 95.37, 95.6, 95.67, 95.52, 95.35, 95.6, 95.45, 95.5, 95.48, 95.63, 95.52, 95.4]
fed_server_alpha_075 = [93.77, 94.67, 94.53, 94.45, 94.33, 94.73, 94.97, 94.68, 94.8, 94.77, 94.8, 94.85, 95.08, 94.82, 95.2, 94.77, 94.85, 95.15, 95.3, 94.57, 95.0, 94.87, 94.88, 94.92, 94.83, 95.25, 95.15, 94.75, 94.93, 94.88, 94.7, 95.08, 95.02, 94.98, 95.08, 94.95, 95.12, 94.4, 94.98, 94.88, 94.8, 94.95, 94.8, 94.97, 94.98, 94.95, 94.68, 94.95, 94.67, 94.88]
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
