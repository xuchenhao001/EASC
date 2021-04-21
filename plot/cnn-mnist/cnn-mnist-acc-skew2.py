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
local_train = [6.41, 65.34, 66.62, 67.07, 67.24, 67.41, 67.48, 67.72, 67.72, 67.72, 67.83, 67.83, 67.83, 67.86, 67.86, 67.90, 67.62, 67.86, 67.93, 67.86, 67.79, 67.86, 67.90, 67.93, 67.93, 67.83, 67.79, 67.90, 67.93, 67.83, 67.76, 67.97, 67.93, 68.03, 67.66, 67.93, 67.97, 67.83, 68.00, 67.90, 67.90, 67.97, 67.86, 67.97, 68.03, 68.03, 67.97, 67.97, 67.93, 67.93]
fed_avg = [34.14, 63.24, 69.55, 72.52, 76.72, 78.93, 82.41, 84.03, 85.59, 86.93, 86.93, 88.10, 88.59, 88.86, 89.52, 90.07, 89.76, 90.52, 90.59, 90.24, 90.55, 90.93, 91.41, 91.83, 92.03, 91.59, 91.90, 92.48, 93.03, 92.97, 92.31, 93.07, 93.66, 93.83, 93.62, 94.31, 94.45, 94.34, 94.28, 94.31, 94.41, 94.21, 94.45, 95.10, 95.03, 95.24, 94.93, 94.72, 95.17, 95.00]
apfl = [6.41, 57.34, 66.86, 67.45, 67.66, 67.62, 67.62, 67.83, 67.45, 67.83, 67.72, 67.83, 67.83, 67.79, 67.97, 67.93, 67.97, 67.90, 68.00, 67.86, 67.90, 67.97, 67.86, 68.03, 67.97, 67.86, 67.86, 67.86, 68.14, 67.90, 67.90, 68.10, 67.76, 67.90, 67.97, 68.03, 67.90, 67.97, 67.93, 67.86, 67.86, 67.90, 67.86, 67.93, 67.90, 67.86, 67.83, 67.90, 67.90, 68.03]
scei = [64.59, 66.55, 67.17, 67.28, 67.41, 67.86, 67.90, 67.86, 68.69, 68.86, 69.38, 69.48, 70.66, 72.31, 71.90, 73.62, 73.03, 73.03, 73.03, 74.72, 74.59, 79.14, 76.45, 76.28, 76.83, 77.93, 78.21, 77.83, 79.38, 78.86, 79.24, 81.14, 80.83, 79.79, 83.93, 82.07, 80.93, 80.03, 81.59, 83.00, 83.10, 82.14, 85.38, 84.86, 82.55, 85.59, 83.83, 83.00, 85.31, 84.69]

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
plt.ylim(60, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
