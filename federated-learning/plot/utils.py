# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd
from cycler import cycler
import pylab

# input latex symbols in matplotlib
# https://stackoverflow.com/questions/43741928/matplotlib-raw-latex-epsilon-only-yields-varepsilon
plt.rcParams["mathtext.fontset"] = "cm"


# Plot number in a row: "2", "3", "4"
# 2: Two plots in a row (the smallest fonts)
# 3: Three plots in a row
# 4: Four plots in a row (the biggest fonts)
def get_font_settings(size):
    if size == "2":
        font_size_dict = {"l": 21, "m": 18, "s": 16}
        fig_width = 8  # by default is 6.4 x 4.8
        fig_height = 4
    elif size == "3":
        font_size_dict = {"l": 25, "m": 21, "s": 19}
        fig_width = 8
        fig_height = 4
    else:
        font_size_dict = {"l": 25, "m": 25, "s": 20}
        # fig_width = 6.4
        # fig_height = 4.8
        fig_width = 7.4
        fig_height = 4

    xy_label_font = font_manager.FontProperties(
        family='Times New Roman', weight='bold', style='normal', size=font_size_dict["l"])
    title_font = font_manager.FontProperties(
        family='Times New Roman', weight='bold', style='normal', size=font_size_dict["m"])
    legend_font = font_manager.FontProperties(
        family='Times New Roman', weight='bold', style='normal', size=font_size_dict["s"])
    ticks_font = font_manager.FontProperties(family='Times New Roman', style='normal', size=font_size_dict["s"])
    cs_xy_label_font = {'fontproperties': xy_label_font}
    cs_title_font = {'fontproperties': title_font}
    cs_xy_ticks_font = {'fontproperties': ticks_font}
    font_factory = {
        'legend_font': legend_font,
        'cs_xy_label_font': cs_xy_label_font,
        'cs_title_font': cs_title_font,
        'cs_xy_ticks_font': cs_xy_ticks_font,
        'fig_width': fig_width,
        'fig_height': fig_height,
    }
    return font_factory


def get_color_settings():
    # color names: https://matplotlib.org/stable/gallery/color/named_colors.html
    # colors = plt.get_cmap('tab10').colors  # by default
    colors = ("tab:blue",) + plt.get_cmap('Set2').colors
    # colors = [plt.cm.Spectral(i / float(6)) for i in range(6)]
    # colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']
    return colors


def get_cycler_settings():
    my_cycler = cycler(color=get_color_settings())
    return my_cycler


def plot_legend_head(axes, legend_column, width, height, save_path=None, plot_size="3"):
    font_settings = get_font_settings(plot_size)
    figlegend = pylab.figure()
    figlegend.legend(axes.get_legend_handles_labels()[0], axes.get_legend_handles_labels()[1],
                     prop=font_settings.get("legend_font"), ncol=legend_column, loc='upper center')
    figlegend.tight_layout()
    figlegend.set_size_inches(width, height)
    if save_path:
        save_path = save_path[:-4] + "-legend.eps"
        figlegend.savefig(save_path, format='eps')
    else:
        figlegend.show()


def plot_round_acc(title, scei, scei_async, apfl, fedavg, local, in_legend=False, ex_legend=False, save_path=None, plot_size="3"):
    font_settings = get_font_settings(plot_size)
    cycler_settings = get_cycler_settings()
    x = range(1, len(scei) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycler_settings)

    axes.plot(x, scei, label="SCEI", linewidth=4.5, zorder=10, marker='o', markevery=5, markersize=8, mfc='none')
    axes.plot(x, scei_async, label="SCEI-Async", marker='D', markevery=5, markersize=8, mfc='none')
    axes.plot(x, apfl, label="APFL", marker='v', markevery=5, markersize=8, mfc='none')
    axes.plot(x, fedavg, label="FedAvg", marker='>', markevery=5, markersize=8, mfc='none')
    axes.plot(x, local, label="Local", marker='x', markevery=5, markersize=8, mfc='none')

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.ylim(bottom=70)
    if in_legend:
        plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path, format='eps')
    else:
        plt.show()
    if ex_legend:
        plot_legend_head(axes, 5, 20.6, 0.7, save_path, plot_size)


