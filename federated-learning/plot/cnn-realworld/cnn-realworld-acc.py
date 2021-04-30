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

fed_server = [86.33, 88.33, 89.23, 90.27, 89.6, 90.17, 89.43, 90.43, 90.4, 91.57, 91.03, 89.53, 91.43, 90.77, 90.27, 91.4, 91.4, 90.93, 91.53, 91.33, 91.33, 91.83, 91.2, 91.9, 91.53, 91.67, 92.1, 91.97, 91.97, 92.17, 92.0, 91.87, 92.17, 92.2, 92.03, 92.1, 92.1, 92.03, 91.63, 92.27, 92.2, 91.5, 92.43, 91.8, 92.6, 92.1, 91.97, 92.07, 92.47, 91.8]
main_fed_localA = [11.9, 79.83, 87.9, 89.67, 90.1, 90.57, 91.4, 91.07, 90.6, 89.73, 90.77, 91.07, 91.13, 90.23, 91.1, 91.47, 91.47, 91.43, 90.87, 91.2, 90.53, 91.0, 91.1, 90.93, 91.2, 91.4, 91.1, 90.9, 91.1, 91.17, 91.33, 91.0, 91.07, 91.57, 91.6, 91.43, 91.03, 91.17, 91.13, 90.7, 90.77, 91.13, 91.47, 91.67, 91.47, 90.97, 91.77, 91.33, 91.47, 91.1]
main_fed = [49.73, 54.73, 58.2, 60.53, 61.83, 63.6, 65.77, 67.63, 67.33, 69.47, 68.47, 70.33, 71.3, 70.57, 71.43, 71.67, 71.37, 70.87, 71.23, 73.03, 72.57, 73.63, 73.57, 74.13, 74.47, 72.67, 73.87, 75.13, 74.77, 74.17, 75.73, 75.97, 76.43, 75.17, 75.87, 74.57, 75.27, 75.03, 76.53, 76.67, 76.47, 76.27, 75.07, 76.73, 74.53, 77.27, 75.97, 76.57, 76.67, 76.7]
main_nn = [11.46, 88.5, 90.46, 90.54, 90.92, 91.17, 91.37, 91.37, 91.62, 91.21, 91.21, 91.25, 91.54, 91.54, 91.87, 91.58, 90.75, 91.17, 91.67, 92.17, 91.92, 91.29, 91.75, 92.04, 92.04, 91.58, 91.54, 91.67, 91.67, 92.0, 91.58, 91.62, 91.71, 91.62, 91.67, 91.79, 91.79, 91.58, 91.5, 91.17, 91.25, 91.58, 91.75, 92.08, 91.83, 91.79, 91.62, 91.17, 91.62, 91.87]

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
plt.ylim(70)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
