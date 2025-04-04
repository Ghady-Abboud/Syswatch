import psutil
import csv
from datetime import datetime

def log_system_stats():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    now = datetime.now().isoformat()

    with open('system_stats.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([now,cpu,mem])
        print(f"{now}, CPU: {cpu}%, Memory: {mem}%")