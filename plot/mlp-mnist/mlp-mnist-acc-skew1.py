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
local_train = [8.09, 81.13, 82.13, 82.57, 82.39, 82.43, 82.22, 82.52, 82.52, 82.52, 82.74, 82.57, 82.48, 82.7, 82.48, 82.57, 82.48, 82.74, 82.61, 82.65, 82.52, 82.48, 82.43, 82.48, 82.35, 82.61, 82.52, 82.22, 82.39, 82.48, 82.43, 82.48, 82.35, 82.43, 82.39, 82.43, 82.43, 82.57, 82.48, 82.35, 82.48, 82.35, 82.48, 82.43, 82.43, 82.35, 82.43, 82.22, 82.48, 82.52]
fed_avg = [45.57, 61.43, 67.39, 71.35, 73.39, 75.26, 76.65, 77.57, 78.57, 79.13, 80.35, 80.74, 81.65, 82.3, 82.91, 83.3, 83.65, 84.04, 84.39, 84.87, 85.26, 85.57, 85.96, 86.13, 86.57, 86.39, 86.65, 86.96, 87.39, 87.65, 87.43, 87.65, 88.04, 88.13, 87.96, 88.39, 88.57, 88.83, 89.35, 89.13, 89.17, 89.04, 89.26, 89.43, 89.7, 89.52, 90.09, 90.57, 90.57, 90.48]
apfl = [8.09, 70.57, 81.87, 82.22, 82.3, 82.39, 82.43, 82.7, 82.39, 82.61, 82.65, 81.52, 83, 83, 82.78, 82.74, 82.57, 82.83, 82.91, 82.87, 82.78, 82.91, 82.91, 82.87, 82.83, 82.57, 82.74, 82.78, 82.74, 82.91, 82.87, 82.7, 82.83, 83, 82.87, 82.91, 82.7, 82.74, 82.74, 82.91, 82.83, 82.83, 82.91, 83.04, 82.78, 82.87, 83.09, 82.78, 82.96, 83.04]
scei = [80.43, 82, 82.26, 82.52, 82.91, 83.04, 82.83, 83, 83.39, 83.39, 84.09, 84.39, 84.3, 84.26, 84.35, 84.57, 85.3, 84.96, 85.04, 85.35, 85.17, 85.3, 85.35, 85.87, 85.78, 86.09, 86, 86, 86.43, 86.17, 86.74, 86.61, 87.17, 87, 86.87, 86.91, 87.3, 87.3, 87.09, 87.52, 87.3, 87.35, 87.26, 87.43, 87.48, 87.74, 88, 88.09, 88, 88.26]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, local_train, label="Local Training")
axes.plot(x, fed_avg, label="FedAvg")
axes.plot(x, apfl, label="APFL")
axes.plot(x, scei, label="SCEI with negotiated α")


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.ylim(80, 92)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