def plot_round_acc_alpha(title, scei, fedavg, alpha025, alpha050, alpha075, local, in_legend=False, ex_legend=False, save_path=None, plot_size="3"):
    font_settings = get_font_settings(plot_size)
    cycler_settings = get_cycler_settings()
    x = range(1, len(scei) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycler_settings)

    axes.plot(x, scei, label="α=0.5-0.8 (SCEI)", linewidth=4.5, zorder=10, marker='o', markevery=5, markersize=8, mfc='none')
    axes.plot(x, fedavg, label="α=0.0 (FedAvg)", marker='D', markevery=5, markersize=8, mfc='none')
    axes.plot(x, alpha025, label="α=0.25", marker='v', markevery=5, markersize=8, mfc='none')
    axes.plot(x, alpha050, label="α=0.50", marker='>', markevery=5, markersize=8, mfc='none')
    axes.plot(x, alpha075, label="α=0.75", marker='x', markevery=5, markersize=8, mfc='none')
    axes.plot(x, local, label="α=1.0 (Local)", marker='|', markevery=5, markersize=8, mfc='none')

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    # plt.ylim(bottom=80)
    if in_legend:
        plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path, format='eps')
    else:
        plt.show()
    if ex_legend:
        plot_legend_head(axes, 6, 20.6, 0.7, save_path, plot_size)


def plot_time_cost(title, scei, scei_async, apfl, fedavg, local=None, in_legend=False, ex_legend=False, save_path=None, plot_size="3"):
    font_settings = get_font_settings(plot_size)
    cycler_settings = get_cycler_settings()
    x = range(1, len(scei) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycler_settings)

    axes.plot(x, scei, label="SCEI", linewidth=4.5, zorder=10, marker='o', markevery=5, markersize=8, mfc='none')
    axes.plot(x, scei_async, label="SCEI-Async", marker='D', markevery=5, markersize=8, mfc='none')
    axes.plot(x, apfl, label="APFL", marker='v', markevery=5, markersize=8, mfc='none')
    axes.plot(x, fedavg, label="FedAvg", marker='>', markevery=5, markersize=8, mfc='none')
    if local is not None:
        axes.plot(x, local, label="Local", marker='x', markevery=5, markersize=8, mfc='none')

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Average Time (s)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    if in_legend:
        plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path, format='eps')
    else:
        plt.show()
    if ex_legend:
        if local is not None:
            plot_legend_head(axes, 5, 20.6, 0.7, save_path, plot_size)
        else:
            plot_legend_head(axes, 4, 20.6, 0.7, save_path, plot_size)


def plot_round_acc_nodes(title, scei005, scei010, scei020, scei050, scei100, in_legend=False, ex_legend=False, save_path=None, plot_size="3"):
    font_settings = get_font_settings(plot_size)
    cycler_settings = get_cycler_settings()
    x = range(1, len(scei005) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycler_settings)

    axes.plot(x, scei005, label="5 Nodes", marker='o', markevery=5, markersize=8, mfc='none')
    axes.plot(x, scei010, label="10 Nodes", marker='D', markevery=5, markersize=8, mfc='none')
    axes.plot(x, scei020, label="20 Nodes", marker='v', markevery=5, markersize=8, mfc='none')
    axes.plot(x, scei050, label="50 Nodes", marker='>', markevery=5, markersize=8, mfc='none')
    axes.plot(x, scei100, label="100 Nodes", marker='x', markevery=5, markersize=8, mfc='none')

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    if in_legend:
        plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path, format='eps')
    else:
        plt.show()
    if ex_legend:
        plot_legend_head(axes, 5, 20.6, 0.7, save_path, plot_size)


# fed_server = []
# main_nn = []
# main_fed = []
# data = {'SCEI': fed_server, 'Local': main_nn, 'APFL': main_fed_localA, 'FedAvg': main_fed}
def plot_skew(title, data, in_legend=False, ex_legend=False, save_path=None, plot_size="3"):
    font_settings = get_font_settings(plot_size)
    color_settings = get_color_settings()

    df = pd.DataFrame.from_dict(data=data)

    fig, axes = plt.subplots()
    medianprops = dict(linewidth=2, color='black')
    bplot = axes.boxplot(df, labels=data.keys(), medianprops=medianprops, patch_artist=True)

    # fill with colors
    for patch, color in zip(bplot['boxes'], color_settings):
        patch.set_facecolor(color)

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xlabel("Scheme", **font_settings.get("cs_xy_label_font"))
    plt.ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    if in_legend:
        plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path, format='eps')
    else:
        plt.show()
    if ex_legend:
        plot_legend_head(axes, 5, 20.6, 0.7, save_path, plot_size)
