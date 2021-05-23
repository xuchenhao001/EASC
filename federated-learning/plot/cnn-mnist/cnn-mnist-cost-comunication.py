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

fed_server = [4.6, 3.89, 3.69, 4.17, 3.85, 4.0, 3.85, 4.13, 4.76, 5.9, 5.87, 5.78, 4.02, 4.64, 4.56, 3.93, 4.92, 3.97, 3.95, 3.95, 4.62, 6.4, 4.07, 4.17, 4.04, 5.55, 4.09, 6.79, 4.45, 7.13, 4.56, 4.32, 3.89, 4.9, 4.24, 5.76, 4.07, 4.26, 4.04, 4.27, 4.03, 5.09, 5.16, 3.98, 5.88, 3.93, 4.06, 4.02, 4.24, 4.61]
main_fed_localA = [0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
main_fed = [0.01, 0.06, 0.04, 0.06, 0.01, 0.03, 0.03, 0.06, 0.03, 0.03, 0.04, 0.03, 0.02, 0.03, 0.03, 0.04, 0.06, 0.02, 0.04, 0.05, 0.04, 0.03, 0.03, 0.01, 0.05, 0.03, 0.05, 0.03, 0.02, 0.06, 0.03, 0.02, 0.04, 0.03, 0.04, 0.02, 0.02, 0.04, 0.02, 0.03, 0.03, 0.02, 0.03, 0.03, 0.03, 0.02, 0.02, 0.04, 0.02, 0.03]

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
