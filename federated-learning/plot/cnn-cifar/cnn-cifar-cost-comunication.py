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
fed_server = [4.67, 4.12, 4.06, 3.95, 3.84, 3.83, 4.08, 3.8, 3.94, 3.91, 3.99, 4.24, 3.9, 4.02, 3.92, 3.75, 3.88, 3.81, 3.9, 3.86, 3.71, 3.96, 3.82, 3.99, 3.85, 3.81, 5.3, 4.0, 5.28, 5.83, 5.63, 5.44, 5.76, 4.07, 4.34, 5.54, 4.52, 3.94, 4.02, 4.27, 3.83, 3.75, 3.65, 5.27, 4.51, 4.13, 4.6, 5.39, 3.98, 3.92]
main_fed_localA = [0.01, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
main_fed = [0.01, 0.13, 0.03, 0.07, 0.1, 0.09, 0.06, 0.1, 0.09, 0.11, 0.1, 0.09, 0.06, 0.11, 0.11, 0.04, 0.14, 0.1, 0.07, 0.03, 0.02, 0.1, 0.08, 0.07, 0.1, 0.07, 0.06, 0.11, 0.05, 0.12, 0.09, 0.05, 0.05, 0.11, 0.13, 0.12, 0.12, 0.05, 0.08, 0.12, 0.08, 0.11, 0.09, 0.12, 0.09, 0.09, 0.13, 0.09, 0.04, 0.08]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, fed_server, label="SCEI with negotiated α", linewidth=3)
axes.plot(x, main_fed, label="FedAvg", linestyle='--', alpha=0.5)
axes.plot(x, main_fed_localA, label="APFL", linestyle='--', alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Communication Time Consumption (s)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
