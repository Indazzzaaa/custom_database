import struct
import os

class BinaryFileStorageEngine:
    def __init__(self,directory,enforce_overwrite=False):
        self.directory = directory
        self.enforce_owerwrite = enforce_overwrite
        self.buffer = bytearray(1024)

    def create_table(self,table_name,fields):
        file_path =  os.path.join(self.directory,f"{table_name}.bin")
        if not os.path.exists(file_path) or self.enforce_owerwrite:
            with open(file_path,'wb') as f:
                self.write_string(f,table_name)
                self.write_int(f,len(fields))
                for field in fields:
                    self.write_string(f,field)
        else:
            raise Exception("Table already Exists")
        
    def insert_row(self, table_name, values):
        file_path = f'{self.directory}/{table_name}.bin'
        if os.path.exists(file_path):
            with open(file_path, 'ab') as f:
                self.write_int(f, len(values))
                for value in values:
                    self.write_string(f, str(value))
        else:
            raise Exception('Table does not exist')
        
    def select_rows(self, table_name, where_clause=None):
        file_path = f'{self.directory}/{table_name}.bin'
        rows = []
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                table_name_read = self.read_string(f)
                num_fields = self.read_int(f)
                fields = [self.read_string(f) for _ in range(num_fields)]
                # ? Problem is here fix it.It's going in inifinite loop
                while True:
                    try:
                        num_values = self.read_int(f)
                    except struct.error:
                        break
                    values = [self.read_string(f) for _ in range(num_values)]
                    row = dict(zip(fields, values))
                    if where_clause is None or where_clause(row):
                        rows.append(row)
        else:
            raise Exception('Table does not exist')
        return rows
            

    def write_int(self,f,value):
        self.buffer[:4] = struct.pack("i",value)
        f.write(self.buffer[:4])

    def write_string(self,f,value):
        encoded_value = value.encode('utf-8')
        value_length = len(encoded_value)
        self.write_int(f,value_length)
        f.write(encoded_value)

    def read_int(self,f):
        f.readinto(self.buffer[:4])
        return struct.unpack("i",self.buffer[:4])[0]
    
    def read_string(self,f):
        value_length = self.read_int(f)
        encoded_value = f.read(value_length)
        return encoded_value.decode("utf-8")

storage_engine = BinaryFileStorageEngine("data",enforce_overwrite=True)
storage_engine.create_table("users", ["id", "name", "email"])
storage_engine.insert_row("users", [1, "Alice", "alice@example.com"])
storage_engine.insert_row("users", [2, "Bob", "bob@example.com"])

rows = storage_engine.select_rows("users")
for row in rows:
    print(row["email"])

print("Execution Completed !!")