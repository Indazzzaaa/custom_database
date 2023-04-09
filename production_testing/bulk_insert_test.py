
from pathlib import Path
import sys
import random
path = Path(__file__).parent.parent
sys.path.append(fr"{path}")

from storage import FileStorageEngine
simple_storage = FileStorageEngine(Path(__file__).parent)
simple_storage.create_table(table_name='test1',fields=['col1','col2','col3'])


one_million_data = 1_000_000
bulk_data = ([f"val1_{random.randint(1,100)}",f"val2_{random.randint(1,100)}",f"val3_{random.randint(1,100)}"] for i in range(one_million_data))
simple_storage.insert_bulk(table_name='test1',bulk_data=bulk_data)
print("Execution completed !!")



