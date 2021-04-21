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
local_train = [10.03, 64.34, 65.14, 65.48, 65.34, 65.38, 65.21, 65.45, 65.45, 65.45, 65.62, 65.48, 65.41, 65.59, 65.41, 65.48, 65.41, 65.62, 65.52, 65.55, 65.45, 65.41, 65.38, 65.41, 65.31, 65.52, 65.45, 65.21, 65.34, 65.41, 65.38, 65.41, 65.31, 65.38, 65.34, 65.38, 65.38, 65.48, 65.41, 65.31, 65.41, 65.31, 65.41, 65.38, 65.38, 65.31, 65.38, 65.21, 65.41, 65.45]
fed_avg = [40.45, 56.69, 62.28, 66.28, 68.79, 70.86, 72.14, 73.28, 74.55, 75.21, 76.62, 77.14, 78.1, 78.62, 79.38, 80.17, 80.55, 80.93, 81.59, 81.72, 82.55, 82.9, 83.24, 83.21, 83.76, 83.72, 84, 84.31, 84.9, 85.17, 85.03, 85.45, 85.72, 85.79, 85.86, 86.21, 86.55, 86.69, 87.21, 87.1, 87.17, 87.17, 87.34, 87.62, 87.86, 87.48, 88.1, 88.83, 88.69, 88.66]
apfl = [10.03, 57.17, 64.93, 65.21, 65.28, 65.34, 65.38, 65.59, 65.34, 65.52, 65.55, 65.62, 66.17, 65.97, 65.72, 65.69, 65.52, 65.72, 65.79, 65.72, 65.66, 65.76, 65.76, 65.72, 65.69, 65.48, 65.62, 65.66, 65.62, 65.76, 65.72, 65.59, 65.69, 65.83, 65.72, 65.76, 65.59, 65.62, 65.62, 65.76, 65.69, 65.69, 65.76, 65.86, 65.66, 65.72, 65.9, 65.66, 65.79, 65.86]
scei = [63.79, 65.03, 65.38, 65.66, 66.34, 66.55, 66.62, 67.21, 67.79, 67.86, 69.31, 69.97, 69.45, 69.66, 70.31, 70.52, 71.86, 71.03, 71.24, 71.66, 71.9, 71.97, 72.21, 72.86, 72.9, 73.38, 73.28, 73.41, 74.21, 73.52, 75.17, 74.83, 76.1, 75.21, 75.03, 75, 75.52, 75.79, 75.41, 76.55, 76.21, 75.83, 75.93, 76.24, 76.17, 76.76, 77.72, 76.86, 76.97, 77.52]

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
plt.ylim(60, 90)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
