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
network_5_node = [87.27, 90.47, 90.2, 91.53, 92.2, 91.6, 92.13, 91.67, 92.33, 92.13, 92.0, 92.8, 92.8, 92.4, 92.27, 92.13, 91.93, 92.6, 93.6, 93.2, 93.33, 93.33, 92.4, 92.0, 92.67, 93.13, 92.53, 92.93, 92.4, 91.27, 93.27, 93.07, 93.47, 92.87, 92.73, 93.0, 93.2, 93.33, 93.2, 91.87, 92.53, 92.73, 93.0, 93.0, 92.8, 92.87, 92.93, 92.6, 93.27, 93.0]
network_10_node = [84.53, 86.03, 87.4, 88.4, 87.93, 88.77, 88.67, 88.33, 88.63, 89.4, 89.5, 89.37, 89.47, 89.5, 88.73, 89.47, 89.37, 90.07, 89.57, 90.23, 89.83, 90.5, 90.3, 90.47, 90.37, 90.17, 90.17, 90.23, 90.03, 90.67, 90.3, 90.73, 90.6, 90.27, 90.47, 90.9, 90.9, 90.67, 90.4, 90.43, 90.5, 90.43, 90.43, 90.93, 90.73, 91.23, 91.73, 91.13, 91.07, 90.83]
network_20_node = [57.75, 53.48, 55.35, 60.98, 59.0, 59.82, 62.02, 61.53, 63.08, 62.82, 64.63, 64.33, 66.23, 65.5, 66.82, 66.88, 68.92, 67.3, 68.35, 67.62, 69.25, 66.95, 67.52, 67.63, 69.55, 69.67, 70.38, 69.4, 69.52, 69.67, 71.57, 70.35, 69.57, 70.78, 70.82, 68.9, 71.35, 71.07, 70.07, 70.32, 72.92, 72.93, 72.13, 71.2, 73.18, 71.87, 72.67, 70.55, 71.93, 73.05]

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
# plt.ylim(40)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
