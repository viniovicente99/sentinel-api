from sqlalchemy import Column, String, Date, DateTime, DOUBLE_PRECISION
from sqlalchemy.dialects.postgresql import JSONB
from db.database import Base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

class SecurityEvent(Base):
    __tablename__ = 'security_events'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source = Column(String, index=True)
    event_type = Column(String, index=True)
    ip = Column(String)
    username = Column(String)
    timestamp = Column(Date)
    country = Column(String)
    country_code = Column(String)
    region = Column(String)
    city = Column(String)
    latitude = Column(DOUBLE_PRECISION)
    longitude= Column(DOUBLE_PRECISION)
    isp = Column(String)
    raw_payload = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)

