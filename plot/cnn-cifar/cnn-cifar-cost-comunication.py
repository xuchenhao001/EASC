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
fed_avg = [6.68, 3.98, 4.07, 4.03, 3.93, 4.19, 4.22, 4.02, 4.04, 3.90, 3.88, 3.94, 4.06, 4.04, 4.00, 3.93, 3.80, 3.85, 4.10, 3.96, 4.18, 3.91, 3.98, 3.90, 3.92, 4.16, 4.04, 4.00, 3.94, 3.79, 4.05, 3.88, 4.00, 3.89, 3.93, 4.12, 3.90, 3.97, 3.83, 3.78, 3.90, 3.97, 3.94, 3.94, 3.86, 3.94, 4.23, 4.14, 4.02, 2.51]
apfl = [0.00, 20.33, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 30.17, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 29.26, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 31.53, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 30.96, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
scei = [14.42, 14.42, 14.26, 18.10, 14.73, 14.60, 14.60, 14.36, 15.27, 15.03, 14.37, 15.43, 15.14, 14.70, 15.97, 17.22, 15.69, 15.37, 19.67, 16.21, 16.82, 15.77, 16.50, 16.27, 15.92, 16.36, 16.59, 16.69, 16.37, 16.90, 17.60, 15.90, 16.80, 21.80, 20.02, 18.23, 17.15, 19.83, 17.27, 17.80, 17.55, 17.02, 16.60, 18.06, 18.54, 17.42, 18.30, 21.30, 20.53, 19.38]

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
