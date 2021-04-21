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
local_train = [7.03, 54.14, 55.20, 55.57, 55.71, 55.86, 55.91, 56.11, 56.11, 56.11, 56.20, 56.20, 56.20, 56.23, 56.23, 56.26, 56.03, 56.23, 56.29, 56.23, 56.17, 56.23, 56.26, 56.29, 56.29, 56.20, 56.17, 56.26, 56.29, 56.20, 56.14, 56.31, 56.29, 56.37, 56.06, 56.29, 56.31, 56.20, 56.34, 56.26, 56.26, 56.31, 56.23, 56.31, 56.37, 56.37, 56.31, 56.31, 56.29, 56.29]
fed_avg = [30.60, 58.74, 65.80, 68.63, 73.91, 76.09, 79.71, 81.23, 82.63, 83.97, 84.40, 85.37, 85.77, 86.49, 87.09, 87.91, 87.34, 87.97, 88.66, 87.89, 88.23, 89.00, 89.71, 90.03, 90.40, 89.60, 89.94, 90.74, 91.29, 91.49, 90.51, 91.66, 92.23, 92.46, 92.40, 92.66, 93.23, 93.00, 92.77, 93.03, 93.14, 93.03, 93.14, 94.23, 94.23, 94.06, 93.80, 93.40, 94.11, 93.80]
apfl = [7.03, 48.80, 55.40, 55.89, 56.06, 56.03, 56.03, 56.20, 55.89, 56.20, 56.11, 56.20, 56.20, 56.17, 56.31, 56.29, 56.31, 56.26, 56.34, 56.23, 56.26, 56.31, 56.23, 56.37, 56.31, 56.23, 56.23, 56.23, 56.46, 56.26, 56.26, 56.43, 56.14, 56.26, 56.31, 56.37, 56.26, 56.31, 56.29, 56.23, 56.23, 56.26, 56.23, 56.29, 56.26, 56.23, 56.20, 56.26, 56.26, 56.37]
scei = [53.51, 55.14, 55.66, 55.74, 55.86, 56.31, 56.43, 56.46, 57.51, 57.97, 58.34, 58.54, 60.49, 62.34, 61.97, 64.14, 63.23, 63.46, 62.69, 65.46, 64.46, 71.34, 67.51, 67.29, 67.66, 69.74, 69.97, 69.57, 72.51, 71.06, 71.26, 74.11, 73.71, 72.31, 78.54, 75.63, 73.86, 72.94, 74.57, 77.34, 76.60, 75.89, 79.80, 79.57, 75.97, 80.74, 77.94, 77.11, 79.80, 79.29]

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
plt.ylim(50, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
