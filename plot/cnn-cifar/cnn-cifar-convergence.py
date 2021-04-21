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
network_5_node = [39.60, 48.20, 53.40, 52.90, 54.90, 57.00, 58.70, 61.80, 62.80, 61.10, 60.10, 62.40, 62.20, 62.70, 62.30, 63.00, 62.20, 62.00, 63.90, 63.00, 63.30, 63.50, 63.60, 62.70, 62.70, 63.50, 62.40, 62.80, 62.10, 62.30, 63.20, 63.60, 61.30, 61.80, 61.70, 62.90, 61.80, 63.10, 62.90, 63.70, 63.80, 64.50, 63.60, 64.00, 61.90, 63.20, 63.90, 62.40, 63.10, 61.10]
network_10_node = [45.05, 51.1, 56, 59.55, 62.05, 63.15, 62.95, 64.5, 64.4, 65.4, 65.7, 65.7, 65.7, 65.25, 65.25, 66.55, 65.8, 66.6, 66.55, 64.75, 65.45, 65.35, 64.65, 65.25, 65.45, 66.35, 65.8, 65.25, 65.45, 66.45, 66.5, 66.8, 66.75, 66.75, 66, 66.9, 66.4, 66.5, 66.15, 66.45, 66.55, 66.25, 66.35, 66.9, 66.85, 66.7, 66.35, 65.55, 66.2, 66.5]
network_20_node = [51.77, 54.38, 56.90, 59.27, 60.10, 61.95, 63.83, 63.67, 64.50, 64.95, 64.60, 65.20, 65.45, 66.55, 65.97, 66.28, 65.78, 66.95, 65.70, 66.95, 66.75, 67.00, 67.17, 67.17, 67.75, 67.33, 65.83, 67.25, 67.88, 67.33, 67.58, 67.72, 67.12, 66.53, 67.50, 67.72, 67.80, 67.70, 67.88, 68.17, 66.85, 68.08, 68.30, 67.28, 68.30, 68.53, 67.55, 67.35, 67.97, 67.55]

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
plt.ylim(40)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
