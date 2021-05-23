# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
network_5_node = [51.33, 56.67, 58.8, 64.0, 65.07, 62.0, 64.53, 66.13, 66.53, 66.0, 66.13, 67.6, 66.4, 66.93, 66.8, 67.47, 67.33, 66.93, 66.4, 67.33, 67.33, 66.53, 66.93, 67.07, 66.4, 68.8, 67.2, 67.73, 66.53, 66.27, 67.2, 67.47, 67.2, 67.47, 66.67, 67.6, 67.73, 68.13, 67.47, 66.53, 67.07, 68.4, 68.0, 68.27, 68.53, 68.4, 67.6, 67.6, 67.87, 68.13]
network_10_node = [54.87, 62.6, 66.07, 69.2, 73.53, 72.07, 72.4, 73.67, 73.33, 73.0, 73.8, 74.6, 74.53, 74.0, 74.0, 74.53, 74.13, 74.8, 74.53, 74.53, 74.8, 74.87, 74.87, 75.0, 74.33, 75.13, 74.4, 74.47, 74.8, 74.53, 75.2, 74.53, 75.2, 75.0, 75.87, 75.47, 75.33, 75.93, 76.13, 76.0, 75.93, 75.87, 75.67, 74.67, 74.67, 75.53, 75.87, 76.6, 76.27, 75.73]
network_20_node = [30.67, 38.33, 37.67, 38.43, 42.53, 44.4, 46.0, 42.97, 46.83, 49.47, 46.83, 47.73, 48.93, 50.03, 49.5, 47.93, 50.33, 51.73, 51.6, 49.77, 52.13, 51.8, 50.53, 50.27, 52.1, 52.53, 52.1, 51.03, 52.0, 52.97, 52.37, 51.97, 52.17, 52.83, 52.27, 51.2, 51.3, 53.17, 51.17, 52.5, 51.8, 52.77, 52.83, 50.87, 52.8, 52.43, 52.93, 51.37, 51.87, 53.97]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

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
