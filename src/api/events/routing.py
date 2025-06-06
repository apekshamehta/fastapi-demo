from fastapi import APIRouter
from .schema import EventSchema,EventListSchema
router = APIRouter()

# GET DATA HERE
# LIST VIEW
# GET /api/events/
@router.get("/")
async def read_events() -> EventListSchema:
    # a bunch of items in a table
    return {
        "itmes" : [{"id" : 1}, {"id" : 2}, {"id" : 3}],
        "count" : 3
    }
    
    
# SEND DATA HERE
# CREATE VIEW
# POST /api/events/
@router.post("/")
async def create_events(data:dict = {}):
    # a bunch of items in a table
    print(data)
    return data

# GET /api/events/12
@router.get("/{event_id}")
async def get_event(event_id: str) -> EventSchema:
    # a single row
    return {
        "id" : event_id
    }
    

# Update this data
# PUT /api/events/12
@router.put("/{event_id}")
async def update_event(event_id: str,payload:dict = {}) -> EventSchema:
    # a single row
    return {
        "id" : event_id
    }
    
#     # GET/api/events/12
# @router.delete("/{event_id}")
# async def delete_event(event_id: str) -> EventSchema:
#     # a single row
#     return {
#         "id" : event_id
#     }