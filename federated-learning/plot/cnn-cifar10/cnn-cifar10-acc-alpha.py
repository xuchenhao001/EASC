import sys

from plot.utils import plot_round_acc_alpha

scei = [40.35, 50.6, 55.7, 59.2, 61.8, 63.0, 64.1, 63.3, 64.85, 64.65, 64.8, 64.95, 65.1, 65.05, 65.5, 66.0, 65.95, 65.3, 66.4, 66.3, 66.05, 64.95, 66.0, 65.2, 65.85, 66.0, 65.55, 67.0, 67.1, 65.6, 66.6, 66.55, 66.55, 66.3, 66.35, 66.2, 66.8, 66.35, 66.95, 66.6, 66.9, 67.1, 66.35, 66.05, 66.25, 66.8, 66.9, 66.75, 66.7, 66.95]
scei_025 = [49.25, 56.45, 58.95, 59.0, 58.6, 58.95, 59.6, 57.8, 59.1, 57.85, 57.2, 57.4, 57.3, 57.0, 55.9, 55.45, 56.35, 55.25, 55.7, 55.7, 54.8, 55.0, 54.55, 55.45, 53.9, 54.05, 53.6, 53.55, 55.0, 53.7, 53.9, 53.45, 53.0, 53.5, 53.55, 53.4, 52.8, 52.55, 53.05, 52.95, 53.05, 52.75, 53.2, 52.6, 52.15, 51.95, 53.45, 52.3, 52.65, 51.3]
scei_050 = [50.35, 56.95, 60.55, 63.15, 61.0, 60.6, 60.55, 60.6, 60.05, 60.05, 59.7, 58.1, 59.3, 59.3, 59.15, 59.3, 59.75, 58.05, 58.9, 57.95, 58.7, 58.45, 55.6, 57.5, 57.7, 57.4, 56.9, 56.65, 57.05, 57.35, 57.2, 56.0, 56.75, 55.9, 56.2, 57.05, 55.15, 56.45, 56.0, 56.0, 55.85, 55.5, 55.7, 55.25, 55.25, 55.65, 55.45, 54.7, 55.2, 54.0]
scei_075 = [53.65, 59.0, 60.8, 59.5, 60.7, 60.5, 60.95, 59.85, 61.2, 61.3, 60.35, 62.0, 61.35, 61.55, 61.05, 61.95, 61.7, 61.05, 59.9, 61.95, 61.3, 60.95, 60.5, 61.4, 61.7, 61.85, 61.45, 61.0, 62.1, 60.25, 61.85, 61.15, 62.1, 61.75, 59.8, 60.95, 59.95, 61.9, 59.5, 59.95, 61.25, 58.0, 58.55, 58.3, 59.65, 60.6, 59.2, 59.45, 58.5, 59.8]
fedavg = [17.55, 21.6, 31.1, 36.35, 39.6, 41.6, 41.8, 41.05, 40.45, 39.8, 40.85, 40.2, 40.85, 41.2, 40.55, 40.35, 40.7, 40.3, 40.8, 40.3, 41.3, 40.25, 41.55, 41.45, 42.0, 41.5, 41.55, 42.45, 42.2, 41.3, 40.55, 41.75, 41.9, 42.75, 42.45, 42.65, 42.15, 42.9, 42.8, 40.65, 41.85, 42.05, 41.6, 41.8, 41.55, 41.6, 41.7, 42.55, 41.8, 42.3]
local = [55.35, 59.5, 60.3, 59.65, 58.95, 61.55, 62.6, 62.85, 62.95, 62.9, 63.0, 63.1, 63.15, 63.15, 63.0, 63.15, 63.2, 63.2, 63.15, 63.1, 63.1, 63.15, 63.15, 63.15, 63.15, 63.2, 63.15, 63.15, 63.15, 63.15, 63.15, 63.15, 63.15, 63.15, 63.15, 63.2, 63.2, 63.2, 63.2, 63.2, 63.2, 63.2, 63.2, 63.2, 63.25, 63.25, 63.25, 63.25, 63.3, 63.3]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc_alpha("", scei, fedavg, scei_025, scei_050, scei_075, local, True, False, save_path, plot_size="3")
