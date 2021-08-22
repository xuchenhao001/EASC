# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import cycler


def plot_time_cost(title, fed_server, main_fed, main_fed_localA, main_nn=None, save_path=None):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    fig, axes = plt.subplots()
    legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
    xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
    titleFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=17)
    csXYLabelFont = {'fontproperties': xylabelFont}
    csTitleFont = {'fontproperties': titleFont}
    markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1", "|"]
    axes.set_prop_cycle(cycler(color=plt.get_cmap('tab10').colors, marker=markers))
    axes.plot(x, fed_server, label="SCEI", linewidth=3)
    axes.plot(x, main_fed, label="FedAvg", alpha=0.5)
    axes.plot(x, main_fed_localA, label="APFL", alpha=0.5)
    if main_nn:
        axes.plot(x, main_nn, label="Local Training", alpha=0.5)
    axes.set_xlabel("Training Round", **csXYLabelFont)
    axes.set_ylabel("Time (s)", **csXYLabelFont)
    plt.title(title, **csTitleFont)
    plt.xticks(family='Times New Roman', fontsize=15)
    plt.yticks(family='Times New Roman', fontsize=15)
    plt.tight_layout()
    # plt.ylim(90, 100)
    plt.legend(prop=legendFont)
    plt.grid()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

