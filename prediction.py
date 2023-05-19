from PIL import Image
from io import BytesIO
import deepface
from deepface import DeepFace
from pydantic import BaseModel
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from dbconfig import get_etudiant
from pymongo import MongoClient
from bson.objectid import ObjectId

def predict_face(image_path):
        results = DeepFace.find(img_path =image_path, db_path = "C:/Users/pc/Desktop/fastapi_test/image",enforce_detection=False,model_name='VGG-Face')
        photo = list(map(lambda x: x['identity'],results))
        if not photo:
          return {"etudiant n existe pas"}
        else:
          url=photo[0][0]
          print(url)
          donne=get_etudiant(photo=url)
          return donne
      