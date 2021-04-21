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
local_train = [6.94, 59.22, 60.38, 60.78, 60.94, 61.09, 61.16, 61.38, 61.38, 61.38, 61.47, 61.47, 61.47, 61.50, 61.50, 61.53, 61.28, 61.50, 61.56, 61.50, 61.44, 61.50, 61.53, 61.56, 61.56, 61.47, 61.44, 61.53, 61.56, 61.47, 61.41, 61.59, 61.56, 61.66, 61.31, 61.56, 61.59, 61.47, 61.62, 61.53, 61.53, 61.59, 61.50, 61.59, 61.66, 61.66, 61.59, 61.59, 61.56, 61.56]
fed_avg = [32.28, 60.91, 67.50, 70.75, 75.41, 77.34, 80.78, 82.66, 84.12, 85.53, 85.88, 86.88, 87.03, 87.56, 87.97, 88.47, 88.31, 88.94, 88.91, 88.53, 89.12, 89.38, 90.00, 90.22, 90.78, 89.91, 90.44, 90.91, 91.47, 91.41, 90.59, 91.94, 92.41, 92.31, 92.22, 92.66, 92.94, 92.97, 92.88, 92.81, 93.19, 92.81, 93.09, 94.25, 94.16, 93.94, 93.81, 93.38, 94.09, 93.41]
apfl = [6.94, 52.78, 60.59, 61.12, 61.31, 61.28, 61.28, 61.47, 61.12, 61.47, 61.38, 61.47, 61.47, 61.44, 61.59, 61.56, 61.59, 61.53, 61.62, 61.50, 61.53, 61.59, 61.50, 61.66, 61.59, 61.50, 61.50, 61.50, 61.75, 61.53, 61.53, 61.72, 61.41, 61.53, 61.59, 61.66, 61.53, 61.59, 61.56, 61.50, 61.50, 61.53, 61.50, 61.56, 61.53, 61.50, 61.47, 61.53, 61.53, 61.66]
scei = [58.53, 60.31, 60.88, 60.97, 61.09, 61.44, 61.53, 61.47, 62.50, 62.75, 63.34, 63.47, 65.03, 67.19, 66.50, 68.41, 67.59, 67.94, 67.44, 69.59, 68.75, 75.00, 72.03, 71.47, 72.12, 73.97, 73.94, 73.69, 75.78, 74.69, 75.19, 77.47, 77.38, 76.19, 81.31, 79.00, 77.06, 76.66, 78.28, 80.03, 79.94, 79.09, 82.59, 82.22, 79.28, 83.00, 81.12, 80.41, 82.78, 82.34]

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
