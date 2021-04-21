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
local_train = [8.83, 28.83, 35.62, 37.48, 41.28, 41.38, 42.72, 42.38, 41.24, 43.52, 43.55, 43.55, 43.52, 43.41, 43.45, 43.52, 43.31, 43.34, 43.34, 43.38, 43.21, 43.21, 43.17, 43.24, 43.17, 43.14, 43.17, 43.14, 43.24, 43.24, 43.14, 43.21, 43.14, 43.21, 43.24, 43.24, 43.17, 43.28, 43.21, 43.21, 43.24, 43.28, 43.21, 43.17, 43.17, 43.21, 43.24, 43.17, 43.28, 43.28]
fed_avg = [16.79, 25.03, 26.24, 28.93, 30.45, 34.52, 35.66, 39.1, 39.28, 39.72, 41.66, 43.24, 42.41, 43.1, 43.24, 43.41, 44, 44.1, 44.03, 44.38, 43.34, 44.14, 44.21, 43.66, 43.86, 43.72, 44.52, 43.79, 43.86, 44.24, 43.66, 44.03, 43.03, 43.55, 43.14, 43.21, 43.1, 43.17, 43.03, 43.79, 44.21, 43.03, 43.48, 43.52, 43.9, 43.69, 43.93, 43.45, 43.97, 43.86]
apfl = [8.83, 25.1, 35.76, 37.66, 40.72, 41.97, 43.07, 42.83, 42.97, 42.9, 42.38, 41.03, 41.86, 44.1, 44, 43.9, 43.79, 43.76, 43.66, 43.69, 43.59, 43.62, 43.45, 43.48, 43.62, 43.62, 43.62, 43.66, 43.55, 43.52, 43.66, 43.59, 43.66, 43.55, 43.55, 43.52, 43.55, 43.55, 43.59, 43.45, 43.45, 43.48, 43.48, 43.48, 43.48, 43.55, 43.45, 43.59, 43.45, 43.55]
scei = [31.07, 35.24, 38.62, 41.07, 42.79, 43.55, 43.41, 44.48, 44.41, 45.17, 45.31, 45.34, 45.48, 45.14, 45.03, 46.14, 45.55, 46.31, 46.48, 44.9, 45.59, 45.72, 44.97, 45.79, 46.03, 46.48, 46.38, 46, 46.69, 46.72, 47.14, 47.31, 47.38, 47.31, 46.86, 47.34, 47.14, 47.41, 46.72, 47.17, 47.38, 47.34, 47.07, 47.86, 47.83, 48, 48.21, 46.55, 47.03, 47.76]

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
