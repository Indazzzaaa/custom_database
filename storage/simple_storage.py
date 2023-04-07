import os
import threading

file_seamaphore = threading.Semaphore(1)


class FileStorageEngine:
    def __init__(self,directory,enforce_overwrite=False):
        self.directory = directory
        self.enforce_overwrite = enforce_overwrite
        if not os.path.exists(directory):
            os.makedirs(directory) 
            
    def create_table(self,table_name:str,fields:list):
        file_path = os.path.join(self.directory,f"{table_name}.csv")
        if not os.path.exists(file_path) or self.enforce_overwrite:
            with open(file_path , "w") as f:
                f.write(",".join(fields) + "\n")
        else:
            raise Exception("Table already exists")
    
    def insert_row(self,table_name:str,values:list):
        file_path = os.path.join(self.directory,f"{table_name}.csv")
        if  os.path.exists(file_path) :
            file_seamaphore.acquire()
            try:
                with open(file_path, "a") as f:
                    f.write(",".join(str(v) for v in values) + "\n")
            finally:
                file_seamaphore.release()
        else:
            raise Exception("Table does not exist")    
        
    def select_rows(self,table_name:str,where_clause=None):
        file_path = os.path.join(self.directory,f"{table_name}.csv")
        rows = []
        if  os.path.exists(file_path):
            with open(file_path,'r') as f:
                header = f.readline().strip().split(",")
                for line in f:
                    values = line.strip().split(",")
                    row = dict(zip(header,values))
                    if where_clause is None or where_clause(row):
                        rows.append(row)
        else:
            raise Exception("Table does not exist")
        return rows


# ! example to use it.
""" storage_engine = FileStorageEngine("data/customData",enforce_overwrite=True)
# storage_engine.create_table("users", ["id", "name", "email"])
# storage_engine.insert_row("users", [1, "Alice", "alice@example.com"])
# storage_engine.insert_row("users", [2, "Bob", "bob@example.com"])

rows = storage_engine.select_rows("users", where_clause=lambda row: row["name"] == "Alice")
for row in rows:
    print(row["email"])

print("Execution Completed !!") """
