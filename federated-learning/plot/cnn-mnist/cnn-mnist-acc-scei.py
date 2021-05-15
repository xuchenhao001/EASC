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
fed_server = [96.87, 98.0, 98.2, 97.67, 97.87, 98.27, 98.13, 98.2, 98.13, 98.0, 98.4, 98.33, 98.4, 98.4, 98.4, 98.4, 98.6, 98.87, 98.67, 98.6, 98.47, 98.93, 98.93, 98.8, 98.67, 98.87, 98.93, 98.93, 98.93, 99.13, 98.8, 98.93, 98.8, 99.0, 98.73, 98.8, 98.8, 98.8, 98.53, 98.73, 99.07, 98.8, 99.13, 98.8, 99.0, 99.0, 98.8, 98.6, 99.2, 98.8]
fed_server_alpha_025 = [91.0, 92.6, 92.87, 93.33, 94.4, 94.07, 95.07, 96.07, 95.73, 96.27, 95.73, 96.2, 96.73, 97.13, 96.8, 97.13, 97.33, 97.27, 97.53, 97.67, 97.87, 97.93, 97.93, 98.07, 97.87, 97.87, 97.87, 98.53, 97.67, 98.0, 97.93, 98.13, 98.0, 98.27, 97.93, 98.2, 98.33, 98.33, 98.33, 98.2, 98.4, 98.33, 98.27, 98.4, 98.13, 98.07, 98.53, 98.33, 98.27, 98.27]
fed_server_alpha_050 = [94.8, 95.33, 95.67, 96.8, 96.73, 96.93, 96.53, 96.87, 96.8, 97.2, 96.93, 97.4, 97.13, 97.33, 97.53, 97.53, 97.47, 97.33, 97.73, 97.6, 97.67, 97.47, 98.2, 97.6, 97.53, 98.13, 98.0, 97.93, 98.07, 98.07, 97.93, 97.87, 98.2, 98.0, 98.0, 98.2, 98.0, 98.0, 97.87, 98.2, 97.93, 97.73, 98.2, 98.0, 98.0, 98.13, 98.13, 97.93, 98.13, 97.93]
fed_server_alpha_075 = [95.73, 97.0, 97.47, 97.33, 97.4, 97.93, 97.67, 97.87, 97.8, 97.73, 98.0, 98.0, 97.93, 98.2, 98.13, 98.2, 98.27, 98.4, 98.13, 98.2, 98.33, 98.33, 98.6, 98.6, 98.53, 98.67, 98.6, 98.73, 98.33, 98.47, 98.4, 98.67, 98.67, 98.6, 98.73, 98.67, 98.6, 98.8, 98.8, 98.87, 98.93, 99.07, 98.87, 98.73, 98.87, 98.87, 98.6, 99.0, 98.93, 99.0]
main_fed = [59.8, 72.07, 81.4, 84.53, 86.0, 87.87, 88.87, 88.33, 89.13, 89.67, 90.13, 90.4, 91.47, 91.13, 91.4, 91.27, 91.87, 91.67, 92.93, 92.67, 92.67, 92.93, 92.73, 92.87, 93.67, 93.93, 93.93, 94.33, 94.47, 94.13, 94.47, 94.13, 94.13, 94.07, 94.73, 94.47, 94.8, 95.13, 95.13, 94.87, 95.33, 95.47, 95.33, 95.4, 95.33, 95.27, 95.73, 95.8, 95.6, 95.8]
main_nn = [5.33, 95.33, 97.2, 97.8, 98.33, 98.13, 97.93, 98.47, 98.27, 98.67, 98.6, 98.4, 98.73, 98.47, 98.53, 98.53, 98.67, 98.67, 98.67, 98.6, 98.6, 98.6, 98.67, 98.33, 98.87, 98.8, 98.8, 98.6, 98.73, 98.67, 98.67, 98.73, 98.6, 98.93, 98.73, 98.73, 98.67, 98.6, 98.6, 98.33, 98.73, 98.53, 98.4, 98.8, 98.67, 98.67, 98.8, 98.8, 98.87, 98.87]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

axes.plot(x, fed_server, label="negotiated α (0.5-0.8)", linewidth=3)
axes.plot(x, main_fed, label="α=0.0 (i.e. FedAvg)", linestyle='--', alpha=0.5)
axes.plot(x, fed_server_alpha_025, label="α=0.25", linestyle='--', alpha=0.5)
axes.plot(x, fed_server_alpha_050, label="α=0.5", linestyle='--', alpha=0.5)
axes.plot(x, fed_server_alpha_075, label="α=0.75", linestyle='--', alpha=0.5)
axes.plot(x, main_nn, label="α=1.0 (i.e. Local Training)", linestyle='--', alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
