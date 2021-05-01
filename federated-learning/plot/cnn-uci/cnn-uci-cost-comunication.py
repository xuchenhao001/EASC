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
fed_server = [179.43, 177.96, 189.51, 181.22, 178.24, 181.9, 182.02, 175.37, 177.23, 176.29, 171.56, 175.85, 171.98, 177.91, 183.71, 179.45, 188.57, 179.63, 179.39, 182.42, 178.46, 178.68, 184.39, 176.65, 178.37, 180.59, 168.72, 174.26, 176.6, 180.43, 177.64, 184.28, 172.92, 174.48, 175.76, 169.21, 180.86, 176.78, 167.82, 179.03, 168.42, 177.36, 163.87, 182.58, 172.23, 181.93, 174.45, 176.75, 178.33, 184.16]
main_fed_localA = [0.19, 260.53, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 297.77, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 263.71, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 277.24, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 289.74, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
main_fed = [222.39, 213.96, 206.23, 206.05, 200.49, 194.63, 194.75, 198.9, 203.9, 199.27, 208.61, 197.59, 201.6, 195.77, 207.03, 196.85, 200.7, 206.74, 201.4, 201.66, 207.33, 205.59, 203.07, 203.6, 193.5, 202.28, 199.05, 196.5, 195.31, 199.55, 200.63, 200.51, 201.97, 204.64, 201.46, 202.56, 201.06, 200.89, 201.55, 198.3, 195.37, 196.65, 197.19, 202.72, 198.98, 196.23, 191.12, 200.56, 196.77, 160.04]

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
# plt.ylim(90, 100)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
