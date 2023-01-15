import sys

from plot.utils import plot_round_acc

apfl = [50.0, 53.0, 55.0, 55.0, 59.0, 57.0, 61.5, 63.5, 58.0, 63.0, 68.0, 65.5, 64.5, 65.0, 61.5, 63.5, 60.5, 62.5, 63.0, 63.5, 64.0, 64.5, 66.0, 65.5, 62.5, 63.0, 65.5, 68.0, 69.0, 65.5, 66.5, 66.5, 66.5, 67.5, 67.5, 65.5, 66.5, 67.5, 66.5, 66.5, 64.5, 65.0, 65.0, 66.0, 65.5, 65.0, 67.0, 63.0, 65.5, 64.5]
fedavg = [29.0, 38.5, 44.0, 53.5, 53.0, 46.5, 52.0, 62.0, 62.0, 57.0, 61.5, 58.5, 62.0, 52.5, 68.0, 58.5, 67.0, 69.5, 66.5, 66.0, 63.5, 66.5, 65.5, 59.5, 65.0, 64.0, 65.0, 65.5, 65.0, 65.5, 65.5, 65.0, 66.0, 64.0, 65.0, 62.5, 61.5, 66.0, 66.5, 70.5, 69.5, 69.5, 70.0, 67.5, 69.0, 68.5, 69.5, 68.5, 66.0, 64.5]
local = [35.5, 48.5, 51.0, 44.5, 55.0, 57.5, 60.5, 60.0, 59.5, 61.0, 63.5, 59.0, 62.5, 64.0, 60.5, 63.0, 63.5, 59.0, 61.5, 57.0, 62.0, 62.5, 66.0, 64.5, 67.5, 65.5, 66.5, 66.0, 67.0, 66.5, 67.0, 71.0, 64.0, 67.0, 66.5, 69.0, 68.5, 63.0, 65.5, 66.5, 66.0, 63.5, 67.5, 66.5, 65.5, 65.0, 69.0, 68.5, 68.5, 68.5]
scei = [26.0, 38.0, 43.5, 31.5, 53.5, 62.5, 59.5, 48.5, 67.0, 58.5, 76.0, 68.0, 66.5, 64.5, 72.0, 76.0, 74.0, 77.0, 74.0, 81.5, 79.0, 84.0, 83.0, 86.0, 78.0, 86.0, 85.5, 81.5, 82.5, 83.5, 82.5, 83.5, 82.5, 82.5, 84.5, 82.5, 84.0, 83.5, 84.5, 82.0, 85.5, 82.5, 84.0, 82.5, 83.5, 86.0, 84.5, 84.5, 83.0, 83.5]
scei_async = [36.5, 44.5, 67.0, 52.5, 64.0, 70.0, 76.5, 74.5, 72.0, 68.0, 70.5, 67.0, 80.5, 80.0, 77.5, 79.5, 80.5, 83.0, 80.5, 81.5, 80.5, 79.0, 78.0, 78.0, 79.0, 80.5, 80.5, 77.0, 79.0, 75.5, 77.0, 69.0, 80.0, 78.0, 78.5, 78.0, 78.5, 78.5, 79.5, 77.5, 77.0, 78.0, 79.0, 79.0, 78.0, 78.0, 78.0, 78.0, 78.5, 79.5]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc("", scei, scei_async, apfl, fedavg, local, False, False, save_path, plot_size="4")