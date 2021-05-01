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
network_5_node = [87.73, 89.87, 90.4, 91.6, 91.07, 91.53, 91.47, 91.93, 91.6, 92.4, 92.33, 92.33, 92.4, 92.4, 92.0, 91.6, 92.33, 92.07, 92.87, 92.27, 92.33, 92.33, 92.73, 92.67, 92.33, 92.53, 91.8, 91.67, 92.2, 92.53, 92.13, 91.87, 91.07, 92.13, 92.6, 92.93, 93.07, 92.27, 92.53, 91.8, 91.8, 92.13, 92.47, 92.33, 92.53, 92.13, 92.73, 92.4, 92.47, 92.53]
network_10_node = [86.33, 88.33, 89.23, 90.27, 89.6, 90.17, 89.43, 90.43, 90.4, 91.57, 91.03, 89.53, 91.43, 90.77, 90.27, 91.4, 91.4, 90.93, 91.53, 91.33, 91.33, 91.83, 91.2, 91.9, 91.53, 91.67, 92.1, 91.97, 91.97, 92.17, 92.0, 91.87, 92.17, 92.2, 92.03, 92.1, 92.1, 92.03, 91.63, 92.27, 92.2, 91.5, 92.43, 91.8, 92.6, 92.1, 91.97, 92.07, 92.47, 91.8]
network_20_node = [59.23, 59.15, 58.87, 60.12, 64.22, 63.35, 63.55, 63.98, 66.93, 67.25, 65.23, 65.83, 68.93, 68.37, 68.92, 68.72, 69.48, 70.13, 70.05, 70.97, 72.6, 72.0, 71.68, 72.35, 73.35, 72.87, 74.88, 73.82, 75.4, 74.03, 74.35, 74.2, 76.27, 76.58, 76.48, 76.77, 75.78, 75.57, 76.28, 76.2, 76.25, 76.32, 76.68, 77.37, 78.22, 75.48, 75.85, 76.07, 77.18, 77.68]

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
