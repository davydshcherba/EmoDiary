from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .models import User

router = APIRouter()

@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
