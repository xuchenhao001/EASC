# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt-get install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```

import matplotlib.pyplot as plt
import matplotlib.transforms as mtrans
import matplotlib.font_manager as font_manager

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
node0 = [25.0, 25.0, 25.0, 25.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
node1 = [25.0, 23.0, 25.0, 25.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
node2 = [35.5, 45.5, 54.5, 48.5, 57.5, 57.5, 54.5, 55.0, 57.0, 60.5, 61.0, 62.5, 61.5, 61.0, 61.0, 59.0, 59.0, 60.5, 59.0, 60.5, 63.0, 60.5, 61.5, 61.5, 62.5, 60.5, 60.0, 60.0, 58.0, 61.0, 60.0, 60.0, 60.0, 59.0, 59.5, 61.5, 61.0, 59.5, 59.0, 58.0, 59.5, 59.0, 60.5, 60.5, 60.0, 60.5, 60.5, 60.0, 60.5, 62.0]
node3 = [40.0, 46.5, 47.5, 49.5, 53.5, 57.0, 59.5, 58.5, 53.5, 55.0, 51.0, 58.5, 59.5, 60.0, 63.5, 60.0, 59.0, 60.0, 55.5, 59.0, 57.5, 57.5, 59.0, 58.0, 57.0, 58.5, 59.0, 60.0, 59.5, 60.0, 61.5, 59.5, 60.0, 62.5, 61.0, 60.0, 61.5, 60.0, 61.0, 62.0, 63.0, 62.5, 61.5, 57.0, 59.0, 59.0, 60.0, 59.5, 60.0, 59.0]
node4 = [39.5, 47.5, 60.5, 53.5, 65.0, 63.5, 64.0, 59.5, 61.0, 63.0, 65.0, 63.5, 63.5, 66.5, 64.0, 63.0, 63.0, 63.5, 64.0, 64.0, 63.0, 64.0, 63.5, 63.0, 63.0, 62.5, 62.5, 63.0, 63.0, 64.5, 65.5, 66.0, 65.0, 62.5, 63.0, 63.5, 65.0, 65.0, 64.5, 64.5, 63.5, 63.5, 61.5, 62.5, 63.5, 63.0, 66.5, 64.5, 63.5, 62.0]
node5 = [34.0, 53.0, 58.5, 58.0, 59.5, 68.0, 66.5, 67.5, 64.0, 64.0, 66.5, 66.5, 66.0, 66.5, 66.0, 64.5, 67.0, 67.5, 67.0, 67.5, 65.5, 67.0, 67.5, 68.0, 68.0, 67.5, 68.0, 63.5, 66.0, 66.5, 67.0, 66.0, 65.5, 70.5, 70.0, 70.0, 69.0, 68.5, 67.5, 68.5, 67.0, 65.5, 68.0, 68.0, 68.0, 67.0, 65.5, 66.5, 68.0, 67.0]
node6 = [47.5, 45.0, 61.0, 58.0, 56.0, 54.5, 57.0, 53.0, 57.5, 58.0, 59.0, 61.0, 62.0, 62.5, 59.5, 61.0, 59.0, 59.5, 59.5, 60.0, 61.0, 60.5, 60.0, 58.5, 58.5, 59.0, 58.5, 59.0, 59.5, 60.5, 61.5, 60.5, 60.0, 58.5, 60.5, 60.5, 59.5, 59.5, 59.0, 57.5, 59.0, 61.5, 61.0, 61.0, 57.0, 57.5, 61.0, 60.5, 60.0, 59.5]
node7 = [42.5, 53.5, 61.0, 64.0, 64.0, 64.0, 62.5, 64.5, 64.5, 62.5, 66.0, 66.5, 66.5, 67.5, 66.5, 69.5, 68.5, 68.0, 69.0, 67.5, 67.0, 67.0, 67.5, 67.0, 67.5, 67.5, 67.5, 67.0, 66.0, 65.5, 69.5, 68.0, 66.5, 66.5, 66.5, 67.0, 67.0, 68.0, 67.0, 66.0, 65.5, 65.5, 64.5, 64.0, 66.0, 66.0, 66.0, 63.5, 63.0, 65.5]
node8 = [39.0, 51.0, 51.5, 60.5, 60.5, 53.5, 60.5, 67.0, 62.5, 62.5, 64.0, 66.5, 65.0, 63.0, 66.0, 66.0, 65.0, 65.0, 64.5, 65.0, 65.5, 64.5, 65.0, 66.0, 67.0, 66.5, 65.5, 66.5, 65.5, 66.0, 67.5, 68.0, 70.0, 68.5, 68.0, 67.5, 68.5, 67.0, 66.5, 65.5, 64.5, 65.5, 67.0, 68.0, 62.5, 67.0, 68.5, 69.0, 68.0, 70.0]
node9 = [38.5, 52.5, 45.0, 54.0, 60.0, 59.5, 62.0, 63.0, 65.0, 59.5, 54.0, 61.0, 59.5, 59.0, 60.5, 59.0, 58.0, 58.0, 57.5, 60.0, 60.0, 60.0, 60.5, 59.5, 61.5, 60.5, 61.5, 63.0, 62.0, 60.5, 61.5, 62.5, 61.5, 63.0, 64.0, 64.5, 63.5, 64.0, 64.0, 25.0, 21.0, 25.0, 25.0, 0, 0, 0, 0, 0, 0, 0]

fig, axes = plt.subplots(figsize=(6, 3))
# fig, axes = plt.subplots()

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

# axes.set_aspect('equal')

plt.xticks(family='Times New Roman', fontsize=10)
plt.yticks(family='Times New Roman', fontsize=10)
# plt.ylim(90, 100)
# plt.legend(prop=legendFont, bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=5)
plt.legend(prop=legendFont, bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=4)
plt.grid()
plt.show()
