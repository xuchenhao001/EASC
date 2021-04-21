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
fed_avg = [4.20, 2.27, 2.28, 2.34, 2.30, 2.33, 2.44, 2.23, 2.28, 2.25, 2.30, 2.43, 2.24, 2.24, 2.24, 2.30, 2.26, 2.25, 2.25, 2.25, 2.23, 2.24, 2.23, 2.28, 2.21, 2.26, 2.27, 2.28, 2.26, 2.23, 2.75, 2.39, 2.24, 2.40, 2.36, 2.23, 2.26, 2.24, 2.24, 2.25, 2.22, 2.27, 2.23, 2.29, 2.33, 2.24, 2.24, 2.40, 2.27, 1.64]
apfl = [0.07, 19.90, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 34.10, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 34.81, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 35.44, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 31.79, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
scei = [14.15, 13.28, 13.45, 13.40, 12.89, 14.08, 13.76, 14.06, 14.06, 14.60, 14.46, 14.58, 12.91, 13.49, 13.34, 13.72, 14.58, 14.43, 18.87, 16.95, 15.52, 14.59, 16.33, 15.19, 15.49, 20.04, 16.14, 14.70, 15.40, 16.33, 16.03, 20.24, 19.94, 20.67, 18.40, 19.32, 16.64, 16.27, 19.63, 19.53, 20.80, 19.69, 16.84, 18.93, 18.76, 18.69, 19.08, 16.84, 17.03, 17.54]

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
