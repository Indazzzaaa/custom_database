import threading
from multiprocessing.pool import ThreadPool
import random
import sys
from pathlib import Path
import time
from memory_profiler import profile

start = time.perf_counter()

path = Path(__file__).parent.parent
sys.path.append(fr"{path}")

from storage import FileStorageEngine


msg_list = ["Hello",'hi','How are you','How you doing? ','Lets play the game','No i wont']
worker_count =5000

simple_storage = FileStorageEngine(f'{path}\data',enforce_overwrite=True)
simple_storage.create_table(table_name="Thread_data",fields=['Thread No.','Thread id','Thead_Msg'])




def execute(thread_no):
    simple_storage.insert_row(table_name="Thread_data",values=[thread_no,threading.get_ident(),random.choice(msg_list)])

@profile
def main():
    with ThreadPool(processes=worker_count) as pool:
        pool.map(execute, range(worker_count))

if __name__ =="__main__":
    main()



end = time.perf_counter()
print(f"Execution completed in : {end-start:.2f}sec")

print("Execution completed !!")