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

fed_avg = [4.35, 2.40, 2.30, 2.44, 2.37, 2.36, 2.41, 2.30, 2.28, 2.33, 2.42, 2.54, 2.29, 2.33, 2.35, 2.31, 2.37, 2.49, 2.37, 2.40, 2.49, 2.37, 2.39, 2.52, 2.38, 2.31, 2.47, 2.37, 2.43, 2.42, 2.40, 2.44, 2.54, 2.34, 2.44, 2.27, 2.34, 2.57, 2.39, 2.37, 2.42, 2.32, 2.34, 2.51, 2.36, 2.36, 2.30, 2.47, 2.36, 1.47]
apfl = [0.07, 18.56, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 21.27, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 21.16, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 21.38, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 20.72, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
scei = [11.09, 10.51, 11.03, 10.88, 12.19, 11.49, 12.03, 11.22, 11.17, 10.73, 11.18, 12.24, 12.50, 11.97, 11.26, 11.87, 12.65, 11.39, 12.13, 13.01, 13.53, 12.11, 11.52, 12.20, 13.22, 12.88, 12.75, 12.90, 12.72, 12.52, 12.38, 13.36, 13.54, 13.76, 13.95, 12.26, 11.79, 12.53, 11.51, 13.96, 14.21, 13.52, 13.97, 14.98, 12.53, 13.76, 13.99, 13.83, 13.52, 14.67]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, scei, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, fed_avg, label="FedAvg", linestyle='--', alpha=0.5)
axes.plot(x, apfl, label="APFL", linestyle='--', alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Communication Time Consumption (s)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
