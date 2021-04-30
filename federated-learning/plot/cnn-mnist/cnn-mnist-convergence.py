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
network_10_node = [47.80, 56.20, 66.75, 77.55, 77.75, 77.95, 76.95, 79.60, 80.65, 80.25, 80.45, 89.10, 88.55, 88.15, 87.30, 91.00, 92.05, 90.65, 85.00, 88.95, 91.20, 90.15, 92.00, 93.00, 93.30, 94.60, 93.95, 89.00, 94.15, 93.95, 91.05, 92.65, 94.30, 92.65, 93.85, 93.05, 93.25, 95.10, 94.00, 91.25, 92.35, 93.15, 94.10, 94.30, 95.75, 95.55, 94.70, 91.70, 95.50, 95.15]
network_20_node = [42.20, 49.42, 63.38, 71.90, 75.55, 78.33, 83.30, 81.83, 86.25, 87.62, 93.08, 92.33, 89.42, 91.38, 92.47, 91.20, 91.35, 92.40, 93.95, 90.55, 94.28, 93.62, 95.10, 95.03, 94.00, 94.90, 96.08, 95.35, 95.85, 96.78, 94.58, 91.88, 95.92, 95.25, 96.38, 96.30, 95.30, 96.17, 94.78, 96.45, 96.45, 97.17, 94.97, 95.03, 96.20, 96.80, 97.28, 96.92, 97.12, 97.30]
# network_50_node = [94.98, 96.69, 96.91, 97.46, 96.97, 97.54, 97.90, 97.82, 98.13, 98.17, 98.18, 98.29, 98.53, 98.32, 98.55, 98.58, 98.53, 98.60, 98.42, 98.63, 98.72, 98.87, 98.80, 98.72, 98.77, 98.75, 98.79, 98.85, 98.87, 98.83, 98.82, 98.85, 98.85, 98.96, 99.01, 98.95, 99.00, 99.01, 99.10, 98.99, 98.92, 99.01, 98.96, 98.93, 98.99, 99.09, 98.99, 99.11, 99.05, 99.13]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, network_5_node, label="SCEI with 5 nodes")
axes.plot(x, network_10_node, label="SCEI with 10 nodes")
axes.plot(x, network_20_node, label="SCEI with 20 nodes")
# axes.plot(x, network_50_peer, label="SCEI with 50 nodes")

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
# plt.ylim(40)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
