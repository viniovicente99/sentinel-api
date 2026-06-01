from fastapi import APIRouter
from services.event_service import get_event, list_events, create, edit, delete
from db.session import db_dependency
from uuid import UUID
from schemas.event_schema import EventItemResponse, EventItem, EventItemPatch
from typing import List

router = APIRouter(prefix="/events")

@router.get("", response_model=List[EventItemResponse])
def list_all_events(db: db_dependency):
    return list_events(db)

@router.get("/{id}", response_model=EventItemResponse)
def get_event_by_id(db: db_dependency, id: UUID):
    return get_event(db, id)

@router.post("", response_model=EventItem)
def create_event(db: db_dependency, event: EventItem ):
    return create(db, event)

@router.patch("/{id}")
def edit_event(db: db_dependency, id: UUID, event: EventItemPatch):
    return edit(db, id, event)

@router.delete("/{id}")
def delete_event(db: db_dependency, id: UUID):
    return delete(db, id)