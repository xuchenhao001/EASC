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
network_5_node = [94.4, 95.2, 94.83, 94.83, 94.87, 95.77, 95.2, 95.07, 94.93, 95.5, 95.13, 95.2, 95.23, 95.4, 95.1, 95.17, 94.8, 95.1, 95.47, 95.33, 95.37, 95.53, 95.3, 95.37, 95.43, 95.37, 95.2, 95.37, 95.4, 95.5, 94.67, 95.07, 95.3, 95.2, 95.0, 94.93, 95.1, 95.07, 95.07, 95.17, 95.3, 95.37, 95.23, 95.3, 94.8, 94.97, 94.8, 94.9, 94.97, 94.93]
network_10_node = [95.25, 94.8, 96.03, 96.03, 95.93, 96.12, 96.3, 95.93, 96.72, 96.12, 96.5, 96.57, 96.73, 96.73, 96.78, 96.67, 96.88, 96.9, 96.77, 96.95, 96.57, 97.02, 96.85, 96.93, 96.4, 97.1, 96.88, 96.92, 97.13, 96.98, 96.88, 97.08, 97.18, 96.95, 97.1, 96.98, 96.95, 97.33, 97.03, 96.8, 96.5, 96.67, 96.6, 96.77, 96.73, 96.97, 96.82, 96.97, 96.83, 96.77]
network_20_node = [66.71, 67.02, 74.51, 74.45, 74.77, 77.75, 79.94, 80.02, 80.71, 81.61, 82.0, 83.22, 84.16, 84.54, 85.91, 85.87, 86.52, 87.43, 87.14, 87.47, 87.58, 87.9, 87.17, 88.11, 88.24, 88.99, 88.52, 89.21, 89.18, 89.05, 89.07, 89.15, 89.62, 89.8, 89.37, 89.63, 89.28, 90.27, 90.33, 90.47, 90.11, 90.64, 90.1, 90.76, 90.41, 90.51, 89.94, 90.19, 90.4, 90.32]

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
plt.ylim(85)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
