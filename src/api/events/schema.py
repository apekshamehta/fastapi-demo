from typing import List
from pydantic import BaseModel


class EventSchema(BaseModel):
    id: str
    

class EventListSchema(BaseModel):
    results: List[EventSchema]