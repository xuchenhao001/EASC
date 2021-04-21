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
network_5_node = [90.75, 92.25, 92.75, 93.75, 93, 93.25, 93.5, 93.25, 93.40, 93.50, 93.80, 94.30, 93.75, 93.40, 93.60, 93.30, 94.60, 94.00, 94.00, 94.50, 94.30, 94.50, 94.40, 94.60, 94.40, 94.70, 94.60, 94.60, 94.60, 94.80, 94.90, 94.50, 94.80, 94.50, 94.70, 94.80, 94.90, 94.50, 94.60, 94.30, 94.60, 94.80, 94.80, 94.80, 94.50, 94.80, 94.90, 94.70, 94.70, 94.80]
network_10_node = [92.5, 94.3, 94.6, 94.8, 94.95, 95.15, 94.85, 94.85, 95.15, 94.9, 94.8, 95.1, 95.15, 95.1, 94.95, 95.2, 95.4, 95.25, 95.45, 95.5, 95.35, 95.45, 95.3, 95.5, 95.45, 95.55, 95.45, 95.5, 95.6, 95.55, 95.3, 95.4, 95.3, 95.75, 95.6, 95.55, 95.7, 95.65, 95.5, 95.65, 95.5, 95.7, 95.6, 95.65, 95.55, 95.75, 95.55, 95.85, 96, 95.95]
network_20_node = [93.625, 93.75, 94, 94.375, 94.875, 94.75, 94.55, 94.5, 94.66, 95, 95.22, 95.44, 95.22, 95.11, 95.83, 95.38, 95.5, 95.94, 95.66, 95.16, 95.72, 95.27, 94.83, 95.38, 95.22, 95.44, 95.66, 95.77, 95.72, 96.16, 96, 95.83, 95.83, 95.94, 95.5, 95.33, 95.72, 95.44, 95.94, 95.44, 95.77, 95.83, 96.05, 96.05, 95.94, 95.77, 96.16, 96.27, 96.05, 95.94]

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
