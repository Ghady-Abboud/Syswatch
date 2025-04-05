import psutil
import csv
import system_monitor
from datetime import datetime

def log_system_stats():
    cpu = system_monitor.get_cpu_usage() 
    cpu_load = system_monitor.get_cpu_load_average()
    cpu_temp = system_monitor.get_cpu_temp() 
    mem = system_monitor.get_memory_usage()
    now = datetime.now().isoformat()

    with open('system_stats.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([now,cpu,mem])
        print(f"{now}, CPU: {cpu}%, Memory: {mem}%")