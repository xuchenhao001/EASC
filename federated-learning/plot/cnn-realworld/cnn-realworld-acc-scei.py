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

fed_server = [84.53, 86.03, 87.4, 88.4, 87.93, 88.77, 88.67, 88.33, 88.63, 89.4, 89.5, 89.37, 89.47, 89.5, 88.73, 89.47, 89.37, 90.07, 89.57, 90.23, 89.83, 90.5, 90.3, 90.47, 90.37, 90.17, 90.17, 90.23, 90.03, 90.67, 90.3, 90.73, 90.6, 90.27, 90.47, 90.9, 90.9, 90.67, 90.4, 90.43, 90.5, 90.43, 90.43, 90.93, 90.73, 91.23, 91.73, 91.13, 91.07, 90.83]
fed_server_alpha_025 = [66.1, 67.27, 72.1, 74.83, 74.1, 75.63, 76.47, 77.5, 77.47, 78.87, 80.07, 80.63, 79.67, 80.93, 80.7, 81.43, 80.77, 79.93, 81.83, 81.83, 81.7, 82.0, 81.5, 82.8, 81.9, 82.17, 82.6, 81.9, 82.3, 82.13, 82.83, 82.73, 83.1, 82.7, 83.0, 83.8, 83.6, 83.47, 82.5, 83.3, 83.57, 83.23, 83.73, 83.5, 83.43, 83.4, 83.37, 84.07, 83.53, 83.53]
fed_server_alpha_050 = [81.7, 82.27, 84.6, 85.03, 85.1, 86.37, 86.77, 87.2, 87.47, 87.4, 87.93, 88.9, 88.73, 88.6, 88.63, 89.07, 88.63, 89.1, 88.83, 89.17, 89.27, 89.27, 89.7, 88.97, 89.37, 90.43, 89.93, 89.8, 89.33, 90.27, 89.97, 89.87, 89.97, 90.4, 90.2, 89.5, 89.5, 91.0, 90.43, 90.17, 90.23, 90.5, 90.6, 90.5, 90.67, 91.27, 90.77, 90.97, 90.93, 90.67]
fed_server_alpha_075 = [81.3, 81.93, 83.7, 83.63, 84.23, 85.2, 83.97, 84.87, 85.87, 84.57, 85.37, 85.87, 85.97, 85.67, 85.67, 85.63, 86.07, 85.67, 85.6, 87.03, 86.17, 85.53, 86.57, 86.63, 86.6, 86.1, 87.5, 86.37, 86.47, 86.6, 86.67, 87.03, 86.67, 87.17, 87.07, 86.8, 87.63, 87.57, 87.67, 88.03, 87.0, 87.4, 87.67, 87.4, 87.87, 87.4, 87.43, 88.43, 87.57, 89.0]
main_fed = [40.5, 51.63, 55.97, 60.23, 62.83, 64.37, 66.13, 66.93, 68.3, 69.73, 70.87, 70.2, 72.17, 70.93, 71.6, 72.63, 72.5, 73.67, 73.47, 73.43, 74.2, 74.17, 74.47, 74.8, 74.73, 75.3, 74.53, 74.37, 75.17, 75.07, 75.37, 75.43, 75.0, 74.47, 75.07, 75.57, 76.03, 74.27, 75.47, 75.43, 76.3, 74.87, 75.93, 76.0, 75.43, 75.97, 75.63, 76.27, 76.43, 76.27]
main_nn = [10.27, 81.23, 83.5, 84.6, 85.6, 85.37, 86.03, 87.13, 86.53, 87.07, 87.13, 87.57, 87.4, 87.77, 87.77, 87.77, 87.7, 87.63, 87.6, 87.27, 88.33, 87.63, 87.67, 88.33, 87.43, 87.7, 88.23, 88.13, 87.8, 87.8, 87.83, 88.0, 87.7, 88.5, 88.13, 88.53, 87.93, 88.77, 88.13, 88.73, 87.97, 88.3, 88.2, 87.93, 88.43, 88.23, 87.93, 87.9, 87.9, 87.93]

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
plt.ylim(50)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()
