# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import cycler

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

fed_server = [94.53, 95.33, 95.87, 95.53, 95.6, 95.6, 95.33, 95.87, 95.87, 95.6, 95.87, 95.6, 95.73, 95.33, 95.6, 95.53, 95.93, 96.07, 95.93, 95.8, 95.87, 95.8, 95.73, 95.73, 95.6, 95.67, 96.0, 96.27, 95.8, 96.07, 96.0, 96.0, 96.0, 95.8, 95.8, 95.93, 96.13, 95.73, 96.07, 95.93, 96.0, 95.87, 96.0, 95.87, 96.2, 96.27, 96.07, 96.07, 96.33, 96.47]
main_fed_localA = [8.0, 92.47, 95.8, 96.27, 96.13, 96.0, 96.2, 96.07, 96.0, 96.27, 96.2, 95.53, 96.27, 96.33, 96.4, 96.27, 96.27, 96.47, 96.2, 96.27, 96.07, 96.2, 96.33, 95.93, 96.13, 96.13, 96.13, 96.0, 96.2, 96.07, 96.07, 96.27, 96.13, 96.07, 96.2, 96.27, 96.47, 96.47, 96.33, 96.2, 96.33, 96.4, 96.13, 96.0, 96.27, 96.13, 96.27, 96.2, 96.33, 96.27]
main_fed = [47.67, 63.87, 72.33, 76.93, 79.53, 81.67, 82.73, 84.27, 85.0, 85.53, 86.13, 86.27, 86.4, 86.73, 86.6, 87.27, 87.73, 87.73, 87.93, 88.2, 88.73, 88.47, 88.73, 89.07, 89.13, 89.27, 89.47, 89.27, 89.4, 89.47, 89.4, 89.87, 90.07, 89.93, 90.0, 89.8, 90.27, 90.0, 90.33, 90.07, 90.53, 90.33, 90.47, 90.73, 90.6, 90.67, 90.67, 90.93, 90.73, 90.93]
main_nn = [10.0, 96.07, 96.93, 97.07, 96.93, 97.13, 96.93, 97.13, 97.07, 97.13, 97.0, 97.13, 97.13, 96.93, 96.93, 97.07, 97.13, 97.07, 97.0, 96.93, 97.0, 97.0, 97.13, 97.13, 97.13, 97.0, 97.0, 97.07, 97.0, 97.07, 97.07, 97.13, 97.13, 97.13, 97.0, 97.07, 97.0, 97.07, 97.07, 97.13, 97.0, 97.07, 97.07, 97.07, 97.07, 97.13, 97.2, 97.13, 97.0, 97.2]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_nn, label="Local Training", alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", alpha=0.5)
axes.plot(x, main_fed, label="FedAvg", alpha=0.5)
# axes.plot(x, scei, label="SCEI with negotiated α", linewidth=3, color='#1f77b4')


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(85, 98)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
