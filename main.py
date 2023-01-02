from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
import uuid

app = FastAPI()

db = []

@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    contents = await file.read() 

    db.append(file)

    with open(file.filename, "wb") as f:
        f.write(contents)

    return {"filename": file.filename}

@app.get("/images/")
async def show_image():  
     return db[0]
