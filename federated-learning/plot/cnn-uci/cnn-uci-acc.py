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

fed_server = [95.25, 94.8, 96.03, 96.03, 95.93, 96.12, 96.3, 95.93, 96.72, 96.12, 96.5, 96.57, 96.73, 96.73, 96.78, 96.67, 96.88, 96.9, 96.77, 96.95, 96.57, 97.02, 96.85, 96.93, 96.4, 97.1, 96.88, 96.92, 97.13, 96.98, 96.88, 97.08, 97.18, 96.95, 97.1, 96.98, 96.95, 97.33, 97.03, 96.8, 96.5, 96.67, 96.6, 96.77, 96.73, 96.97, 96.82, 96.97, 96.83, 96.77]
main_fed_localA = [33.6, 91.17, 96.55, 96.68, 96.58, 96.62, 96.7, 96.7, 96.68, 96.85, 96.68, 97.15, 96.8, 96.85, 96.92, 96.77, 97.03, 96.92, 97.05, 96.93, 96.92, 96.95, 96.92, 97.0, 96.73, 96.97, 97.1, 96.93, 96.93, 96.98, 97.03, 97.02, 96.8, 96.88, 96.93, 97.13, 97.1, 97.02, 97.02, 97.18, 97.23, 97.13, 96.93, 97.15, 97.08, 97.18, 96.8, 97.33, 97.35, 97.25]
main_fed = [68.43, 73.88, 82.73, 87.3, 89.53, 89.88, 90.65, 91.32, 91.45, 91.35, 91.33, 91.43, 91.53, 91.92, 91.87, 92.0, 91.9, 92.08, 91.98, 91.85, 92.38, 92.35, 92.05, 92.0, 91.9, 91.95, 91.83, 92.05, 92.3, 92.15, 92.32, 91.87, 92.27, 92.2, 92.08, 92.13, 92.03, 92.03, 91.98, 92.07, 91.95, 92.13, 92.15, 92.02, 92.15, 92.08, 92.18, 92.18, 91.87, 92.05]
main_nn = [18.22, 96.32, 96.85, 97.07, 97.1, 96.72, 96.95, 96.77, 96.75, 96.93, 96.93, 96.88, 97.03, 97.23, 97.05, 97.08, 97.18, 96.93, 96.82, 97.08, 97.0, 97.18, 97.18, 96.83, 97.0, 96.8, 97.02, 97.07, 96.95, 97.0, 96.93, 97.0, 97.05, 96.93, 97.08, 96.93, 96.75, 96.82, 96.95, 96.63, 96.9, 96.85, 96.92, 96.78, 96.97, 96.87, 96.88, 96.72, 96.9, 96.8]

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
plt.ylim(90, 98)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
