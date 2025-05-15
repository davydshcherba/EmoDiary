from fastapi import FastAPI
from .database import Base, engine
from .auth.routers import router as auth_router

app = FastAPI()

# Створення таблиць у БД
Base.metadata.create_all(bind=engine)

# Підключення роутерів
app.include_router(auth_router, prefix="/auth", tags=["auth"])
