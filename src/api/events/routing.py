import os
from fastapi import APIRouter,Depends
from sqlmodel import Session
from api.db.session import get_session


from .models import EventModel,EventListSchema,EventCreateSchema,EventUpdateSchema
router = APIRouter()
from api.db.config import DATABASE_URL


#GET /api/events/
@router.get("/")
async def read_events() -> EventListSchema:
    # a bunch of items in a table
    print(os.environ.get("DATABASE_URL"),DATABASE_URL)
    return {
        "itmes" : [{"id":1},{"id":2},{"id":3}],
        "count" : 3
    }
    
    
#POST /api/events/
@router.post("/",response_model=EventModel)
async def create_event(
    payload: EventCreateSchema,
    session:Session=Depends(get_session)):
    # a single row
    print(payload)
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.get("/{event_id}")
async def get_event(event_id: str) -> EventModel:
    # a single row
    return {
        "id" : event_id
    }

@router.put("/{event_id}")
async def update_event(event_id: int, payload: EventUpdateSchema) -> EventModel:
    # a single row
    print(event_id)
    print("--------------------------------next is payload--------------------------------")
    print(payload)
    data = payload.model_dump()
    return {
        "id" : event_id,   **data
    }

# @router.delete("/{event_id}", response_model=EventSchema)
# async def delete_event(event_id: str) -> EventSchema:
#     # a single row
#     return {
#         "id" : event_id
#     }