from typing import Optional
from fastapi import FastAPI
import os
from honey import txt_finder

app = FastAPI()
directory = os.listdir(path=".")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_items(items_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}