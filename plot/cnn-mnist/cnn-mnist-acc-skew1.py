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
local_train = [5.91, 82.39, 84.00, 84.57, 84.78, 85.00, 85.09, 85.39, 85.39, 85.39, 85.52, 85.52, 85.52, 85.57, 85.57, 85.61, 85.26, 85.57, 85.65, 85.57, 85.48, 85.57, 85.61, 85.65, 85.65, 85.52, 85.48, 85.61, 85.65, 85.52, 85.43, 85.70, 85.65, 85.78, 85.30, 85.65, 85.70, 85.52, 85.74, 85.61, 85.61, 85.70, 85.57, 85.70, 85.78, 85.78, 85.70, 85.70, 85.65, 85.65]
fed_avg = [39.91, 68.57, 75.30, 77.70, 81.78, 83.39, 86.35, 87.57, 88.74, 89.65, 89.96, 90.87, 91.30, 91.57, 91.87, 92.43, 92.22, 92.78, 92.70, 92.43, 92.78, 93.00, 93.57, 93.61, 94.09, 93.48, 93.70, 94.43, 94.65, 94.87, 94.22, 95.04, 95.35, 95.48, 95.30, 95.57, 95.87, 95.83, 95.78, 95.74, 96.00, 95.83, 95.96, 96.52, 96.52, 96.61, 96.30, 96.17, 96.43, 96.43]
apfl = [5.91, 71.00, 84.30, 85.04, 85.30, 85.26, 85.26, 85.52, 85.04, 85.52, 85.39, 85.52, 85.52, 85.48, 85.70, 85.65, 85.70, 85.61, 85.74, 85.57, 85.61, 85.70, 85.57, 85.78, 85.70, 85.57, 85.57, 85.57, 85.91, 85.61, 85.61, 85.87, 85.43, 85.61, 85.70, 85.78, 85.61, 85.70, 85.65, 85.57, 85.57, 85.61, 85.57, 85.65, 85.61, 85.57, 85.52, 85.61, 85.61, 85.78]
scei = [81.43, 83.91, 84.70, 84.83, 85.00, 85.43, 85.48, 85.48, 85.65, 85.96, 86.26, 86.17, 87.00, 87.91, 87.61, 88.52, 88.00, 88.00, 87.96, 89.17, 88.61, 90.57, 89.78, 89.83, 89.91, 90.65, 90.52, 90.61, 91.13, 90.70, 91.17, 91.39, 91.43, 91.35, 92.35, 91.83, 91.30, 91.30, 92.04, 92.39, 92.26, 91.96, 93.00, 93.00, 92.09, 93.43, 92.70, 92.48, 93.04, 92.87]

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
plt.ylim(80, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
