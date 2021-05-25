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
network_5_node = [45.6, 52.27, 55.07, 60.4, 61.73, 62.67, 64.93, 67.73, 66.67, 65.07, 65.47, 65.6, 68.4, 68.27, 67.6, 68.13, 68.27, 67.47, 66.93, 68.4, 68.53, 67.73, 68.27, 68.4, 68.8, 69.2, 68.53, 68.13, 68.13, 68.13, 68.8, 68.27, 68.53, 68.13, 68.0, 67.73, 68.67, 67.87, 67.6, 68.0, 68.27, 68.27, 67.73, 67.87, 68.0, 68.4, 67.73, 67.6, 67.07, 66.93]
network_10_node = [54.87, 62.6, 66.07, 69.2, 73.53, 72.07, 72.4, 73.67, 73.33, 73.0, 73.8, 74.6, 74.53, 74.0, 74.0, 74.53, 74.13, 74.8, 74.53, 74.53, 74.8, 74.87, 74.87, 75.0, 74.33, 75.13, 74.4, 74.47, 74.8, 74.53, 75.2, 74.53, 75.2, 75.0, 75.87, 75.47, 75.33, 75.93, 76.13, 76.0, 75.93, 75.87, 75.67, 74.67, 74.67, 75.53, 75.87, 76.6, 76.27, 75.73]
network_20_node = [30.93, 34.47, 35.67, 37.9, 38.23, 40.8, 44.1, 42.4, 45.83, 44.97, 45.17, 45.8, 48.0, 47.27, 48.27, 46.83, 49.4, 48.7, 48.03, 48.93, 48.1, 48.87, 48.13, 47.5, 49.07, 49.53, 49.4, 47.97, 47.47, 49.3, 47.5, 48.23, 48.37, 48.77, 49.13, 48.23, 47.73, 49.37, 48.83, 48.47, 49.8, 48.97, 49.0, 49.27, 48.93, 49.33, 51.3, 50.0, 49.13, 50.93]

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
