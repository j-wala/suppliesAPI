from pymongo import MongoClient
from models.supply_model import SupplyItem


class DbOperations:
    def __init__(self, db:str):   
        self.client = MongoClient("mongo", 27017)
        self.db = self.client[db]
        
    def add_item_to_collection(self, collection: str, item: SupplyItem):
        col = self.db[collection]
        try:
            result = col.insert_one(item.model_dump())
            return {"success": True,
                    "result": result,
                    }
        except Exception as e:
            return {"success": False}
    