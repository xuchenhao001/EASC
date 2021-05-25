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
network_5_node = [93.47, 95.2, 96.8, 98.0, 97.2, 97.47, 97.87, 98.13, 98.13, 98.13, 98.4, 98.53, 98.13, 97.87, 98.0, 98.0, 98.0, 98.0, 98.27, 98.0, 98.13, 98.27, 98.13, 97.87, 98.27, 98.27, 98.4, 98.13, 98.27, 98.27, 98.0, 98.4, 98.13, 98.27, 98.27, 98.13, 98.53, 98.53, 98.93, 98.0, 98.53, 98.93, 98.8, 98.67, 98.53, 98.67, 98.4, 98.67, 98.27, 98.4]
network_10_node = [96.87, 98.0, 98.2, 97.67, 97.87, 98.27, 98.13, 98.2, 98.13, 98.0, 98.4, 98.33, 98.4, 98.4, 98.4, 98.4, 98.6, 98.87, 98.67, 98.6, 98.47, 98.93, 98.93, 98.8, 98.67, 98.87, 98.93, 98.93, 98.93, 99.13, 98.8, 98.93, 98.8, 99.0, 98.73, 98.8, 98.8, 98.8, 98.53, 98.73, 99.07, 98.8, 99.13, 98.8, 99.0, 99.0, 98.8, 98.6, 99.2, 98.8]
network_20_node = [64.07, 65.53, 70.5, 75.77, 83.27, 84.33, 87.0, 84.47, 86.93, 88.8, 90.67, 90.37, 88.17, 90.77, 92.73, 92.1, 91.1, 91.73, 94.17, 93.93, 93.43, 92.8, 93.1, 94.57, 93.93, 94.27, 94.93, 94.8, 94.27, 95.1, 94.93, 95.63, 95.07, 95.23, 95.33, 96.03, 95.07, 95.43, 95.43, 96.03, 96.6, 96.07, 96.7, 96.0, 96.4, 95.23, 95.87, 95.8, 96.0, 96.73]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, network_5_node, label="SCEI with 5 nodes")
axes.plot(x, network_10_node, label="SCEI with 10 nodes")
axes.plot(x, network_20_node, label="SCEI with 20 nodes")
# axes.plot(x, network_50_peer, label="SCEI with 50 nodes")

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(85)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
