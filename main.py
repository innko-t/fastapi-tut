from fastapi import FastAPI
from db.database import engine
from db import models
from routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def root():
    return 'Hello! Thid id tutorial!'

models.Base.metadata.create_all(engine)