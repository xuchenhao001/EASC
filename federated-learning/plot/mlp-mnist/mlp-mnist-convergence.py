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
network_5_node = [95.73, 96.8, 96.93, 97.33, 97.47, 97.33, 97.33, 97.33, 97.2, 97.2, 97.2, 97.33, 97.2, 97.33, 97.33, 97.33, 97.33, 97.47, 97.47, 97.47, 97.73, 97.47, 97.47, 97.2, 97.33, 97.73, 97.47, 97.6, 97.47, 97.73, 97.6, 97.47, 97.33, 97.6, 97.6, 97.47, 97.47, 97.33, 97.47, 97.47, 97.2, 97.33, 97.33, 97.47, 97.6, 97.47, 97.47, 97.47, 97.33, 97.2]
network_10_node = [95.87, 96.8, 97.07, 97.33, 97.4, 97.4, 97.33, 97.07, 97.47, 97.2, 97.2, 97.2, 97.33, 97.33, 97.4, 97.4, 97.4, 97.27, 97.27, 97.33, 97.4, 97.33, 97.4, 97.4, 97.47, 97.27, 97.4, 97.4, 97.33, 97.47, 97.53, 97.4, 97.67, 97.47, 97.4, 97.67, 97.47, 97.6, 97.67, 97.53, 97.53, 97.47, 97.53, 97.47, 97.67, 97.53, 97.67, 97.47, 97.6, 97.73]
network_20_node = [62.3, 63.4, 73.4, 72.17, 77.8, 75.37, 81.07, 83.63, 84.97, 83.5, 87.8, 86.93, 86.3, 86.63, 87.7, 89.9, 89.13, 87.83, 88.13, 88.83, 90.23, 90.13, 90.0, 89.5, 92.3, 90.57, 91.93, 89.7, 90.87, 89.8, 89.23, 90.4, 89.53, 90.57, 92.17, 90.1, 91.37, 90.6, 89.37, 90.93, 92.1, 91.73, 90.5, 92.83, 93.23, 92.63, 92.73, 91.23, 92.87, 93.1]

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
plt.ylim(80)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
