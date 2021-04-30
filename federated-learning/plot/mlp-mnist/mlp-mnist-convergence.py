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
network_5_node = [41.80, 51.00, 62.90, 69.60, 80.20, 81.00, 81.80, 87.20, 85.50, 84.30, 87.20, 86.20, 83.10, 84.40, 88.90, 88.30, 88.90, 92.90, 89.80, 85.80, 90.10, 91.20, 93.50, 92.40, 90.90, 91.50, 91.20, 92.30, 94.80, 93.60, 92.90, 92.30, 92.80, 91.80, 93.30, 93.30, 93.40, 93.90, 94.00, 94.60, 91.50, 92.60, 94.90, 93.70, 93.60, 92.50, 93.20, 93.20, 95.50, 96.00]
network_10_node = [46.90, 59.75, 58.65, 62.30, 70.65, 69.85, 80.85, 76.00, 77.25, 77.50, 77.05, 76.30, 76.50, 79.95, 83.55, 81.95, 82.95, 81.10, 84.40, 79.20, 80.70, 82.60, 79.85, 87.05, 86.10, 85.65, 86.85, 85.60, 86.80, 87.00, 85.60, 87.55, 87.25, 87.70, 87.70, 89.10, 87.05, 86.55, 88.10, 88.35, 88.10, 87.50, 88.40, 87.80, 88.70, 86.60, 88.70, 88.25, 88.45, 86.50]
network_20_node = [41.25, 41.45, 52.67, 61.02, 67.60, 72.15, 75.30, 76.42, 78.88, 80.20, 75.92, 73.97, 76.33, 72.58, 75.08, 82.67, 83.47, 81.10, 81.65, 84.47, 85.40, 83.92, 82.92, 85.50, 88.80, 87.90, 88.47, 86.90, 87.05, 88.45, 88.03, 87.85, 89.78, 88.55, 89.35, 88.67, 89.53, 87.25, 87.70, 88.85, 86.38, 88.58, 88.70, 88.95, 90.58, 90.35, 86.62, 90.10, 89.55, 90.05]

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
