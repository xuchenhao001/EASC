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
fed_server_alpha_025 = [73.27, 78.72, 83.48, 83.72, 88.08, 89.23, 90.15, 91.03, 90.67, 91.47, 91.9, 91.88, 92.38, 92.47, 92.42, 92.72, 92.85, 92.88, 93.05, 93.15, 93.27, 93.3, 93.38, 93.55, 93.28, 93.63, 93.48, 93.37, 93.6, 93.5, 93.72, 93.63, 93.63, 93.8, 93.58, 93.93, 93.88, 94.05, 94.05, 93.72, 93.73, 93.98, 94.12, 93.8, 93.9, 94.05, 94.07, 94.13, 93.85, 94.12]
fed_server_alpha_050 = [90.75, 91.52, 91.4, 91.77, 92.13, 92.7, 92.82, 92.9, 93.08, 93.12, 93.08, 93.52, 93.63, 93.82, 93.45, 93.53, 93.4, 93.78, 93.6, 93.55, 93.98, 93.67, 93.75, 93.93, 93.78, 93.77, 94.07, 93.63, 94.23, 94.18, 94.45, 94.28, 94.5, 93.87, 94.73, 94.22, 94.1, 94.25, 94.42, 94.58, 94.55, 94.25, 94.55, 94.1, 94.07, 94.38, 94.08, 94.03, 94.48, 94.27]
fed_server_alpha_075 = [93.78, 93.75, 93.78, 93.8, 93.88, 93.8, 93.33, 93.95, 94.45, 93.95, 94.1, 94.67, 94.5, 94.47, 94.6, 94.28, 94.88, 94.63, 95.05, 94.8, 94.83, 94.43, 95.37, 94.57, 94.95, 95.4, 94.92, 95.2, 94.92, 95.25, 95.13, 94.45, 95.23, 94.95, 95.17, 95.25, 95.1, 94.87, 94.73, 95.18, 95.53, 94.83, 95.05, 95.3, 94.55, 95.38, 95.67, 95.43, 95.28, 95.23]
main_fed = [68.43, 73.88, 82.73, 87.3, 89.53, 89.88, 90.65, 91.32, 91.45, 91.35, 91.33, 91.43, 91.53, 91.92, 91.87, 92.0, 91.9, 92.08, 91.98, 91.85, 92.38, 92.35, 92.05, 92.0, 91.9, 91.95, 91.83, 92.05, 92.3, 92.15, 92.32, 91.87, 92.27, 92.2, 92.08, 92.13, 92.03, 92.03, 91.98, 92.07, 91.95, 92.13, 92.15, 92.02, 92.15, 92.08, 92.18, 92.18, 91.87, 92.05]
main_nn = [18.22, 96.32, 96.85, 97.07, 97.1, 96.72, 96.95, 96.77, 96.75, 96.93, 96.93, 96.88, 97.03, 97.23, 97.05, 97.08, 97.18, 96.93, 96.82, 97.08, 97.0, 97.18, 97.18, 96.83, 97.0, 96.8, 97.02, 97.07, 96.95, 97.0, 96.93, 97.0, 97.05, 96.93, 97.08, 96.93, 96.75, 96.82, 96.95, 96.63, 96.9, 96.85, 96.92, 96.78, 96.97, 96.87, 96.88, 96.72, 96.9, 96.8]

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
plt.tight_layout()
plt.ylim(80, 98)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
