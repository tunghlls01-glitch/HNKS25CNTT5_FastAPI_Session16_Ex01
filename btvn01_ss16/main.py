from fastapi import FastAPI
import models
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def check_api():
    return {
        "API chạy ok"
    }





