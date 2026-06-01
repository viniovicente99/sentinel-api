from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated
from db.database import sessionLocal


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]