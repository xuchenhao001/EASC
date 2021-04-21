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
network_5_node = [94.70, 96.10, 96.70, 97.40, 97.30, 97.30, 97.10, 97.50, 97.50, 97.60, 97.90, 98.20, 98.00, 97.70, 97.70, 97.70, 98.20, 98.10, 97.90, 98.40, 98.10, 97.90, 97.90, 97.80, 98.30, 98.50, 98.60, 98.10, 98.40, 98.20, 98.20, 98.20, 98.30, 98.40, 98.40, 98.40, 98.50, 98.70, 98.30, 98.70, 98.60, 98.70, 98.70, 98.30, 98.40, 98.80, 98.40, 98.70, 98.50, 98.30]
network_10_node = [93.65, 96.50, 97.40, 97.55, 97.75, 98.25, 98.20, 98.05, 97.85, 98.45, 98.40, 98.25, 98.55, 98.45, 98.70, 98.55, 98.45, 98.60, 98.65, 98.85, 98.85, 98.60, 98.75, 98.90, 98.75, 98.95, 98.85, 98.95, 98.85, 98.80, 98.90, 98.90, 98.75, 98.75, 98.75, 98.80, 98.80, 98.75, 98.95, 98.75, 99.00, 98.65, 98.90, 99.00, 98.85, 99.05, 99.05, 99.00, 99.15, 98.85]
network_20_node = [94.60, 96.45, 96.95, 97.67, 97.50, 97.90, 98.22, 98.15, 98.12, 98.03, 98.30, 98.25, 98.42, 98.58, 98.33, 98.53, 98.60, 98.92, 98.83, 98.72, 98.50, 98.62, 98.85, 98.65, 98.88, 98.80, 98.55, 98.42, 98.58, 98.60, 98.80, 98.85, 98.85, 98.83, 98.88, 98.75, 99.05, 99.05, 98.80, 98.90, 98.95, 99.08, 99.05, 99.08, 99.03, 98.80, 99.00, 99.08, 99.10, 98.97]
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
