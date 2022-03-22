from typing import Optional
from fastapi import FastAPI
import os
from honey import txt_finder

app = FastAPI()
directory = os.listdir(path=".")
test_dict = {0: "honeypot1", 1: "honeypot2", 2: "honeypot3"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/honeypots/")
def read_items(item_name: str):
    
    if item_name in test_dict.values():
        return {item_name}
    else:
        return {"nope"}

# @app.post("/files/")
# async def create_file(file: bytes = File(...)):
# #     return {"file_size": len(file)}

# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}