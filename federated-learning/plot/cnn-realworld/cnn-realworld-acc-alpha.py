import sys

from plot.utils import plot_round_acc_alpha

scei = [79.53, 82.25, 83.08, 83.47, 84.1, 84.38, 83.97, 84.58, 85.85, 86.15, 85.4, 86.6, 86.0, 86.75, 86.28, 86.88, 86.33, 87.25, 87.08, 87.47, 87.53, 87.7, 88.03, 88.17, 88.12, 87.78, 87.97, 88.78, 88.35, 88.17, 87.75, 88.33, 88.6, 89.03, 88.65, 88.25, 88.03, 88.55, 88.78, 89.03, 88.9, 88.28, 88.85, 88.95, 89.17, 88.67, 88.9, 88.67, 89.22, 89.2]
scei_025 = [57.98, 73.6, 77.15, 76.68, 78.38, 78.15, 78.55, 79.25, 78.05, 79.22, 78.5, 73.05, 80.75, 79.8, 81.2, 79.5, 77.75, 79.5, 78.75, 78.35, 80.25, 80.1, 76.95, 77.4, 77.05, 80.4, 80.45, 80.45, 78.55, 80.15, 79.65, 78.9, 79.05, 78.25, 77.45, 77.35, 79.5, 77.35, 77.95, 76.75, 74.75, 77.45, 76.7, 77.6, 79.05, 78.25, 77.45, 77.35, 79.5, 77.45]
scei_050 = [74.18, 76.35, 78.85, 79.7, 80.6, 82.08, 81.0, 81.9, 81.9, 70.75, 74.3, 74.65, 76.8, 78.05, 77.65, 80, 81.35, 81.55, 80.5, 80.3, 81, 81.45, 80.45, 80.05, 78.45, 80.35, 80.2, 79.25, 78.7, 79.5, 78.6, 78.6, 79.65, 78.4, 77.8, 76.05, 77, 77.7, 78.45, 78.05, 76.7, 76.15, 75.7, 76.65, 76.2, 75.6, 76.65, 74.75, 75.2, 74.85]
scei_075 = [56.7, 59.05, 64.95, 68.65, 70.8, 72.25, 74.4, 75.65, 76.25, 79.6, 76.1, 77.55, 78.65, 78.95, 80.65, 80, 80.35, 80.35, 80.1, 79.15, 81.8, 82.75, 82.8, 82.75, 83.1, 83.05, 84, 79.85, 81.85, 82.6, 81.9, 82.25, 80.7, 80.9, 80.15, 82.7, 81.2, 79.35, 80.6, 79.65, 80.7, 80.1, 80.2, 79.55, 79.05, 80.1, 80.1, 78.95, 80.9, 78.6]
fedavg = [51.12, 57.62, 62.95, 68.6, 70.03, 69.95, 71.45, 72.2, 71.7, 72.67, 72.55, 72.53, 73.85, 74.33, 74.12, 74.03, 75.1, 74.5, 75.25, 75.42, 74.92, 75.62, 75.58, 75.03, 75.22, 76.58, 76.42, 75.35, 76.33, 76.8, 76.42, 76.53, 76.72, 77.1, 76.62, 76.85, 77.1, 76.83, 77.33, 77.25, 76.62, 77.65, 77.42, 77.03, 77.22, 77.45, 77.53, 77.08, 77.15, 77.2]
local = [14.68, 78.47, 80.78, 81.95, 82.88, 83.25, 83.85, 82.88, 83.55, 83.83, 83.8, 83.85, 83.15, 84.17, 84.25, 84.12, 84.83, 84.45, 83.95, 84.88, 84.5, 85.4, 84.8, 84.33, 84.58, 84.95, 84.47, 85.1, 85.28, 85.85, 85.2, 84.83, 84.88, 85.38, 85.25, 85.2, 85.22, 85.03, 85.2, 84.85, 85.58, 85.55, 85.85, 85.53, 85.55, 85.05, 85.33, 84.9, 85.2, 84.95]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc_alpha("", scei, fedavg, scei_025, scei_050, scei_075, local, True, False, save_path, plot_size="3")
