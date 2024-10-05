import psutil
import shutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > CPU_THRESHOLD:
    print(f"CPU usage is high: {cpu_usage}%")

memory_info = psutil.virtual_memory()
memory_usage = memory_info.percent
if memory_usage > MEMORY_THRESHOLD:
    print(f"Memory usage is high: {memory_usage}%")

disk_usage = shutil.disk_usage("/")
disk_percent = disk_usage.used / disk_usage.total * 100
if disk_percent > DISK_THRESHOLD:
    print(f"Disk usage is high: {disk_percent:.2f}%")
