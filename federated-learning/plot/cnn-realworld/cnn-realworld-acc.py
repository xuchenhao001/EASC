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

fed_server = [84.53, 86.03, 87.4, 88.4, 87.93, 88.77, 88.67, 88.33, 88.63, 89.4, 89.5, 89.37, 89.47, 89.5, 88.73, 89.47, 89.37, 90.07, 89.57, 90.23, 89.83, 90.5, 90.3, 90.47, 90.37, 90.17, 90.17, 90.23, 90.03, 90.67, 90.3, 90.73, 90.6, 90.27, 90.47, 90.9, 90.9, 90.67, 90.4, 90.43, 90.5, 90.43, 90.43, 90.93, 90.73, 91.23, 91.73, 91.13, 91.07, 90.83]
main_fed_localA = [11.67, 66.17, 86.03, 87.13, 87.17, 87.83, 87.67, 87.33, 88.33, 87.83, 87.43, 87.7, 88.5, 87.63, 87.97, 88.23, 88.5, 88.0, 88.03, 87.83, 88.63, 88.43, 87.57, 88.3, 88.63, 88.8, 89.37, 89.03, 89.2, 88.37, 88.7, 88.63, 89.5, 88.9, 88.73, 89.17, 89.37, 88.47, 89.03, 89.0, 89.13, 88.57, 89.53, 89.6, 89.1, 88.93, 89.63, 88.97, 89.53, 89.6]
main_fed = [55.4, 56.13, 57.47, 58.83, 63.53, 65.83, 68.53, 70.87, 68.77, 70.3, 71.17, 71.53, 70.8, 71.3, 72.47, 73.67, 74.03, 73.3, 73.27, 73.13, 73.87, 74.33, 74.2, 74.67, 73.77, 74.53, 73.77, 75.3, 74.23, 74.5, 74.3, 75.53, 74.93, 75.57, 75.53, 75.2, 75.6, 74.93, 75.8, 76.0, 75.13, 75.73, 76.0, 76.5, 75.73, 76.6, 75.77, 76.83, 75.73, 75.9]
main_nn = [10.27, 81.23, 83.5, 84.6, 85.6, 85.37, 86.03, 87.13, 86.53, 87.07, 87.13, 87.57, 87.4, 87.77, 87.77, 87.77, 87.7, 87.63, 87.6, 87.27, 88.33, 87.63, 87.67, 88.33, 87.43, 87.7, 88.23, 88.13, 87.8, 87.8, 87.83, 88.0, 87.7, 88.5, 88.13, 88.53, 87.93, 88.77, 88.13, 88.73, 87.97, 88.3, 88.2, 87.93, 88.43, 88.23, 87.93, 87.9, 87.9, 87.93]

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

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(70)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
