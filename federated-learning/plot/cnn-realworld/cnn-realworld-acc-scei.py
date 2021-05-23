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

fed_server = [84.53, 86.03, 87.4, 88.4, 87.93, 88.77, 88.67, 88.33, 88.63, 89.4, 89.5, 89.37, 89.47, 89.5, 88.73, 89.47, 89.37, 90.07, 89.57, 90.23, 89.83, 90.5, 90.3, 90.47, 90.37, 90.17, 90.17, 90.23, 90.03, 90.67, 90.3, 90.73, 90.6, 90.27, 90.47, 90.9, 90.9, 90.67, 90.4, 90.43, 90.5, 90.43, 90.43, 90.93, 90.73, 91.23, 91.73, 91.13, 91.07, 90.83]
fed_server_alpha_025 = [68.47, 63.33, 66.0, 66.87, 69.7, 72.07, 73.67, 74.97, 77.0, 77.57, 77.93, 78.63, 80.33, 81.1, 82.23, 82.6, 82.57, 82.87, 83.0, 84.97, 83.8, 83.57, 83.77, 84.97, 84.57, 84.3, 84.77, 85.37, 85.47, 85.23, 85.5, 85.57, 85.8, 86.17, 86.27, 85.57, 84.9, 85.7, 86.5, 85.47, 85.67, 85.9, 86.53, 86.43, 86.0, 86.37, 86.33, 85.97, 85.8, 86.13]
fed_server_alpha_050 = [80.23, 83.37, 84.63, 85.2, 87.63, 88.23, 88.73, 89.0, 89.1, 90.63, 89.73, 90.6, 90.07, 91.0, 90.73, 91.03, 90.43, 90.6, 90.93, 91.23, 90.03, 90.77, 90.67, 91.6, 90.83, 91.17, 91.3, 91.03, 91.3, 91.07, 91.23, 91.57, 90.8, 91.1, 91.37, 91.13, 91.23, 91.5, 91.2, 91.07, 91.43, 91.5, 91.37, 91.27, 91.57, 91.83, 91.7, 91.97, 91.67, 91.73]
fed_server_alpha_075 = [78.9, 81.47, 83.5, 83.6, 83.0, 84.37, 84.37, 84.9, 85.0, 85.67, 84.6, 85.63, 85.7, 86.07, 86.53, 86.97, 86.23, 85.97, 86.4, 86.37, 86.77, 87.33, 87.07, 87.13, 87.0, 86.7, 87.53, 87.63, 87.67, 86.83, 87.07, 87.8, 85.43, 87.73, 87.83, 88.2, 88.03, 87.87, 87.47, 88.03, 88.37, 87.83, 88.0, 88.8, 88.13, 87.93, 88.2, 87.77, 88.53, 88.87]
main_fed = [55.4, 56.13, 57.47, 58.83, 63.53, 65.83, 68.53, 70.87, 68.77, 70.3, 71.17, 71.53, 70.8, 71.3, 72.47, 73.67, 74.03, 73.3, 73.27, 73.13, 73.87, 74.33, 74.2, 74.67, 73.77, 74.53, 73.77, 75.3, 74.23, 74.5, 74.3, 75.53, 74.93, 75.57, 75.53, 75.2, 75.6, 74.93, 75.8, 76.0, 75.13, 75.73, 76.0, 76.5, 75.73, 76.6, 75.77, 76.83, 75.73, 75.9]
main_nn = [10.27, 81.23, 83.5, 84.6, 85.6, 85.37, 86.03, 87.13, 86.53, 87.07, 87.13, 87.57, 87.4, 87.77, 87.77, 87.77, 87.7, 87.63, 87.6, 87.27, 88.33, 87.63, 87.67, 88.33, 87.43, 87.7, 88.23, 88.13, 87.8, 87.8, 87.83, 88.0, 87.7, 88.5, 88.13, 88.53, 87.93, 88.77, 88.13, 88.73, 87.97, 88.3, 88.2, 87.93, 88.43, 88.23, 87.93, 87.9, 87.9, 87.93]

fig, axes = plt.subplots()

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
csXYLabelFont = {'fontproperties': xylabelFont}

markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
axes.plot(x, fed_server, label="negotiated α (0.5-0.8)", linewidth=3)
axes.plot(x, main_fed, label="α=0.0 (i.e. FedAvg)",  alpha=0.5)
axes.plot(x, fed_server_alpha_025, label="α=0.25",  alpha=0.5)
axes.plot(x, fed_server_alpha_050, label="α=0.5",  alpha=0.5)
axes.plot(x, fed_server_alpha_075, label="α=0.75",  alpha=0.5)
axes.plot(x, main_nn, label="α=1.0 (i.e. Local Training)",  alpha=0.5)


axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Mean of Local Test Accuracy (%)", **csXYLabelFont)

plt.xticks(family='Times New Roman', fontsize=15)
plt.yticks(family='Times New Roman', fontsize=15)
plt.tight_layout()
plt.ylim(50)
plt.legend(prop=legendFont)
plt.grid()
plt.show()
