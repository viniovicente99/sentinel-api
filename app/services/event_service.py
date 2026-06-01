from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.event_model import SecurityEvent
from schemas.event_schema import EventItemResponse, EventItem, EventItemPatch
from uuid import UUID
from fastapi import HTTPException
from integrations.ip_api import get_geo_location
from schemas.geo_location_schema import GeoLocationSchema

def list_events(db: Session):
    return db.query(SecurityEvent).all()


def get_event(db: Session, id: UUID ):
    security_event = db.query(SecurityEvent).filter(SecurityEvent.id == id).first()
    if not security_event:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")
    return security_event


def create(db: Session, event: EventItem):

    event_dict = event.dict()
    event_dict["ip"] = str(event_dict["ip"])
    new_event = SecurityEvent(**event_dict)

    try:
        geo_data = get_geo_location(new_event.ip)
        geo = GeoLocationSchema(**geo_data)

        new_event.country = geo.country
        new_event.country_code = geo.country_code
        new_event.region = geo.region
        new_event.city = geo.city
        new_event.latitude = geo.latitude
        new_event.longitude = geo.longitude
        new_event.isp = geo.isp

    except Exception as e:
        new_event.country = "None"
        new_event.country_code = "None"
        new_event.region = "None"
        new_event.city = "None"
        new_event.latitude = 0.0
        new_event.longitude = 0.0
        new_event.isp = "None"

        print(f"[ERROR] - Geo API falhou: {e}")

    try: 
        payload = event.dict()

        payload["ip"] = str(payload["ip"])
        payload["timestamp"] = payload["timestamp"].isoformat()

        new_event.raw_payload = payload

        db.add(new_event)
        db.commit()
        db.refresh(new_event)
    
    except SQLAlchemyError as e:         
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao cadastrar evento")    

    return EventItemResponse.model_validate(new_event, from_attributes=True)


def edit(db: Session, id: UUID, event_update: EventItemPatch):

    try:
        db_event = db.query(SecurityEvent).filter(SecurityEvent.id == id).first()
        if not db_event:
            raise HTTPException(status_code=404, detail="Evento não encontrado.")
        
        updated_data = event_update.model_dump(exclude_unset=True)

        if "ip" in updated_data:
            updated_data["ip"] = str(updated_data["ip"])

        for field, value in updated_data.items():
            setattr(db_event, field, value)

        db.commit()
        db.refresh(db_event)

    except SQLAlchemyError as e:         
            db.rollback()
            print(f"[ERROR] - Erro ao editar evento: {e}")
            raise HTTPException(status_code=500, detail="Erro ao editar evento")

    return db_event   


def delete(db: Session, id: UUID):

    db_event = db.query(SecurityEvent).filter(SecurityEvent.id == id).first()

    if not db_event:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    try:       
        db.delete(db_event)
        db.commit()

    except SQLAlchemyError as e:         
        db.rollback()
        print(f"[ERROR] - Erro ao excluir evento: {e}")
        raise HTTPException(status_code=500, detail="Erro ao excluir evento")   
        
    return {"message": "Evento excluído com sucesso."}

        

   
    



