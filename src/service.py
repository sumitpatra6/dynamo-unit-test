import uuid
from src.db import DB
class Service:
    def __init__(self) -> None:
        self.db = DB()

    def create_date(self):
        items = [{
            'id' : uuid.uuid4().hex,
            'name' : 'Sumit'
        },
        {
            'id' : uuid.uuid4().hex,
            'name' : 'Sweta'
        }
        ]
        self.db.save_date(items)

    def get_data(self):
        self.db.get_items()

    def query(self, id):
        self.db.query(id)