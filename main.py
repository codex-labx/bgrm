from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
# import uvicorn
from PIL import Image
import io
from app import Removebg

app = FastAPI()

def save_image(image):
    with open('uploaded.png', "wb") as f:
        f.write(image)

@app.get('/')
def remove():
    return 'RemoveBG Powered by Zandora, Kindly visit /removebg to remove background of images.'

@app.post('/removebg')
async def removebg(file: UploadFile = File(...)):
    image = await file.read()
    save_image(image)
    resp = Removebg('uploaded.png')
    img = Image.open(resp)
    img.save('bgremoved.png')
    file = open('bgremoved.png', mode="rb")

    return StreamingResponse(file, media_type="image/png")


# if __name__=="__main__":
#     uvicorn.run(app, port=5000, host='127.0.0.1')
