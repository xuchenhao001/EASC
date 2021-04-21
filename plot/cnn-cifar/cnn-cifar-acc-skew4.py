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
local_train = [9.46, 23.89, 29.51, 31.06, 34.2, 34.29, 35.4, 35.11, 34.17, 36.06, 36.09, 36.09, 36.06, 35.97, 36, 36.06, 35.89, 35.91, 35.91, 35.94, 35.8, 35.8, 35.77, 35.83, 35.77, 35.74, 35.77, 35.74, 35.83, 35.83, 35.74, 35.8, 35.74, 35.8, 35.83, 35.83, 35.77, 35.86, 35.8, 35.8, 35.83, 35.86, 35.8, 35.77, 35.77, 35.8, 35.83, 35.77, 35.86, 35.86]
fed_avg = [15.57, 23.94, 25.14, 27.63, 29.37, 32.6, 34.29, 38.4, 38.54, 39.31, 41.09, 42.43, 42.06, 43.11, 43.43, 43.66, 43.77, 44, 44.2, 44.29, 43.43, 43.37, 43.6, 43.11, 43.6, 43, 43.66, 43.14, 43.23, 43.43, 43.09, 43.09, 42.63, 43.2, 42.71, 43.11, 42.6, 42.4, 42.86, 42.91, 43.29, 42.54, 42.77, 42.57, 43.06, 42.51, 43.14, 42.94, 43.71, 42.69]
apfl = [9.46, 20.8, 29.63, 31.2, 33.74, 34.77, 35.69, 35.49, 35.6, 35.54, 35.11, 34, 34.69, 36.54, 36.46, 36.37, 36.29, 36.26, 36.17, 36.2, 36.11, 36.14, 36, 36.03, 36.14, 36.14, 36.14, 36.17, 36.09, 36.06, 36.17, 36.11, 36.17, 36.09, 36.09, 36.06, 36.09, 36.09, 36.11, 36, 36, 36.03, 36.03, 36.03, 36.03, 36.09, 36, 36.11, 36, 36.09]
scei = [25.74, 29.2, 32, 34.03, 35.46, 36.09, 35.97, 36.86, 36.8, 37.4, 37.54, 37.6, 37.86, 37.57, 37.46, 38.31, 37.8, 38.37, 38.49, 37.37, 38, 38.2, 37.37, 37.94, 38.29, 38.77, 38.69, 38.46, 39.6, 38.97, 39.83, 39.6, 39.83, 39.63, 39.77, 39.6, 39.77, 40.17, 39.43, 39.83, 40.31, 40.34, 40, 40.57, 40.54, 41.09, 41.43, 39.34, 39.54, 40.31]

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
plt.ylim(25)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
