# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd


# fed_server = []
# main_nn = []
# main_fed = []
# data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}

def plot_skew(data, save_path):
    df = pd.DataFrame.from_dict(data=data)

    fig, axes = plt.subplots()
    medianprops = dict(linewidth=2, color='black')
    bplot = axes.boxplot(df, labels=data.keys(), medianprops=medianprops, patch_artist=True)

    # fill with colors
    colors = plt.get_cmap('tab10').colors
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    # legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=15)
    titleFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=25)
    csTitleFont = {'fontproperties': titleFont}
    xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=25)
    csXYLabelFont = {'fontproperties': xylabelFont}
    plt.xlabel("Models", **csXYLabelFont)
    plt.ylabel("Mean Local Test ACC (%)", **csXYLabelFont)
    # plt.title(title, **csTitleFont)
    plt.xticks(family='Times New Roman', weight='bold', fontsize=22)
    plt.yticks(family='Times New Roman', weight='bold', fontsize=22)
    plt.tight_layout()
    # plt.legend(prop=legendFont)
    plt.grid()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

