import tracemalloc

tracemalloc.start()

# your code here
list= (i for i in range(10_000_000))
print(type(list))
# del list

# a =10
current, peak = tracemalloc.get_traced_memory()
# print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Current memory usage: {current} bytes")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()
