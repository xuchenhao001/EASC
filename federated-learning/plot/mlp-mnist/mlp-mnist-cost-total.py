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

fed_server = [19.16, 18.87, 18.67, 19.0, 18.75, 18.9, 18.96, 18.85, 18.87, 17.19, 18.76, 18.9, 18.75, 18.91, 18.92, 18.86, 18.88, 17.06, 16.69, 17.42, 17.98, 17.58, 17.42, 18.09, 17.53, 17.28, 17.53, 17.45, 17.44, 17.42, 17.24, 17.19, 17.48, 19.19, 19.15, 17.17, 19.33, 17.09, 17.36, 17.38, 17.59, 17.32, 17.16, 17.31, 17.58, 17.23, 19.1, 17.03, 17.42, 18.21]
main_fed_localA = [0.91, 21.0, 0.96, 0.97, 0.87, 0.85, 0.84, 0.88, 0.87, 0.84, 0.83, 21.39, 0.88, 0.83, 0.86, 0.86, 0.85, 0.86, 0.9, 0.88, 0.82, 19.96, 0.89, 0.85, 0.84, 0.87, 0.88, 0.87, 0.85, 0.9, 0.83, 19.7, 0.86, 0.84, 0.86, 0.86, 0.86, 0.84, 0.91, 0.86, 0.84, 19.55, 0.86, 0.88, 0.85, 0.81, 0.86, 0.88, 0.86, 0.84]
main_fed = [4.9, 1.67, 1.67, 1.62, 1.62, 1.7, 1.64, 1.65, 1.64, 1.64, 1.64, 1.59, 1.65, 1.59, 1.64, 1.61, 1.6, 1.62, 1.59, 1.65, 1.64, 1.6, 1.65, 1.62, 1.65, 1.65, 1.63, 1.6, 1.66, 1.64, 1.65, 1.66, 1.65, 1.64, 1.6, 1.59, 1.64, 1.67, 1.6, 1.59, 1.59, 1.65, 1.65, 1.64, 1.63, 1.66, 1.61, 1.65, 1.59, 1.72]
main_nn = [0.43, 0.41, 0.42, 0.43, 0.44, 0.43, 0.42, 0.42, 0.42, 0.41, 0.42, 0.42, 0.43, 0.43, 0.46, 0.42, 0.43, 0.43, 0.43, 0.45, 0.44, 0.44, 0.43, 0.44, 0.43, 0.43, 0.43, 0.43, 0.43, 0.46, 0.45, 0.48, 0.46, 0.44, 0.44, 0.44, 0.41, 0.44, 0.42, 0.4, 0.4, 0.4, 0.4, 0.41, 0.4, 0.43, 0.42, 0.42, 0.42, 0.41]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_nn, label="Local Training", linestyle='--', alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", linestyle='--', alpha=0.5)
axes.plot(x, main_fed, label="FedAvg", linestyle='--', alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Total Time Consumption (s)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
