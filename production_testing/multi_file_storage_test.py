import sys
from pathlib import Path
sys.path.append(fr"{Path(__file__).parent.parent}")
# sys.path.append(r"E:\Python_Proj\database_creation")

from storage import MultiFileStorageEngine
multi_file_storage = MultiFileStorageEngine()



multi_file_storage.create_multiple_tables(table1=['col1','col2','col3'],table2=['col1','col2','col3'],table3=['col1','col2','col3'])

multi_file_storage.insert_multiple_row(table1=['val1','val2','val3'],table2 =['val1','val2','val3'])
multi_file_storage.insert_multiple_row(table3=['val1','val2','val3'],table2 =['val1','val2','val3'])
multi_file_storage.insert_multiple_row(table1=['val1','val2','val3'],table3 =['val1','val2','val3'])

try:
    multi_file_storage.insert_multiple_row(table1=['val1','val2','val3'],table4 =['val1','val2','val3'])
except Exception as e:
    print(str(e))

print(multi_file_storage.read_table(table_name='table1',lines_to_read=2))

print("Execution Completd")


