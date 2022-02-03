import sys

from plot.utils import plot_round_acc_alpha

scei = [79.53, 82.25, 83.08, 83.47, 84.1, 84.38, 83.97, 84.58, 85.85, 86.15, 85.4, 86.6, 86.0, 86.75, 86.28, 86.88, 86.33, 87.25, 87.08, 87.47, 87.53, 87.7, 88.03, 88.17, 88.12, 87.78, 87.97, 88.78, 88.35, 88.17, 87.75, 88.33, 88.6, 89.03, 88.65, 88.25, 88.03, 88.55, 88.78, 89.03, 88.9, 88.28, 88.85, 88.95, 89.17, 88.67, 88.9, 88.67, 89.22, 89.2]
alpha025 = [60.98, 63.8, 69.4, 70.97, 73.97, 75.6, 77.7, 77.17, 80.05, 79.83, 81.35, 81.33, 82.22, 80.47, 81.55, 82.03, 83.05, 82.03, 83.15, 83.12, 82.45, 83.05, 82.92, 82.9, 82.8, 83.25, 83.6, 82.97, 84.03, 83.53, 83.88, 83.78, 84.17, 83.85, 83.78, 84.75, 84.1, 85.22, 83.95, 84.78, 84.28, 85.38, 85.08, 84.42, 84.42, 85.3, 84.97, 84.6, 85.17, 85.15]
alpha050 = [78.1, 80.55, 82.3, 82.47, 82.62, 84.47, 84.78, 84.1, 85.38, 85.42, 85.8, 85.6, 85.58, 86.05, 85.92, 86.28, 86.95, 86.1, 86.0, 87.25, 87.0, 87.08, 87.03, 86.75, 87.53, 87.25, 87.47, 87.33, 87.67, 87.6, 87.38, 87.53, 87.42, 87.95, 88.35, 87.9, 87.3, 87.9, 87.85, 88.6, 87.92, 87.97, 88.05, 88.33, 88.25, 88.97, 87.83, 88.12, 88.78, 88.62]
alpha075 = [73.65, 76.03, 77.9, 79.95, 79.8, 80.35, 80.88, 81.08, 81.12, 82.4, 81.95, 81.95, 82.75, 81.28, 82.62, 82.6, 83.12, 83.15, 83.03, 83.33, 83.58, 83.7, 83.12, 82.78, 83.0, 82.95, 83.15, 83.45, 83.6, 83.58, 83.62, 83.9, 83.6, 84.1, 84.17, 84.22, 84.22, 83.25, 84.2, 84.3, 84.83, 84.22, 83.97, 84.12, 84.1, 84.38, 84.92, 84.47, 84.17, 85.4]
fedavg = [52.92, 56.83, 61.73, 66.8, 69.78, 71.47, 71.78, 73.15, 73.25, 73.4, 73.2, 73.97, 74.97, 74.85, 75.42, 76.15, 76.38, 76.53, 76.72, 76.85, 77.08, 77.5, 77.47, 77.35, 77.45, 77.9, 78.1, 78.4, 78.0, 78.58, 77.95, 78.7, 78.78, 78.95, 78.78, 79.62, 78.75, 79.5, 79.95, 80.15, 80.33, 80.28, 79.75, 80.38, 80.22, 80.12, 80.9, 80.05, 80.28, 80.5]
local = [11.85, 78.08, 81.53, 82.78, 83.7, 83.3, 84.0, 84.25, 83.85, 83.35, 83.65, 84.03, 84.53, 84.12, 83.97, 84.5, 84.53, 85.12, 84.0, 84.58, 83.95, 83.38, 84.4, 84.58, 84.9, 85.1, 85.22, 84.38, 84.85, 84.35, 83.85, 84.78, 84.95, 84.83, 85.15, 84.42, 84.0, 84.97, 85.42, 84.6, 84.72, 84.67, 84.75, 84.88, 84.78, 84.97, 84.88, 85.33, 84.03, 84.47]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc_alpha("", scei, fedavg, alpha025, alpha050, alpha075, local, True, False, save_path, plot_size="3")
