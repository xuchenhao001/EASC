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
network_5_node = [15.60, 31.87, 32.40, 34.00, 35.73, 35.87, 20.00, 37.47, 20.53, 22.93, 36.93, 36.13, 19.07, 36.13, 21.47, 24.27, 24.27, 35.47, 23.60, 23.07, 27.87, 35.87, 37.47, 36.40, 22.27, 36.40, 37.33, 24.27, 26.80, 36.93, 37.87, 36.67, 37.20, 39.87, 39.87, 22.80, 37.47, 38.27, 19.87, 37.20, 24.40, 31.47, 24.27, 38.40, 38.40, 25.60, 29.73, 37.60, 38.53, 39.33]
network_10_node = [27.47, 18.47, 19.80, 34.60, 31.80, 33.00, 32.13, 31.67, 38.33, 32.60, 34.40, 36.33, 36.33, 39.60, 37.33, 35.93, 40.87, 41.33, 37.20, 31.60, 38.20, 28.53, 35.53, 40.20, 40.53, 40.20, 33.20, 39.13, 39.80, 25.60, 27.00, 41.93, 38.40, 37.33, 39.93, 41.20, 40.60, 41.00, 27.93, 39.60, 42.07, 27.60, 34.07, 42.27, 41.13, 41.87, 41.53, 31.67, 35.33, 43.47]
network_20_node = [18.40, 12.40, 17.97, 21.57, 22.33, 23.23, 26.63, 22.50, 26.57, 21.73, 28.40, 25.63, 28.77, 25.90, 33.90, 25.93, 30.73, 33.03, 38.63, 35.20, 35.53, 41.07, 33.00, 32.27, 35.90, 25.43, 28.97, 34.53, 35.83, 31.20, 31.57, 35.33, 39.27, 38.60, 41.47, 37.13, 35.77, 33.30, 33.60, 38.17, 39.20, 39.37, 41.03, 37.20, 35.23, 41.37, 31.10, 41.70, 38.67, 33.97]

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
# plt.ylim(40)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
