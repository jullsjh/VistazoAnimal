from time import process_time_ns
from pymongo import MongoClient
from bson.objectid import ObjectId
#conexion con la base de datos
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.VistazoAnimal


#id = "6216848d3c7b5b70d315d5fe"       

#filter = {'_id': ObjectId(id)}
update = {'$set': {
            "nombre": "jairo",
            "apellido1": "Gutierrez",
            "apellido2": "Sivila",
            "email": "j@gmail.com",
            "telefono": "675134156",
            "pass": "jairo1234"   
        }}
#db.usuarios.update_one(filter, update)


filter = {'nombre': 'Pradera'}


habitat = list(db.habitats.find(filter))
for i in habitat:
    print (i)
