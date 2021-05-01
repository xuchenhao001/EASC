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
network_5_node = [91.1, 91.6, 91.67, 91.97, 92.13, 91.57, 92.67, 92.2, 92.63, 92.33, 93.47, 93.27, 93.4, 93.33, 93.9, 93.13, 93.17, 93.37, 93.3, 93.63, 93.53, 93.67, 93.33, 93.53, 93.13, 94.23, 93.7, 94.13, 93.53, 93.1, 93.37, 94.33, 94.0, 93.57, 94.3, 94.17, 94.3, 93.77, 93.67, 93.6, 94.1, 93.0, 93.57, 93.2, 93.47, 93.4, 93.87, 93.7, 93.67, 93.57]
network_10_node = [93.02, 94.05, 93.95, 94.22, 94.1, 94.35, 95.0, 94.8, 94.83, 95.08, 95.07, 95.2, 95.42, 95.07, 95.82, 95.13, 95.52, 95.42, 95.7, 95.42, 95.0, 95.77, 95.1, 95.63, 95.55, 95.75, 95.67, 96.1, 96.15, 96.12, 95.97, 95.88, 95.82, 95.98, 96.38, 96.17, 95.93, 96.18, 96.2, 95.62, 96.28, 96.03, 96.2, 96.02, 96.4, 96.07, 96.15, 95.95, 96.08, 96.2]
network_20_node = [71.97, 75.87, 79.7, 84.02, 85.16, 83.28, 88.83, 90.16, 87.78, 88.22, 89.42, 89.82, 90.62, 90.32, 90.92, 92.37, 91.55, 92.22, 93.29, 92.81, 91.38, 91.43, 92.61, 93.92, 92.32, 92.43, 93.75, 94.02, 92.91, 91.74, 92.82, 93.71, 92.31, 92.3, 92.07, 93.87, 92.05, 92.3, 92.0, 93.72, 93.27, 92.02, 93.92, 93.7, 92.42, 92.68, 93.14, 94.73, 92.91, 92.84]

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
