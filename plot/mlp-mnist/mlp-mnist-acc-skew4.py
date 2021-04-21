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
local_train = [11.31, 53.31, 53.97, 54.26, 54.14, 54.17, 54.03, 54.23, 54.23, 54.23, 54.37, 54.26, 54.2, 54.34, 54.2, 54.26, 54.2, 54.37, 54.29, 54.31, 54.23, 54.2, 54.17, 54.2, 54.11, 54.29, 54.23, 54.03, 54.14, 54.2, 54.17, 54.2, 54.11, 54.17, 54.14, 54.17, 54.17, 54.26, 54.2, 54.11, 54.2, 54.11, 54.2, 54.17, 54.17, 54.11, 54.17, 54.03, 54.2, 54.23]
fed_avg = [36.71, 52.54, 58.14, 62.57, 64.89, 67.34, 69.06, 70.14, 71.63, 72.49, 73.83, 74.4, 75.54, 76.57, 77.54, 78.09, 78.49, 79.03, 79.63, 80.09, 80.83, 81.2, 81.6, 81.83, 82.34, 82.31, 82.71, 83.11, 83.43, 83.8, 83.83, 84.49, 84.74, 84.86, 85.11, 85.34, 85.69, 85.74, 86.31, 86.11, 86.31, 86.37, 86.4, 86.66, 87.03, 86.66, 87.23, 87.77, 87.69, 87.54]
apfl = [11.31, 48.71, 53.8, 54.03, 54.09, 54.14, 54.17, 54.34, 54.14, 54.29, 54.31, 55.17, 55.06, 54.89, 54.54, 54.46, 54.34, 54.51, 54.57, 54.51, 54.46, 54.54, 54.57, 54.54, 54.49, 54.31, 54.43, 54.46, 54.43, 54.54, 54.51, 54.4, 54.49, 54.6, 54.51, 54.54, 54.4, 54.43, 54.43, 54.54, 54.49, 54.49, 54.54, 54.63, 54.43, 54.51, 54.66, 54.46, 54.57, 54.6]
scei = [52.86, 53.89, 54.2, 54.77, 55.49, 55.74, 55.77, 56.66, 56.8, 57.43, 59.51, 60.17, 59.91, 60.17, 60.8, 61.34, 63.06, 62.23, 62.37, 62.83, 62.97, 63.26, 63.34, 64.43, 64.6, 65.31, 65.06, 65.03, 66.23, 65.71, 67.8, 67, 68.8, 66.83, 67.03, 66.97, 67.69, 68.29, 67.6, 69.2, 68.83, 68.46, 68.66, 68.63, 69.26, 69.8, 71.23, 70.09, 69.83, 70.63]

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
plt.ylim(50, 90)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
