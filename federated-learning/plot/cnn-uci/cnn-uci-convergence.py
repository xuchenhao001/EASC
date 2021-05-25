# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import cycler

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
network_5_node = [90.27, 90.33, 90.67, 90.5, 91.07, 92.13, 91.67, 91.8, 92.0, 91.83, 91.53, 92.7, 92.3, 92.8, 92.57, 92.37, 92.53, 93.17, 91.93, 92.77, 92.7, 92.7, 92.8, 92.53, 93.27, 93.13, 92.17, 92.67, 92.3, 92.57, 91.33, 91.9, 92.57, 92.8, 91.8, 91.6, 92.93, 92.87, 92.43, 92.17, 92.33, 92.2, 92.23, 93.03, 92.63, 92.6, 92.73, 92.43, 92.8, 92.93]
network_10_node = [95.25, 94.8, 96.03, 96.03, 95.93, 96.12, 96.3, 95.93, 96.72, 96.12, 96.5, 96.57, 96.73, 96.73, 96.78, 96.67, 96.88, 96.9, 96.77, 96.95, 96.57, 97.02, 96.85, 96.93, 96.4, 97.1, 96.88, 96.92, 97.13, 96.98, 96.88, 97.08, 97.18, 96.95, 97.1, 96.98, 96.95, 97.33, 97.03, 96.8, 96.5, 96.67, 96.6, 96.77, 96.73, 96.97, 96.82, 96.97, 96.83, 96.77]
network_20_node = [71.99, 72.17, 79.01, 76.83, 80.51, 83.1, 85.42, 85.07, 87.35, 88.22, 89.27, 89.43, 90.24, 90.26, 91.5, 90.97, 90.62, 90.71, 91.76, 92.11, 91.22, 91.72, 92.21, 92.09, 91.67, 91.77, 91.62, 92.25, 92.0, 91.85, 92.59, 92.62, 92.22, 92.86, 92.04, 92.34, 92.2, 91.57, 92.07, 91.88, 91.84, 92.58, 92.49, 91.86, 91.92, 91.64, 91.92, 92.45, 92.22, 92.13]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, network_5_node, label="SCEI with 5 nodes")
axes.plot(x, network_10_node, label="SCEI with 10 nodes")
axes.plot(x, network_20_node, label="SCEI with 20 nodes")

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(85)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
