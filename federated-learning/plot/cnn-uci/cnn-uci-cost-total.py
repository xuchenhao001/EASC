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

fed_server = [233.13, 211.78, 205.49, 215.43, 205.66, 187.28, 205.18, 207.46, 207.25, 213.7, 210.26, 207.27, 210.27, 207.8, 221.86, 221.59, 207.64, 213.44, 209.41, 215.06, 206.39, 190.83, 186.1, 213.68, 216.24, 196.88, 210.41, 214.96, 212.48, 215.98, 213.59, 213.26, 213.03, 226.18, 209.14, 216.02, 206.08, 204.42, 204.56, 210.42, 225.32, 213.23, 222.57, 216.85, 207.44, 216.46, 199.22, 212.12, 204.76, 209.82]
main_fed_localA = [40.49, 278.87, 27.07, 26.34, 24.91, 22.39, 21.96, 25.3, 24.79, 25.15, 20.53, 390.78, 26.35, 25.86, 24.54, 23.46, 22.22, 24.14, 22.86, 21.61, 22.75, 380.16, 24.77, 24.51, 22.74, 21.63, 21.19, 22.46, 24.46, 21.61, 21.42, 380.66, 23.73, 23.87, 24.16, 22.79, 22.54, 23.36, 23.43, 19.38, 17.76, 355.04, 23.43, 23.94, 23.36, 22.33, 22.51, 20.65, 19.16, 18.05]
main_fed = [174.49, 168.37, 168.62, 166.61, 167.09, 169.16, 171.25, 167.51, 169.6, 168.9, 170.97, 165.58, 165.46, 170.71, 168.46, 168.92, 172.03, 164.5, 170.65, 166.64, 169.83, 166.97, 165.88, 168.63, 171.5, 166.41, 170.9, 167.83, 167.37, 165.86, 171.34, 166.97, 167.51, 164.96, 166.38, 169.01, 166.87, 165.75, 165.53, 166.64, 163.29, 164.55, 171.92, 169.79, 162.49, 167.01, 170.48, 168.28, 160.07, 169.79]
main_nn = [12.24, 11.28, 12.13, 12.08, 12.09, 12.14, 12.56, 12.67, 12.69, 12.76, 12.62, 12.61, 12.67, 12.66, 12.69, 12.66, 12.71, 12.63, 12.71, 12.69, 12.59, 12.58, 12.58, 12.62, 12.6, 12.55, 12.57, 12.53, 12.53, 12.71, 12.77, 12.71, 12.89, 13.0, 13.11, 12.86, 12.99, 11.68, 11.1, 10.99, 10.97, 10.94, 10.72, 10.57, 10.45, 10.22, 10.44, 10.17, 10.22, 9.59]

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
