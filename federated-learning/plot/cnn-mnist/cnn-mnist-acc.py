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
fed_server = [96.87, 98.0, 98.2, 97.67, 97.87, 98.27, 98.13, 98.2, 98.13, 98.0, 98.4, 98.33, 98.4, 98.4, 98.4, 98.4, 98.6, 98.87, 98.67, 98.6, 98.47, 98.93, 98.93, 98.8, 98.67, 98.87, 98.93, 98.93, 98.93, 99.13, 98.8, 98.93, 98.8, 99.0, 98.73, 98.8, 98.8, 98.8, 98.53, 98.73, 99.07, 98.8, 99.13, 98.8, 99.0, 99.0, 98.8, 98.6, 99.2, 98.8]
main_fed_localA = [22.27, 82.2, 98.0, 98.6, 98.73, 98.6, 98.87, 99.0, 98.87, 98.87, 99.07, 98.8, 98.87, 98.87, 99.0, 98.87, 98.87, 98.8, 98.8, 98.93, 98.93, 98.93, 99.07, 98.93, 98.93, 99.0, 99.0, 99.2, 99.13, 98.93, 99.0, 99.07, 99.13, 99.0, 99.0, 99.13, 99.07, 99.2, 99.0, 99.07, 98.87, 99.07, 99.2, 99.2, 99.0, 99.07, 99.13, 98.87, 99.0, 98.93]
main_fed = [59.8, 72.07, 81.4, 84.53, 86.0, 87.87, 88.87, 88.33, 89.13, 89.67, 90.13, 90.4, 91.47, 91.13, 91.4, 91.27, 91.87, 91.67, 92.93, 92.67, 92.67, 92.93, 92.73, 92.87, 93.67, 93.93, 93.93, 94.33, 94.47, 94.13, 94.47, 94.13, 94.13, 94.07, 94.73, 94.47, 94.8, 95.13, 95.13, 94.87, 95.33, 95.47, 95.33, 95.4, 95.33, 95.27, 95.73, 95.8, 95.6, 95.8]
main_nn = [5.33, 95.33, 97.2, 97.8, 98.33, 98.13, 97.93, 98.47, 98.27, 98.67, 98.6, 98.4, 98.73, 98.47, 98.53, 98.53, 98.67, 98.67, 98.67, 98.6, 98.6, 98.6, 98.67, 98.33, 98.87, 98.8, 98.8, 98.6, 98.73, 98.67, 98.67, 98.73, 98.6, 98.93, 98.73, 98.73, 98.67, 98.6, 98.6, 98.33, 98.73, 98.53, 98.4, 98.8, 98.67, 98.67, 98.8, 98.8, 98.87, 98.87]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_nn, label="Local Training", linestyle='--', alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", linestyle='--', alpha=0.5)
axes.plot(x, main_fed, label="FedAvg", linestyle='--', alpha=0.5)
# axes.plot(x, scei, label="SCEI with negotiated α", linewidth=3, color='#1f77b4')


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
