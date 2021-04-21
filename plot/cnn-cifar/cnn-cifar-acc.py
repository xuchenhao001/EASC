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
local_train = [7.6, 41.8, 51.65, 54.35, 59.85, 60, 61.95, 61.45, 59.8, 63.1, 63.15, 63.15, 63.1, 62.95, 63, 63.1, 62.8, 62.85, 62.85, 62.9, 62.65, 62.65, 62.6, 62.7, 62.6, 62.55, 62.6, 62.55, 62.7, 62.7, 62.55, 62.65, 62.55, 62.65, 62.7, 62.7, 62.6, 62.75, 62.65, 62.65, 62.7, 62.75, 62.65, 62.6, 62.6, 62.65, 62.7, 62.6, 62.75, 62.75]
fed_avg = [18.45, 27.35, 28.25, 31.2, 32.85, 36.7, 38.5, 41.8, 42.2, 42.7, 44.35, 45.9, 45.1, 46.15, 45.7, 46.05, 46.4, 46.65, 46.85, 46.7, 45.25, 45.65, 45.9, 45.3, 46.2, 45.45, 46.2, 45.8, 45.5, 45.95, 45.35, 45.7, 44.55, 45.6, 44.8, 44.95, 45.05, 44.95, 44.8, 45.3, 45.65, 44.9, 45.3, 45.45, 45.75, 45.2, 45.8, 45.2, 45.55, 45.2]
apfl = [7.6, 36.4, 51.85, 54.6, 59.05, 60.85, 62.45, 62.1, 62.3, 62.2, 61.45, 59.5, 60.7, 63.95, 63.8, 63.65, 63.5, 63.45, 63.3, 63.35, 63.2, 63.25, 63, 63.05, 63.25, 63.25, 63.25, 63.3, 63.15, 63.1, 63.3, 63.2, 63.3, 63.15, 63.15, 63.1, 63.15, 63.15, 63.2, 63, 63, 63.05, 63.05, 63.05, 63.05, 63.15, 63, 63.2, 63, 63.15]
scei = [45.05, 51.1, 56, 59.55, 62.05, 63.15, 62.95, 64.5, 64.4, 65.4, 65.7, 65.7, 65.7, 65.25, 65.25, 66.55, 65.8, 66.6, 66.55, 64.75, 65.45, 65.35, 64.65, 65.25, 65.45, 66.35, 65.8, 65.25, 65.45, 66.45, 66.5, 66.8, 66.75, 66.75, 66, 66.9, 66.4, 66.5, 66.15, 66.45, 66.55, 66.25, 66.35, 66.9, 66.85, 66.7, 66.35, 65.55, 66.2, 66.5]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, scei, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, local_train, label="Local Training", linestyle='--', alpha=0.5)
axes.plot(x, apfl, label="APFL", linestyle='--', alpha=0.5)
axes.plot(x, fed_avg, label="FedAvg", linestyle='--', alpha=0.5)
# axes.plot(x, scei, label="SCEI with negotiated α", linewidth=3, color='#1f77b4')

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.ylim(30)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
