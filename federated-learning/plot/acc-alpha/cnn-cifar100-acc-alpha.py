import sys

from plot.utils import plot_round_acc_alpha

scei = [64.9, 65.6, 67.25, 67.0, 66.85, 64.3, 63.9, 66.4, 65.05, 67.1, 66.1, 66.3, 65.45, 66.45, 65.15, 65.6, 65.85, 64.4, 63.85, 64.0, 61.65, 64.8, 66.05, 63.9, 65.25, 64.1, 63.35, 66.6, 62.05, 62.3, 65.3, 64.9, 66.0, 62.85, 64.05, 62.4, 63.1, 62.05, 66.6, 65.5, 61.35, 64.9, 62.6, 63.65, 63.3, 62.55, 60.55, 64.85, 62.4, 63.55]
scei_025 = [33.55, 41.1, 45.0, 49.35, 48.55, 48.7, 47.85, 50.05, 50.95, 48.55, 47.85, 49.1, 49.2, 47.7, 47.6, 49.55, 48.15, 47.05, 47.75, 46.55, 45.4, 44.85, 46.7, 45.95, 44.3, 42.25, 43.9, 43.7, 45.45, 41.25, 41.8, 42.45, 43.45, 42.95, 44.45, 42.1, 42.5, 44.15, 42.7, 45.45, 42.85, 42.6, 42.6, 42.2, 43.2, 41.75, 42.25, 43.05, 41.65, 42.15]
scei_050 = [56.75, 62.55, 63.0, 62.5, 62.25, 63.55, 62.45, 62.85, 61.3, 63.15, 61.05, 60.95, 61.85, 60.45, 60.35, 61.0, 60.05, 58.65, 58.1, 56.6, 59.15, 57.3, 57.85, 58.8, 57.35, 59.2, 58.25, 56.05, 57.7, 56.85, 58.0, 57.4, 56.0, 56.4, 56.9, 52.25, 55.95, 56.25, 56.1, 55.7, 54.8, 55.4, 55.05, 55.5, 54.05, 55.1, 55.4, 53.75, 55.15, 54.25]
scei_075 = [59.0, 63.3, 69.75, 65.4, 66.4, 67.05, 66.25, 64.35, 66.05, 67.55, 64.45, 65.4, 66.8, 63.75, 65.7, 63.55, 64.4, 62.1, 64.5, 57.7, 60.85, 65.7, 63.05, 63.9, 62.45, 62.05, 64.0, 65.8, 64.25, 62.1, 65.55, 62.35, 64.05, 64.4, 64.25, 64.6, 62.2, 63.0, 63.25, 62.55, 62.5, 64.2, 62.05, 63.7, 64.2, 62.65, 63.85, 64.15, 63.5, 63.2]
fedavg = [9.25, 17.4, 18.0, 21.6, 22.8, 23.45, 24.1, 24.65, 26.0, 25.8, 25.05, 26.35, 26.25, 25.7, 27.3, 25.45, 25.75, 26.55, 25.85, 27.05, 25.3, 25.75, 26.35, 26.05, 26.25, 27.15, 25.7, 28.6, 21.65, 27.8, 26.0, 28.6, 27.3, 26.7, 27.1, 28.25, 28.2, 28.6, 14.3, 23.7, 25.6, 20.55, 26.25, 27.7, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]
local = [59.2, 63.15, 62.15, 62.65, 62.35, 64.0, 63.8, 60.65, 61.8, 61.5, 62.2, 63.35, 58.35, 60.2, 60.0, 60.1, 61.15, 62.8, 60.3, 61.4, 62.85, 61.2, 61.9, 62.1, 62.55, 62.65, 59.95, 55.55, 55.5, 55.4, 55.4, 55.5, 55.5, 55.45, 55.45, 55.5, 55.55, 55.5, 55.55, 55.55, 55.6, 55.5, 55.6, 55.55, 55.55, 55.55, 55.55, 55.55, 55.5, 55.5]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc_alpha("", scei, fedavg, scei_025, scei_050, scei_075, local, False, False, save_path, plot_size="4")