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
node0 = [33.5, 34.5, 24.5, 36.0, 35.0, 34.5, 34.5, 35.0, 34.5, 36.0, 37.0, 36.0, 36.5, 20.5, 20.0, 20.0, 20.0, 20.5, 20.5, 20.5, 20.0, 21.0, 20.5, 20.0, 20.5, 20.5, 20.0, 20.0, 20.0, 20.0, 20.5, 20.0, 20.0, 20.0, 20.0, 20.0, 19.5, 20.0, 20.0, 20.0, 20.0, 20.0, 19.0, 19.0, 10.0, 10.5, 9.5, 10.0, 19.0, 19.5]
node1 = [27.0, 19.0, 29.5, 19.5, 30.5, 19.0, 29.5, 28.5, 17.5, 18.0, 18.5, 18.5, 18.5, 18.0, 17.5, 17.5, 18.0, 18.0, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.0, 18.0, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.5, 17.0, 0.5, 17.0, 17.5, 17.5]
node2 = [83.5, 80.0, 76.0, 68.5, 59.5, 63.5, 49.0, 37.5, 27.0, 30.5, 30.0, 30.0, 30.0, 29.5, 29.5, 24.0, 28.0, 28.0, 28.0, 20.5, 20.5, 20.0, 20.5, 20.5, 27.5, 20.0, 20.0, 36.5, 24.5, 27.0, 14.5, 15.5, 14.0, 14.5, 14.5, 14.5, 15.0, 14.5, 15.0, 20.0, 15.0, 15.0, 14.5, 15.5, 14.5, 14.0, 14.0, 13.0, 15.0, 14.0]
node3 = [89.0, 88.5, 82.0, 78.5, 72.0, 66.5, 75.5, 62.0, 62.0, 67.0, 52.5, 47.0, 46.5, 45.0, 45.5, 47.5, 48.0, 46.5, 46.5, 47.0, 47.5, 43.5, 47.0, 55.0, 46.0, 46.5, 46.0, 42.5, 42.5, 42.5, 46.0, 48.5, 59.5, 41.5, 42.0, 42.5, 42.0, 42.0, 42.0, 41.0, 42.0, 42.0, 42.0, 42.0, 42.5, 49.5, 36.5, 42.5, 42.0, 42.0]
node4 = [89.5, 83.5, 85.0, 72.5, 73.0, 75.5, 59.5, 53.5, 66.5, 50.5, 50.5, 58.0, 48.5, 49.5, 49.0, 48.5, 49.0, 49.0, 41.0, 41.0, 41.5, 41.5, 41.0, 41.5, 47.0, 47.0, 47.5, 42.0, 42.0, 40.5, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 41.0, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 47.5, 40.5, 40.5, 40.5]
node5 = [85.0, 84.0, 85.5, 81.5, 71.5, 58.5, 73.0, 62.0, 66.5, 50.0, 54.5, 52.0, 48.5, 49.0, 49.0, 47.5, 40.0, 41.0, 45.5, 43.0, 44.0, 44.0, 43.5, 44.0, 44.0, 44.5, 44.0, 44.0, 44.5, 44.0, 44.0, 44.0, 44.0, 44.0, 44.0, 43.5, 43.5, 43.5, 43.5, 53.0, 43.0, 43.5, 43.5, 43.5, 43.5, 43.5, 43.5, 48.5, 43.5, 43.5]
node6 = [88.0, 91.0, 82.0, 78.5, 77.5, 58.5, 74.0, 71.0, 64.0, 58.5, 53.5, 51.0, 62.5, 51.0, 43.5, 45.5, 43.5, 56.5, 49.0, 70.0, 41.5, 41.5, 41.5, 41.5, 42.0, 42.0, 42.0, 41.5, 47.5, 48.0, 47.5, 48.0, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5]
node7 = [96.0, 90.0, 83.0, 78.0, 71.0, 70.5, 56.0, 55.0, 51.5, 49.5, 52.0, 49.0, 55.0, 48.5, 48.0, 48.0, 59.0, 41.5, 40.5, 60.0, 40.0, 40.5, 43.5, 40.0, 40.0, 39.5, 39.5, 39.5, 40.0, 39.5, 39.5, 39.5, 40.0, 40.0, 39.5, 40.0, 39.5, 39.5, 39.5, 39.5, 40.0, 39.5, 39.5, 39.5, 39.0, 39.0, 39.5, 39.0, 39.0, 39.5]
node8 = [87.0, 87.5, 77.0, 70.0, 59.5, 62.0, 60.0, 60.0, 54.5, 54.0, 46.0, 45.0, 44.0, 43.0, 42.0, 46.5, 42.0, 42.5, 42.5, 42.0, 42.5, 42.5, 42.0, 41.5, 41.5, 41.0, 41.0, 40.5, 40.0, 40.0, 40.5, 40.0, 40.5, 40.5, 40.5, 40.5, 40.0, 40.5, 40.5, 30.0, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5, 40.5]
node9 = [89.0, 77.5, 80.0, 66.0, 74.0, 55.0, 52.5, 53.5, 54.0, 62.5, 49.0, 50.0, 49.5, 49.5, 50.0, 49.5, 48.5, 48.5, 48.0, 47.5, 47.5, 47.5, 40.0, 47.5, 47.5, 47.5, 47.5, 47.5, 47.0, 58.5, 47.0, 47.0, 47.0, 47.0, 47.0, 47.0, 47.5, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.5, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0]

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
plt.legend(prop=legendFont, bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=4)
plt.grid()
plt.show()
