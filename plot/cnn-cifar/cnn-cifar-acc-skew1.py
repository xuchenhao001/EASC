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
local_train = [8.17, 36.35, 44.91, 47.26, 52.04, 52.17, 53.87, 53.43, 52, 54.87, 54.91, 54.91, 54.87, 54.74, 54.78, 54.87, 54.61, 54.65, 54.65, 54.7, 54.48, 54.48, 54.43, 54.52, 54.43, 54.39, 54.43, 54.39, 54.52, 54.52, 54.39, 54.48, 54.39, 54.48, 54.52, 54.52, 54.43, 54.57, 54.48, 54.48, 54.52, 54.57, 54.48, 54.43, 54.43, 54.48, 54.52, 54.43, 54.57, 54.57]
fed_avg = [17.7, 25.83, 27.04, 30.13, 31.65, 35.22, 37, 40.52, 40.7, 41.39, 43.13, 44.35, 43.74, 44.65, 44.3, 44.74, 44.78, 45.35, 45.43, 45.22, 43.91, 44.17, 44.61, 44.13, 44.7, 44.17, 44.7, 44.52, 44.09, 44.61, 43.91, 44.3, 43.35, 44.48, 43.57, 43.7, 43.96, 43.52, 43.57, 44.22, 44.13, 44, 43.61, 44.09, 44.57, 43.91, 44.61, 43.83, 44.61, 44.09]
apfl = [8.17, 31.65, 45.09, 47.48, 51.35, 52.91, 54.3, 54, 54.17, 54.09, 53.43, 51.74, 52.78, 55.61, 55.48, 55.35, 55.22, 55.17, 55.04, 55.09, 54.96, 55, 54.78, 54.83, 55, 55, 55, 55.04, 54.91, 54.87, 55.04, 54.96, 55.04, 54.91, 54.91, 54.87, 54.91, 54.91, 54.96, 54.78, 54.78, 54.83, 54.83, 54.83, 54.83, 54.91, 54.78, 54.96, 54.78, 54.91]
scei = [39.17, 44.43, 48.7, 51.78, 53.96, 54.91, 54.74, 56.09, 56, 56.87, 57.13, 57.13, 57.26, 56.83, 56.74, 57.96, 57.26, 58, 58.04, 56.35, 57.09, 57.09, 56.3, 56.83, 57.17, 57.83, 57.43, 57.13, 57.43, 57.96, 58.17, 58.35, 58.48, 58.35, 57.87, 58.43, 58.13, 58.39, 57.78, 58.17, 58.3, 58.26, 58.17, 58.61, 58.52, 58.52, 58.3, 57.26, 57.96, 58.39]

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
plt.ylim(30)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
