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
fed_server = [7.45, 7.7, 5.86, 7.11, 7.52, 7.52, 7.42, 7.55, 7.49, 6.0, 7.81, 7.68, 7.49, 7.38, 7.17, 7.64, 7.56, 5.9, 4.85, 6.55, 6.68, 6.67, 6.29, 6.82, 6.34, 5.94, 6.36, 6.37, 6.15, 5.89, 6.11, 6.3, 6.34, 7.78, 7.35, 6.15, 7.92, 5.86, 6.1, 6.19, 6.64, 5.86, 6.09, 6.2, 4.78, 5.81, 7.68, 5.52, 6.53, 6.94]
main_fed_localA = [0.01, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
main_fed = [0.02, 0.13, 0.1, 0.08, 0.09, 0.09, 0.09, 0.09, 0.11, 0.11, 0.11, 0.08, 0.1, 0.08, 0.09, 0.09, 0.05, 0.06, 0.09, 0.06, 0.07, 0.08, 0.11, 0.06, 0.09, 0.09, 0.08, 0.05, 0.11, 0.13, 0.09, 0.06, 0.08, 0.1, 0.06, 0.07, 0.11, 0.09, 0.07, 0.07, 0.07, 0.11, 0.11, 0.11, 0.11, 0.09, 0.07, 0.09, 0.08, 0.09]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_fed, label="FedAvg", alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Communication Time Consumption (s)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
