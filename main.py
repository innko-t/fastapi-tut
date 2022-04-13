from fastapi import FastAPI
from db.database import engine
from db import models


app = FastAPI()

@app.get("/")
def root():
    return 'Hello! Thid id tutorial!'

models.Base.metadata.create_all(engine)