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
local_train = [6.45, 93.3, 94.45, 94.95, 94.75, 94.8, 94.55, 94.9, 94.9, 94.9, 95.15, 94.95, 94.85, 95.1, 94.85, 94.95, 94.85, 95.15, 95, 95.05, 94.9, 94.85, 94.8, 94.85, 94.7, 95, 94.9, 94.55, 94.75, 94.85, 94.8, 94.85, 94.7, 94.8, 94.75, 94.8, 94.8, 94.95, 94.85, 94.7, 94.85, 94.7, 94.85, 94.8, 94.8, 94.7, 94.8, 94.55, 94.85, 94.9]
fed_avg = [49.4, 65.55, 71.2, 75.25, 77.05, 78.95, 79.95, 80.7, 81.5, 81.95, 83.2, 83.45, 84.3, 84.7, 85.2, 85.5, 85.8, 86.1, 86.5, 86.8, 87.2, 87.4, 87.7, 87.6, 88.05, 87.95, 88.2, 88.45, 88.8, 89, 88.85, 89.05, 89.35, 89.45, 89.35, 89.6, 89.85, 90.1, 90.5, 90.35, 90.4, 90.35, 90.55, 90.7, 90.9, 90.65, 91, 91.5, 91.5, 91.45]
apfl = [6.45, 80.2, 94.15, 94.55, 94.65, 94.75, 94.8, 95.1, 94.75, 95, 95.05, 93.2, 95.35, 95.4, 95.2, 95.15, 94.95, 95.25, 95.35, 95.3, 95.2, 95.35, 95.35, 95.3, 95.25, 94.95, 95.15, 95.2, 95.15, 95.35, 95.3, 95.1, 95.25, 95.45, 95.3, 95.35, 95.1, 95.15, 95.15, 95.35, 95.25, 95.25, 95.35, 95.5, 95.2, 95.3, 95.55, 95.2, 95.4, 95.5]
scei = [92.5, 94.3, 94.6, 94.8, 94.95, 95.15, 94.85, 94.85, 95.15, 94.9, 94.8, 95.1, 95.15, 95.1, 94.95, 95.2, 95.4, 95.25, 95.45, 95.5, 95.35, 95.45, 95.3, 95.5, 95.45, 95.55, 95.45, 95.5, 95.6, 95.55, 95.3, 95.4, 95.3, 95.75, 95.6, 95.55, 95.7, 95.65, 95.5, 95.65, 95.5, 95.7, 95.6, 95.65, 95.55, 95.75, 95.55, 95.85, 96, 95.95]

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
plt.ylim(85, 97)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
