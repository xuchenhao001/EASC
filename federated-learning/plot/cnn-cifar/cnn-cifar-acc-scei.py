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
fed_server = [54.87, 62.6, 66.07, 69.2, 73.53, 72.07, 72.4, 73.67, 73.33, 73.0, 73.8, 74.6, 74.53, 74.0, 74.0, 74.53, 74.13, 74.8, 74.53, 74.53, 74.8, 74.87, 74.87, 75.0, 74.33, 75.13, 74.4, 74.47, 74.8, 74.53, 75.2, 74.53, 75.2, 75.0, 75.87, 75.47, 75.33, 75.93, 76.13, 76.0, 75.93, 75.87, 75.67, 74.67, 74.67, 75.53, 75.87, 76.6, 76.27, 75.73]
fed_server_alpha_025 = [41.8, 48.8, 52.93, 57.8, 60.47, 63.13, 64.13, 64.73, 64.8, 63.73, 64.07, 64.2, 64.13, 64.73, 64.47, 65.13, 65.2, 64.8, 63.73, 64.47, 63.13, 63.67, 62.87, 63.4, 63.27, 63.13, 63.13, 62.87, 62.67, 63.0, 62.13, 62.0, 61.2, 61.53, 62.27, 62.07, 61.33, 61.47, 61.47, 61.13, 61.47, 61.53, 61.4, 61.87, 61.2, 61.73, 61.4, 60.47, 60.73, 61.13]
fed_server_alpha_050 = [45.4, 52.67, 55.73, 59.93, 61.6, 62.93, 62.0, 65.07, 65.2, 66.53, 65.6, 67.0, 67.53, 67.27, 65.13, 66.07, 67.07, 66.87, 66.47, 66.8, 66.93, 66.8, 66.73, 66.53, 66.8, 67.07, 66.27, 67.0, 66.4, 65.53, 67.2, 66.13, 67.07, 66.33, 66.87, 65.53, 65.47, 67.4, 66.47, 66.0, 65.87, 65.73, 66.0, 65.4, 65.13, 65.6, 64.73, 65.13, 64.87, 65.27]
fed_server_alpha_075 = [42.73, 52.6, 57.0, 62.2, 64.4, 65.53, 68.0, 68.4, 68.13, 68.27, 67.87, 67.73, 70.2, 68.93, 69.47, 69.8, 71.2, 70.53, 70.67, 70.2, 69.93, 70.33, 70.4, 70.27, 71.47, 70.93, 70.73, 70.8, 70.6, 68.93, 70.4, 70.33, 70.4, 70.33, 70.73, 69.07, 70.47, 69.73, 70.27, 70.93, 70.4, 69.87, 69.87, 70.33, 69.93, 70.67, 69.73, 70.13, 69.73, 71.33]
main_fed = [23.33, 28.93, 32.53, 32.87, 34.87, 36.8, 37.6, 37.67, 39.07, 39.33, 40.0, 40.27, 40.27, 40.67, 41.8, 41.93, 41.67, 43.0, 42.93, 42.53, 42.6, 43.47, 43.13, 43.73, 43.6, 43.73, 44.13, 44.6, 44.2, 44.27, 43.67, 44.4, 44.0, 43.33, 42.47, 43.6, 43.47, 43.27, 42.67, 43.33, 43.8, 43.13, 42.8, 42.8, 42.53, 41.87, 43.13, 43.8, 43.8, 43.27]
main_nn = [13.27, 50.53, 59.07, 63.13, 64.53, 67.53, 68.2, 67.8, 69.73, 69.87, 69.93, 69.87, 69.67, 69.27, 69.53, 69.2, 69.47, 69.13, 69.4, 69.47, 69.2, 69.6, 69.73, 69.53, 69.4, 69.4, 69.6, 69.67, 69.53, 69.67, 69.6, 69.6, 69.67, 69.67, 69.6, 69.6, 69.67, 69.6, 69.67, 69.6, 69.6, 69.67, 69.67, 69.67, 69.6, 69.67, 69.67, 69.67, 69.67, 69.73]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
# markers = ["None", "1", "+", "x", "|", "*", "4", "d", "v", "."]
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
plt.ylim(40)
plt.legend(prop=legendFont)
plt.grid()
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    plt.savefig(sys.argv[2])
else:
    plt.show()

