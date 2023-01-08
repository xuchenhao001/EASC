import sys

from plot.utils import plot_round_acc_alpha

scei = [93.9, 94.6, 94.9, 94.4, 95.2, 95.15, 95.4, 95.1, 95.4, 95.5, 95.1, 95.45, 95.3, 95.55, 95.55, 95.7, 95.7, 95.15, 95.8, 95.55, 95.75, 95.75, 95.95, 96.0, 95.9, 96.0, 95.9, 96.3, 95.95, 96.0, 95.65, 96.15, 96.05, 96.0, 95.85, 95.85, 95.9, 96.25, 96.25, 96.15, 96.2, 95.95, 96.25, 96.2, 96.0, 95.8, 96.4, 96.4, 96.1, 96.25]
scei_025 = [87.0, 91.45, 91.9, 93.0, 93.55, 94.1, 93.65, 94.2, 94.05, 94.5, 94.5, 94.6, 95.0, 94.9, 95.1, 94.75, 95.0, 95.3, 95.1, 94.65, 94.7, 94.8, 94.95, 95.15, 95.35, 94.95, 95.15, 95.15, 94.85, 94.95, 95.35, 95.1, 94.9, 94.9, 94.8, 95.0, 95.1, 94.85, 95.0, 95.15, 95.15, 94.9, 95.2, 95.0, 95.0, 94.95, 95.15, 94.8, 94.9, 94.85]
scei_050 = [92.9, 93.7, 93.75, 94.85, 94.65, 95.05, 94.5, 94.65, 94.65, 94.9, 94.85, 94.85, 94.8, 95.05, 94.8, 95.05, 95.1, 95.3, 95.2, 95.15, 95.4, 95.05, 94.9, 95.15, 95.0, 95.35, 95.55, 95.6, 94.95, 95.4, 95.45, 95.55, 95.35, 95.4, 95.65, 95.35, 95.45, 95.75, 95.55, 95.35, 95.65, 95.4, 95.3, 95.15, 95.6, 95.15, 95.55, 95.65, 95.9, 95.8]
scei_075 = [93.25, 93.6, 94.35, 94.6, 95.05, 95.15, 95.15, 95.05, 95.25, 94.95, 95.2, 95.25, 95.45, 95.75, 95.7, 95.55, 95.7, 95.75, 95.85, 95.65, 95.55, 95.5, 96, 95.5, 95.95, 95.75, 95.75, 96.15, 95.15, 96.25, 95.85, 96.1, 95.9, 96, 96.15, 96.15, 95.9, 96, 95.9, 95.7, 96.1, 95.75, 95.65, 96.1, 96.25, 96.05, 95.85, 95.9, 96, 96.25]
fedavg = [71.05, 73.45, 77.8, 79.75, 81.25, 83.1, 84.1, 85.2, 85.7, 86.1, 86.8, 88.05, 88.35, 88.4, 89.6, 90.05, 89.4, 90.35, 90.8, 90.45, 90.8, 90.65, 90.75, 90.7, 90.85, 90.9, 90.75, 91.45, 91.25, 91.55, 91.6, 91.35, 91.4, 91.3, 91.5, 91.3, 92.0, 91.85, 91.75, 91.7, 91.85, 92.2, 91.8, 92.1, 91.9, 91.75, 92.0, 92.15, 92.1, 92.05]
local = [94.75, 95.55, 95.25, 95.45, 95.3, 95.4, 95.85, 95.65, 95.45, 95.45, 95.7, 95.8, 95.55, 95.7, 95.7, 95.8, 95.75, 95.75, 95.6, 95.55, 95.6, 95.65, 95.8, 95.85, 95.75, 95.9, 95.75, 95.55, 95.65, 95.7, 95.75, 95.65, 95.5, 95.5, 95.55, 95.55, 95.7, 95.7, 95.9, 95.6, 95.85, 95.65, 95.75, 95.9, 95.85, 95.75, 95.8, 95.85, 95.9, 95.9]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc_alpha("", scei, fedavg, scei_025, scei_050, scei_075, local, False, False, save_path, plot_size="4")