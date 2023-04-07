import psutil
import os

process = psutil.Process(os.getpid())
list = ( i for i in range(10_000_000))
print(type(list))
print(f"Memory usage: {process.memory_info().rss / 1024 / 1024:.2f} MB")
