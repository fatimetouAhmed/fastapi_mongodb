from fastapi import FastAPI, File, UploadFile,HTTPException,Header
import uvicorn
#from prediction import read_image
from starlette.responses import JSONResponse
from prediction import predict_face
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import datetime
from dbconfig import etudiermat_collection,examun_collection
# etudiermat ,examun ,Base ,session,engine
from pymongo import MongoClient
from bson.objectid import ObjectId

app=FastAPI()



@app.get('/')
def hello_world():
    return "hello world"
@app.post('/api/predict')

async def predict_image(file :UploadFile=File(...)):
        image = await file.read()
        with open("image.jpg", "wb") as f:
            f.write(image)
        result = predict_face("image.jpg")
        return result 





if __name__== "__main__":
   uvicorn.run(app,port=8000 ,host='127.0.0.1')