from typing import List
from pydantic import BaseModel

class EventCreateSchema(BaseModel):
    id: int
    


class EventSchema(BaseModel):
    id: int
    

class EventListSchema(BaseModel):
    itmes: List[EventSchema]
    count: int