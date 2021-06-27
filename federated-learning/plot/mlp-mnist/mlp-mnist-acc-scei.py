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
fed_server_alpha_025 = [93.13, 93.33, 92.67, 92.53, 92.93, 92.53, 93.2, 93.33, 93.4, 93.47, 93.4, 93.73, 93.73, 93.8, 93.67, 93.8, 93.8, 93.93, 93.73, 93.8, 93.73, 93.6, 93.6, 93.93, 93.73, 93.87, 93.93, 93.73, 94.07, 94.07, 93.87, 93.8, 94.0, 94.13, 94.2, 94.0, 94.2, 94.2, 94.07, 94.47, 94.27, 94.4, 94.4, 94.2, 94.2, 94.33, 94.4, 94.2, 94.13, 94.33]
fed_server_alpha_050 = [94.33, 94.6, 95.0, 95.33, 95.33, 95.47, 95.87, 95.53, 95.73, 96.0, 95.87, 96.0, 95.87, 96.0, 95.87, 95.87, 95.87, 95.73, 95.93, 95.93, 95.87, 96.07, 95.93, 95.8, 95.8, 95.93, 95.93, 96.07, 95.93, 96.13, 96.0, 96.07, 96.07, 96.27, 95.93, 96.0, 96.27, 95.87, 96.0, 96.2, 96.2, 96.27, 96.2, 96.07, 96.0, 96.2, 96.07, 96.33, 96.27, 96.27]
fed_server_alpha_075 = [95.6, 95.67, 96.27, 96.27, 96.53, 96.93, 96.87, 97.0, 96.87, 96.93, 97.13, 97.0, 97.0, 96.93, 96.93, 97.0, 97.2, 97.07, 97.2, 96.93, 97.13, 97.0, 97.13, 97.0, 97.0, 96.73, 96.8, 97.13, 96.73, 96.73, 97.07, 97.2, 97.0, 97.13, 96.67, 96.93, 96.93, 96.8, 96.8, 96.67, 96.93, 96.8, 96.53, 96.8, 96.87, 96.8, 96.93, 96.8, 96.87, 96.53]
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
