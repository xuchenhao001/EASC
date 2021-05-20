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
fed_server = [54.87, 62.6, 66.07, 69.2, 73.53, 72.07, 72.4, 73.67, 73.33, 73.0, 73.8, 74.6, 74.53, 74.0, 74.0, 74.53, 74.13, 74.8, 74.53, 74.53, 74.8, 74.87, 74.87, 75.0, 74.33, 75.13, 74.4, 74.47, 74.8, 74.53, 75.2, 74.53, 75.2, 75.0, 75.87, 75.47, 75.33, 75.93, 76.13, 76.0, 75.93, 75.87, 75.67, 74.67, 74.67, 75.53, 75.87, 76.6, 76.27, 75.73]
main_fed_localA = [10.0, 39.87, 61.07, 67.27, 68.27, 70.4, 69.67, 70.27, 68.47, 69.67, 69.67, 66.87, 67.73, 69.53, 70.93, 71.27, 71.67, 71.8, 71.2, 71.07, 71.4, 71.13, 71.07, 71.2, 71.33, 71.13, 71.0, 71.2, 71.0, 71.13, 70.93, 70.93, 70.8, 70.67, 70.87, 71.07, 71.0, 71.07, 70.87, 71.0, 70.93, 71.13, 70.93, 70.93, 70.93, 70.87, 71.0, 70.93, 70.87, 70.87]
main_fed = [23.33, 28.93, 32.53, 32.87, 34.87, 36.8, 37.6, 37.67, 39.07, 39.33, 40.0, 40.27, 40.27, 40.67, 41.8, 41.93, 41.67, 43.0, 42.93, 42.53, 42.6, 43.47, 43.13, 43.73, 43.6, 43.73, 44.13, 44.6, 44.2, 44.27, 43.67, 44.4, 44.0, 43.33, 42.47, 43.6, 43.47, 43.27, 42.67, 43.33, 43.8, 43.13, 42.8, 42.8, 42.53, 41.87, 43.13, 43.8, 43.8, 43.27]
main_nn = [13.27, 50.53, 59.07, 63.13, 64.53, 67.53, 68.2, 67.8, 69.73, 69.87, 69.93, 69.87, 69.67, 69.27, 69.53, 69.2, 69.47, 69.13, 69.4, 69.47, 69.2, 69.6, 69.73, 69.53, 69.4, 69.4, 69.6, 69.67, 69.53, 69.67, 69.6, 69.6, 69.67, 69.67, 69.6, 69.6, 69.67, 69.6, 69.67, 69.6, 69.6, 69.67, 69.67, 69.67, 69.6, 69.67, 69.67, 69.67, 69.67, 69.73]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_nn, label="Local Training", linestyle='--', alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", linestyle='--', alpha=0.5)
axes.plot(x, main_fed, label="FedAvg", linestyle='--', alpha=0.5)

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.ylim(40)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
