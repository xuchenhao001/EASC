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
local_train = [11.03, 58.31, 59.03, 59.34, 59.22, 59.25, 59.09, 59.31, 59.31, 59.31, 59.47, 59.34, 59.28, 59.44, 59.28, 59.34, 59.28, 59.47, 59.38, 59.41, 59.31, 59.28, 59.25, 59.28, 59.19, 59.38, 59.31, 59.09, 59.22, 59.28, 59.25, 59.28, 59.19, 59.25, 59.22, 59.25, 59.25, 59.34, 59.28, 59.19, 59.28, 59.19, 59.28, 59.25, 59.25, 59.19, 59.25, 59.09, 59.28, 59.31]
fed_avg = [38.56, 54.28, 59.84, 64.38, 66.56, 69.59, 71.38, 72.53, 74.03, 74.53, 75.78, 76.28, 77.47, 78.44, 78.91, 79.53, 79.75, 80.28, 80.72, 81.03, 81.66, 81.91, 82.56, 82.5, 82.94, 82.97, 83.41, 83.91, 84.41, 84.66, 84.62, 85.06, 85.31, 85.38, 85.53, 85.72, 86, 86.25, 86.72, 86.59, 86.66, 86.69, 86.78, 87.19, 87.34, 87.06, 87.56, 88.25, 88.12, 88.12]
apfl = [11.03, 52.56, 58.88, 59.12, 59.16, 59.22, 59.25, 59.44, 59.22, 59.38, 59.41, 59.97, 59.91, 59.91, 59.66, 59.59, 59.41, 59.59, 59.66, 59.62, 59.53, 59.66, 59.66, 59.62, 59.59, 59.41, 59.53, 59.56, 59.5, 59.62, 59.59, 59.5, 59.56, 59.69, 59.59, 59.62, 59.47, 59.5, 59.5, 59.62, 59.56, 59.56, 59.62, 59.72, 59.53, 59.59, 59.78, 59.53, 59.66, 59.72]
scei = [57.81, 58.94, 59.25, 59.56, 60.22, 60.59, 60.59, 61.41, 61.75, 62.12, 64.41, 64.72, 64.34, 64.56, 65.03, 65.22, 66.88, 66.22, 66.44, 66.84, 66.78, 67.09, 67.25, 68.09, 68.06, 68.81, 68.38, 68.66, 69.34, 69.03, 70.59, 69.91, 71.5, 70.28, 70.25, 70.19, 71.12, 71.28, 70.59, 72.25, 71.62, 71.34, 71.25, 71.53, 72.06, 72.5, 74, 72.5, 72.44, 73.16]

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
plt.ylim(55, 90)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
