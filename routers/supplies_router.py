from fastapi import APIRouter, UploadFile, File
from models.supply_model import SupplyItem, SupplyList

from util.db_ops import DbOperations 

router = APIRouter(prefix="/supplies")
db = DbOperations(db="supplies")

@router.get("/")
async def get_all_supplies():
    return {"message": "this da supolies router"}


@router.post("/one")
async def add_new_supply(item: SupplyItem):
    db.add_item_to_collection(item)
    return item.model_dump()


@router.post("/")
async def add_new_supply_items(items: SupplyList):
    for item in items:
        db.add_item_to_collection(item)
    return items.model_dump()