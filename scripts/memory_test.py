import tracemalloc

from src.data.data_iterator import DataIterator

file_path = "data/raw/large_data.csv"

tracemalloc.start()

iterator = DataIterator(file_path)

count = 0

for record in iterator:
    count += 1

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Records processed: {count:,}")
print(f"Current memory: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")