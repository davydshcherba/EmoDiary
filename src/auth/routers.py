from fastapi import APIRouter, Depends
from .schemas import UserResponseSchema
from src.database import get_db
from .models import User
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("",response_model=list[UserResponseSchema])
async def get_users(db: Session=Depends(get_db)):
   users = db.query(User).all()
   return users

@router.post("")
async def create_user():
    ...

@router.get("/{user_id}")
async def get_user(user_id: int):
   ...