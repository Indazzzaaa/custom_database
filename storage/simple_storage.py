import os
import threading
import csv


file_seamaphore = threading.Semaphore(1)
MAX_INT = 10_000_000


class FileStorageEngine:
    def __init__(self,directory,enforce_overwrite=True):
        self.directory = directory
        self.enforce_overwrite = enforce_overwrite
        if not os.path.exists(directory):
            os.makedirs(directory) 
     # Two modes for creating table 1. for create table either exist or not , 2. Throw exception if exist(setting enforce_overwrite=False)
    def create_table(self,table_name:str,fields:list,enforce_overwrite=True):
        self.enforce_overwrite = enforce_overwrite
        file_path = os.path.join(self.directory,f"{table_name}.csv")
        if not os.path.exists(file_path) or self.enforce_overwrite:
            with open(file_path , "w") as f:
                f.write(",".join(fields) + "\n")
        else:
            raise Exception(f"{table_name} Table already exists")
    
    def insert_row(self,table_name:str,values:list):
        file_path = os.path.join(self.directory,f"{table_name}.csv")
        if  os.path.exists(file_path) :
            file_seamaphore.acquire()
            try:
                with open(file_path, "a") as f:
                    f.write(",".join(str(v) for v in values) + "\n")
            except Exception as e:
                print(f"Error while inserting in : {table_name}, values : {values}")
                print(e)
            finally:
                file_seamaphore.release()
        else:
            raise Exception(f"{table_name} Table does not exist")    
        
    def select_rows(self,table_name:str,where_clause=None):
        file_path = os.path.join(self.directory,f"{table_name}.csv")
        rows = []
        if  os.path.exists(file_path):
            try:
                with open(file_path,'r') as f:
                    header = f.readline().strip().split(",")
                    for line in f:
                        values = line.strip().split(",")
                        row = dict(zip(header,values))
                        if where_clause is None or where_clause(row):
                            rows.append(row)
            except Exception as e:
                print(f"Error while Reading from table  : {table_name}")
                print(e)
        else:
            raise Exception(f"{table_name} Table does not exist")
        return rows
    
    def read_table(self,table_name:str,where_clause=None,ignore_header=False,lines_to_read=MAX_INT):
        file_path = os.path.join(self.directory,f"{table_name}.csv")
        if os.path.exists(file_path):
            rows = []
            header = []
            with open(file_path,'r') as csvfile:
                csvreader = csv.reader(csvfile)
                header = next(csvreader)
                if not ignore_header:
                    rows.append(header)
                for i, row in enumerate(csvreader):
                    if i>=lines_to_read:
                        break
                    row = dict(zip(header,row))
                    if where_clause is None or where_clause(row):
                        rows.append(row)
            return rows

        else:
            print(f"{table_name} Table  does not exist")
            raise Exception(" File Not Found ")
        


# ! example to use it.
""" storage_engine = FileStorageEngine("data/customData",enforce_overwrite=True)
# storage_engine.create_table("users", ["id", "name", "email"])
# storage_engine.insert_row("users", [1, "Alice", "alice@example.com"])
# storage_engine.insert_row("users", [2, "Bob", "bob@example.com"])

rows = storage_engine.select_rows("users", where_clause=lambda row: row["name"] == "Alice")
for row in rows:
    print(row["email"])

print("Execution Completed !!") """
