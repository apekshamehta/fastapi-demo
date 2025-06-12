from typing import List,Optional
# from pydantic import BaseModel,Field
from sqlmodel import SQLModel,Field


"""
id 
path
description
"""

class EventModel(SQLModel,table=True):
    id: Optional[int] = Field(default=None,primary_key=True)
    # id:int
    page:Optional[str] = ""
    description:Optional[str] = ""

class EventCreateSchema(SQLModel):    
    
    page: str
    description:Optional[str] = Field(default="my description")

class EventUpdateSchema(SQLModel):
    description: str
    
# {"id":12}

class EventListSchema(SQLModel):
    itmes: List[EventModel]
    count: int