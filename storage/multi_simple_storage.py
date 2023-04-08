from .simple_storage import FileStorageEngine
from pathlib import Path

class MultiFileStorageEngine(FileStorageEngine):
    def __init__(self, directory=Path(__file__).parent.parent.joinpath('Data'), enforce_overwrite=True):
        super().__init__(directory, enforce_overwrite)

    # pass the dictionary of table name and table headings
    def create_multiple_tables(self, **kwargs):
        for table_tuple  in kwargs.items():
            super().create_table(table_name=table_tuple[0],fields=table_tuple[1])

    def insert_multiple_row(self,**kwargs):
        for table_tuple in kwargs.items():
            super().insert_row(table_name=table_tuple[0],values=table_tuple[1])


