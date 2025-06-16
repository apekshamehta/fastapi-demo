import os
from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select
from api.db.session import get_session


from .models import EventModel,EventListSchema,EventCreateSchema,EventUpdateSchema
router = APIRouter()
from api.db.config import DATABASE_URL


#GET /api/events/
@router.get("/",response_model=EventListSchema)
async def read_events(session :Session=Depends(get_session)):
    # a bunch of items in a table
    query = select(EventModel).order_by(EventModel.id.asc()).limit(10)
    results = session.exec(query).all()
    print(os.environ.get("DATABASE_URL"),DATABASE_URL)
    return {
        "results" : results,
        "count" : len(results)
    }
    
    
#POST /api/events/
@router.post("/",response_model=EventModel)
async def create_event(
    payload: EventCreateSchema,
    session:Session=Depends(get_session)):
    # a single row
    print(payload)
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.get("/{event_id}",response_model=EventModel)
async def get_event(event_id: str,session:Session=Depends(get_session)):
    # a single row
    query = select(EventModel).where(EventModel.id == int(event_id))
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404,detail="Event not found")
    return result

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