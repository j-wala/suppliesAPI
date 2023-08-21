from pydantic import BaseModel
from datetime import datetime
from typing import List
from fastapi import UploadFile

class SupplyItem(BaseModel):
    name:str
    category:str
    bestBefore:datetime | None = None
    # photo:UploadFile | None = None
    
    
class SupplyList(BaseModel):
    supplies: List[SupplyItem]