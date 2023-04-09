from pathlib import Path
import sys
import random
import time
start = time.perf_counter()
path = Path(__file__).parent.parent
sys.path.append(fr"{path}")

from storage import MultiFileStorageEngine
multi_storage = MultiFileStorageEngine(f"{Path(__file__).parent.parent.joinpath('data')}")
one_million_data = 1_000_000
def create_test_data(start: int ,end:int):
   return ([f"val1_{random.randint(start,end)}",f"val2_{random.randint(start,end)}",f"val3_{random.randint(start,end)}"] for i in range(one_million_data))


table1 = create_test_data(1,100)
table2 = create_test_data(101,200)
table3 = create_test_data(201,300)

multi_storage.create_multiple_tables(table1=['col1','col2','col3'],table2=['col1','col2','col3'],table3=['col1','col2','col3'])

multi_storage.insert_multiple_bulk(table1=table1,table2=table2,table3=table3)
end = time.perf_counter()
print(f"Execution completed in : {end-start:.2f}sec")