from fastapi import FastAPI
import pymongo
app = FastAPI()
client = pymongo.MongoClient("mongodb://localhost:27017") 
db = client.iscae
@app.get("/") 
def get_documents():
    documents = db.etudiant.find()

    noms_filieres = []
    for document in documents:
      nom_filiere = document["nom"]
      print(nom_filiere)
      noms_filieres.append(nom_filiere)
    return {"nom filiere ": noms_filieres}
      #print(noms_filieres)
    # if(documents):
    # # return {"documents": documents}
    #  return noms_filieres