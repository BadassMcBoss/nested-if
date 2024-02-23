import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass
memory_usage = random.randint(0, 100)
if memory_usage > 80:
    print("High memory usage!")
elif memory_usage > 65 and memory_usage <= 80:
    pass
disk_space = random.randint(0, 100)
if disk_space > 75:
    print("Disk space almost full!")
elif disk_space > 60 and disk_space <= 75:
    pass