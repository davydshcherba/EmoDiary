from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from hashlib import sha256

from ..database import get_db
from .models import User
from .schemas import UserCreate, UserOut

router = APIRouter()

@router.get("/users", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = sha256(user.password.encode()).hexdigest()
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
