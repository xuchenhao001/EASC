# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import cycler

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
network_5_node = [83.93, 86.4, 87.27, 87.2, 87.67, 88.2, 88.53, 88.93, 89.0, 88.8, 88.53, 89.47, 89.73, 89.2, 89.53, 89.53, 89.73, 89.93, 89.67, 89.93, 90.2, 89.87, 90.27, 88.67, 90.13, 90.8, 90.4, 89.2, 90.13, 90.13, 90.27, 90.33, 90.0, 90.47, 89.93, 89.67, 90.33, 90.2, 89.93, 89.33, 90.27, 90.4, 90.53, 90.53, 90.6, 90.13, 89.8, 91.0, 89.87, 90.8]
network_10_node = [84.53, 86.03, 87.4, 88.4, 87.93, 88.77, 88.67, 88.33, 88.63, 89.4, 89.5, 89.37, 89.47, 89.5, 88.73, 89.47, 89.37, 90.07, 89.57, 90.23, 89.83, 90.5, 90.3, 90.47, 90.37, 90.17, 90.17, 90.23, 90.03, 90.67, 90.3, 90.73, 90.6, 90.27, 90.47, 90.9, 90.9, 90.67, 90.4, 90.43, 90.5, 90.43, 90.43, 90.93, 90.73, 91.23, 91.73, 91.13, 91.07, 90.83]
network_20_node = [56.48, 59.35, 61.48, 59.23, 62.98, 63.18, 62.9, 65.9, 65.22, 66.97, 67.67, 68.62, 68.62, 69.1, 70.7, 69.82, 68.28, 72.58, 69.3, 71.03, 71.73, 72.22, 73.12, 73.77, 72.75, 74.08, 74.7, 76.77, 75.2, 76.03, 76.0, 76.2, 74.85, 77.07, 76.32, 77.27, 76.08, 76.55, 76.55, 77.38, 77.4, 78.35, 76.43, 79.18, 76.62, 78.78, 75.32, 77.22, 78.27, 77.3]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, network_5_node, label="SCEI with 5 nodes")
axes.plot(x, network_10_node, label="SCEI with 10 nodes")
axes.plot(x, network_20_node, label="SCEI with 20 nodes")

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
# plt.ylim(40)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
