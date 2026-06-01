from pydantic import BaseModel, field_validator, Field, IPvAnyAddress
from typing import Optional
from uuid import UUID
from datetime import date, datetime

class PayloadSchema(BaseModel):
    source: str = Field(..., min_length=1)
    event_type: str = Field(..., min_length=1)
    ip: IPvAnyAddress
    username: str = Field(..., min_length=1)
    timestamp: date

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, v):
        if v > date.today():
            raise ValueError("A data do timestamp não pode ser no futuro.")
        return v

class EventItem(BaseModel):
    source: str = Field(..., min_length=1)
    event_type: str = Field(..., min_length=1)
    ip: IPvAnyAddress
    username: str = Field(..., min_length=1)
    timestamp: date

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, v):
        if v > date.today():
            raise ValueError("A data do timestamp não pode ser no futuro.")
        return v

class EventItemResponse(BaseModel):
    id: UUID
    source: str = Field(..., min_length=1)
    event_type: str = Field(..., min_length=1)
    ip: IPvAnyAddress
    username: str = Field(..., min_length=1)
    timestamp: date
    country: str = Field(..., min_length=1)
    country_code: str = Field(..., min_length=1)
    region: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    latitude: float = Field(go=-90.0, le=90.0)
    longitude: float = Field(go=-90.0, le=90.0)
    isp: str = Field(..., min_length=1)
    raw_payload: PayloadSchema
    created_at: datetime

class EventItemPatch(BaseModel):
    source: Optional[str] = Field(None, min_length=1)
    event_type: Optional[str] = Field(None, min_length=1)
    ip: Optional[IPvAnyAddress] = None
    username: Optional[str] = Field(None, min_length=1)
    timestamp: Optional[date] = None
    country: Optional[str] = Field(None, min_length=1)
    country_code: Optional[str] = Field(None, min_length=1)
    region: Optional[str] = Field(None, min_length=1)
    city: Optional[str] = Field(None, min_length=1)
    latitude: Optional[float] = Field(None, ge=-90.0, le=90.0)
    longitude: Optional[float] = Field(None, ge=-180.0, le=180.0)
    isp: Optional[str] = Field(None, min_length=1)
    raw_payload: Optional[dict] = None
    
