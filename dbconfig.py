from PIL import Image
# from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from io import BytesIO
import deepface
from deepface import DeepFace
from datetime import datetime
import pymongo
# app = FastAPI()
client = pymongo.MongoClient("mongodb://localhost:27017") 
db = client.iscae
class Etudiant:
    def __init__(self, nom, prenom, email, photo, genre, date_N, lieu_n, telephone, nationalite, date_inscription):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.photo = photo
        self.genre = genre
        self.date_N = date_N
        self.lieu_n = lieu_n
        self.telephone = telephone
        self.nationalite = nationalite
        self.date_inscription = date_inscription

    def save(self):
        etudiant_collection.insert_one(self.__dict__)

    @staticmethod
    def find_by_photo(photo):
        return etudiant_collection.find_one({"photo": photo})


# departement
class Departement:
    def __init__(self, nom):
        self.nom = nom
        self.filiere = []

    def save(self):
        departement_collection.insert_one(self.__dict__)


# filiere
class Filiere:
    def __init__(self, nom, description, id_dep):
        self.nom = nom
        self.description = description
        self.id_dep = id_dep
        self.semestre = []

    def save(self):
        filiere_collection.insert_one(self.__dict__)


# matiere
class Matiere:
    def __init__(self, titre, description, credit):
        self.titre = titre
        self.description = description
        self.credit = credit
        self.examun = []

    def save(self):
        matiere_collection.insert_one(self.__dict__)


# examun
class Examun:
    def __init__(self, type, heure_deb, heure_fin, id_mat, id_sal):
        self.type = type
        self.heure_deb = heure_deb
        self.heure_fin = heure_fin
        self.id_mat = id_mat
        self.id_sal = id_sal

    def save(self):
        examun_collection.insert_one(self.__dict__)


# salle
class Salle:
    def __init__(self, nom):
        self.nom = nom
        self.examun = []

    def save(self):
        salle_collection.insert_one(self.__dict__)


# semestre
class Semestre:
    def __init__(self, nom, id_fil):
        self.nom = nom
        self.id_fil = id_fil
        self.sem_etu = []

    def save(self):
        semestre_collection.insert_one(self.__dict__)


# sem_etu
class SemEtu:
    def __init__(self, id_sem, id_etu):
        self.id_sem = id_sem
        self.id_etu = id_etu

    def save(self):
        sem_etu_collection.insert_one(self.__dict__)


# etudier_matiere
class EtudierMat:
    def __init__(self, id_mat, id_etu):
        self.id_mat = id_mat
        self.id_etu = id_etu

    def save(self):
        etudiermat_collection.insert_one(self.__dict__)


# Get collection references
etudiant_collection = db["etudiant"]
departement_collection = db["departement"]
filiere_collection = db["filiere"]
matiere_collection = db["matiere"]
examun_collection = db["examun"]
salle_collection = db["salle"]
semestre_collection = db["semestre"]
sem_etu_collection = db["sem_etu"]
etudiermat_collection = db["etudiermat"]
def get_exams():
    id_etu = 1
    now = datetime.now()
    print(now)
    subquery = {
        'id_etu': id_etu
    }
    exams = db.examun.find({
        'heure_deb': {'$lte': now},
        'heure_fin': {'$gte': now},
        'id_mat': {'$in': db.etudiermat.distinct('id_mat', subquery)}
    })

    return list(exams)


# @app.get("/") 
def get_etudiant(photo:str):
#     print(photo)
  etudiant = db.etudiant.find_one({"photo": photo})
#   etudiant_json = jsonable_encoder(etudiant)
#   return etudiant_json
# #     etudiant = db.etudiant.findOne({"photo": photo})
# #     return {"nom filiere ": etudiant}
  if etudiant:
        id_etu = etudiant['_id']
        now = datetime.now()
        print(now)
        exams = db.examun.find({
            'heure_deb': {'$lte': now},
            'heure_fin': {'$gte': now},
            'matiere.etudiant.id': id_etu
        })

        if len(list(exams)) == 0:
            return "Votre examun n'est pas à ce moment"
        else:
            return "Rentrez"




