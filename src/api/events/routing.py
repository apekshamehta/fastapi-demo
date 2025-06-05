from fastapi import APIRouter
from .schema import EventSchema,EventListSchema
router = APIRouter()



# /api/events/
@router.get("/")
async def read_events() -> EventListSchema:
    # a bunch of items in a table
    return {
        "items" : [1,2,3]
    }
    
    


@router.get("/{event_id}", response_model=EventSchema)
async def get_event(event_id: str) -> EventSchema:
    # a single row
    return {
        "id" : event_id
    }