from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
import os
from random import randint
import uuid

app = FastAPI()

db = []


@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    db.append(contents)

    return {"filename": file.filename}
