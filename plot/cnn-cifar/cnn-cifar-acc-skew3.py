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
local_train = [9.12, 26.12, 32.28, 33.97, 37.41, 37.5, 38.72, 38.41, 37.38, 39.44, 39.47, 39.47, 39.44, 39.34, 39.38, 39.44, 39.25, 39.28, 39.28, 39.31, 39.16, 39.16, 39.12, 39.19, 39.12, 39.09, 39.12, 39.09, 39.19, 39.19, 39.09, 39.16, 39.09, 39.16, 39.19, 39.19, 39.12, 39.22, 39.16, 39.16, 39.19, 39.22, 39.16, 39.12, 39.12, 39.16, 39.19, 39.12, 39.22, 39.22]
fed_avg = [15.97, 24.5, 26.28, 28.88, 30.28, 34.03, 35.53, 38.66, 39.53, 40.06, 42.16, 43.22, 42.75, 43.41, 43.09, 43.88, 44.28, 44, 44.22, 44.38, 43.88, 44.38, 44.34, 43.91, 44.5, 44.16, 44.59, 44.44, 43.94, 44.53, 44.06, 44.38, 43.66, 44.03, 43.31, 43.5, 43.62, 43.59, 43.34, 43.97, 44.28, 43.66, 43.94, 43.91, 44.47, 43.5, 44, 43.66, 44.03, 43.81]
apfl = [9.12, 22.75, 32.41, 34.12, 36.91, 38.03, 39.03, 38.81, 38.94, 38.88, 38.41, 37.19, 37.94, 39.97, 39.88, 39.78, 39.69, 39.66, 39.56, 39.59, 39.5, 39.53, 39.38, 39.41, 39.53, 39.53, 39.53, 39.56, 39.47, 39.44, 39.56, 39.5, 39.56, 39.47, 39.47, 39.44, 39.47, 39.47, 39.5, 39.38, 39.38, 39.41, 39.41, 39.41, 39.41, 39.47, 39.38, 39.5, 39.38, 39.47]
scei = [28.16, 31.94, 35, 37.22, 38.78, 39.47, 39.34, 40.31, 40.25, 40.88, 41.06, 41.06, 41.31, 41.06, 40.91, 41.84, 41.38, 41.94, 42.06, 40.81, 41.56, 41.56, 40.91, 41.25, 41.88, 42.19, 42.12, 41.94, 42.47, 42.53, 43, 42.78, 42.97, 42.91, 42.84, 42.84, 42.88, 43.31, 42.53, 43.19, 43.47, 43.5, 43.34, 43.69, 43.75, 44, 44.38, 42.53, 42.88, 43.66]

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
