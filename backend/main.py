import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}



@app.post("/volatilityest/{symbol}/{est}")
def volest():
    return {"volest":"findall"}


