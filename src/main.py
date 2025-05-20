from fastapi import FastAPI
from .database import Base, engine
from .auth.routers import router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router,prefix="/auth",tags=["auth"])