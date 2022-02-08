import sys

from plot.utils import plot_round_acc

apfl = [26.05, 38.45, 46.8, 52.9, 55.35, 55.25, 55.55, 55.8, 55.2, 27.1, 41.6, 51.6, 55.3, 55.95, 53.55, 54.85, 52.5, 53.05, 53.0, 38.35, 51.75, 54.1, 53.75, 51.9, 51.25, 50.6, 51.6, 54.6, 53.1, 43.05, 51.75, 50.85, 48.4, 52.1, 50.6, 51.0, 50.9, 50.05, 51.6, 44.5, 50.7, 50.35, 49.95, 48.95, 51.3, 49.75, 50.95, 51.65, 50.55, 45.3]
fedavg = [5.0, 5.25, 6.4, 6.9, 7.45, 7.3, 8.1, 8.05, 8.85, 9.65, 9.85, 10.75, 10.85, 10.35, 10.35, 9.85, 10.75, 10.45, 9.9, 9.95, 11.4, 9.6, 11.05, 9.85, 10.05, 9.8, 10.55, 9.95, 10.15, 9.35, 9.85, 9.75, 9.4, 9.3, 9.2, 8.55, 9.35, 8.7, 9.3, 8.15, 9.75, 9.05, 8.15, 8.4, 8.65, 9.15, 9.15, 8.65, 8.6, 8.1]
local = [28.85, 35.3, 43.65, 49.7, 51.65, 53.25, 53.0, 55.15, 54.35, 52.3, 54.75, 54.25, 53.3, 53.8, 53.6, 51.8, 52.25, 50.15, 52.5, 53.25, 53.05, 52.2, 52.95, 52.35, 53.45, 53.1, 53.5, 51.35, 53.2, 52.8, 53.8, 53.75, 52.1, 53.95, 53.8, 54.2, 54.25, 53.4, 54.5, 54.25, 53.4, 53.7, 53.8, 51.9, 52.9, 53.8, 53.05, 53.75, 53.5, 53.55]
scei = [28.25, 29.3, 34.3, 35.2, 38.95, 41.45, 41.4, 40.3, 44.3, 47.15, 47.05, 46.6, 49.95, 52.1, 52.25, 52.35, 52.9, 55.0, 53.35, 54.3, 54.25, 55.55, 55.5, 57.05, 56.0, 55.95, 54.9, 54.35, 55.5, 56.05, 56.1, 55.1, 55.45, 54.5, 54.1, 54.6, 54.3, 53.4, 55.5, 54.05, 53.4, 53.6, 54.4, 54.35, 53.05, 54.6, 54.25, 53.7, 53.45, 52.85]
scei_async = [25.95, 26.4, 29.85, 36.45, 42.3, 41.4, 42.05, 45.25, 45.9, 46.9, 50.55, 50.95, 50.95, 51.8, 50.9, 53.4, 53.25, 51.6, 49.45, 51.6, 51.6, 51.9, 50.1, 50.95, 51.5, 50.2, 49.7, 50.6, 50.05, 50.0, 48.95, 48.45, 49.75, 49.55, 48.5, 48.7, 49.1, 46.65, 48.3, 46.75, 48.35, 47.85, 47.8, 49.35, 47.0, 46.15, 46.35, 47.85, 48.15, 48.35]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_round_acc("", scei, scei_async, apfl, fedavg, local, False, False, save_path, plot_size="4")
