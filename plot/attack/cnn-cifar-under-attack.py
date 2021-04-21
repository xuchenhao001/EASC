# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans
import matplotlib.patches as mpatches
import matplotlib.font_manager as font_manager

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
node0 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 0.0, 25.0, 0.0, 0.0, 25.0, 0.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 0.0, 25.0, 0.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node1 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node2 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node3 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node4 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node5 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node6 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node7 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node8 = [33.5, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]
node9 = [25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0,
         25.0, 25.0, 25.0, 25.0, 0.0, 25.0, 0.0, 0.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0]

# fig, axes = plt.subplots()
fig, axes = plt.subplots(figsize=(6, 3))

legendFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=10)
xylabelFont = font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=12)
csXYLabelFont = {'fontproperties': xylabelFont}


def split_line(ax, original_y_list, split_at, before_line_style, after_line_style, line_color, line_width, line_label):
    for i in range(split_at):
        ax.plot([i + 1, i + 2], [original_y_list[i], original_y_list[i + 1]],
                linestyle=before_line_style, color=line_color)
    for i in range(split_at, len(original_y_list) - 1):
        if i == len(original_y_list) - 2:
            ax.plot([i + 1, i + 2], [original_y_list[i], original_y_list[i + 1]],
                    linestyle=after_line_style, color=line_color, linewidth=line_width, label=line_label)
        else:
            ax.plot([i + 1, i + 2], [original_y_list[i], original_y_list[i + 1]],
                    linestyle=after_line_style, color=line_color, linewidth=line_width)


axes.plot(x, node0, label="Node1 (Compromised at beginning)", linewidth=3)
tr = mtrans.offset_copy(axes.transData, fig=fig, x=0.0, y=2.0, units='points')
axes.plot(x, node1, label="Node2 (Compromised at beginning)", transform=tr, linewidth=3)
split_line(axes, node9, 38, '--', '-', '#17becf', 3, "Node3 (Compromised in training)")
axes.plot(x, node2, label="Node4", linestyle='--', alpha=0.5)
axes.plot(x, node3, label="Node5", linestyle='--', alpha=0.5)
axes.plot(x, node4, label="Node6", linestyle='--', alpha=0.5)
axes.plot(x, node5, label="Node7", linestyle='--', alpha=0.5)
axes.plot(x, node6, label="Node8", linestyle='--', alpha=0.5)
axes.plot(x, node7, label="Node9", linestyle='--', alpha=0.5)
axes.plot(x, node8, label="Node10", linestyle='--', alpha=0.5)
# axes.plot(x, node9, label="Node10", linestyle='--', alpha=0.5)

axes.set_xlabel("Training Rounds", **csXYLabelFont)
axes.set_ylabel("Local Test Accuracy (%)", **csXYLabelFont)

# where some data has already been plotted to ax
handles, labels = axes.get_legend_handles_labels()
# manually define a new patch
patch = mpatches.Patch(color='grey', label='Manual Label', linestyle='-')
# handles is a list, so append manual patch
handles.append(patch)

plt.xticks(family='Times New Roman', fontsize=10)
plt.yticks(family='Times New Roman', fontsize=10)
# plt.ylim(top=40)
# plt.legend(prop=legendFont)
# plt.legend(prop=legendFont, bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=5)
plt.legend(prop=legendFont, bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=4)
plt.grid()
plt.show()
