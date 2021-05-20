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
network_5_node = [94.93, 95.47, 95.33, 95.73, 95.73, 96.27, 95.6, 95.73, 96.13, 95.73, 95.47, 95.73, 95.47, 95.6, 95.87, 95.6, 95.73, 95.87, 95.73, 95.33, 95.6, 95.6, 95.87, 95.87, 95.87, 95.73, 95.33, 95.6, 95.6, 95.6, 95.73, 95.47, 95.6, 95.87, 96.13, 95.47, 95.6, 95.47, 95.47, 95.87, 95.6, 95.87, 95.47, 95.6, 95.6, 95.33, 95.47, 95.47, 95.73, 95.6]
network_10_node = [94.53, 95.33, 95.87, 95.53, 95.6, 95.6, 95.33, 95.87, 95.87, 95.6, 95.87, 95.6, 95.73, 95.33, 95.6, 95.53, 95.93, 96.07, 95.93, 95.8, 95.87, 95.8, 95.73, 95.73, 95.6, 95.67, 96.0, 96.27, 95.8, 96.07, 96.0, 96.0, 96.0, 95.8, 95.8, 95.93, 96.13, 95.73, 96.07, 95.93, 96.0, 95.87, 96.0, 95.87, 96.2, 96.27, 96.07, 96.07, 96.33, 96.47]
network_20_node = [58.5, 68.57, 69.7, 73.73, 77.13, 78.27, 81.57, 82.8, 83.37, 86.33, 86.97, 86.6, 86.77, 85.87, 87.73, 89.0, 89.73, 89.3, 88.9, 89.97, 89.53, 88.37, 91.5, 89.27, 88.93, 89.9, 91.8, 90.13, 90.23, 90.97, 91.53, 90.2, 91.3, 89.97, 91.5, 91.47, 92.13, 90.6, 91.63, 91.53, 91.3, 91.27, 92.33, 91.37, 91.57, 92.07, 91.7, 92.27, 92.13, 91.57]

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
plt.ylim(80)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
