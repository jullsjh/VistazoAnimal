from time import process_time_ns
from pymongo import MongoClient
from bson.objectid import ObjectId
#conexion con la base de datos
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.VistazoAnimal

json_data = {
    'apellido1':'Munoz',
    'apellido2':'Manzanal',
    'email':'g@gmail.com',
    'telefono':'(699) 3263503',
    'pass':'guille1234',
    'type':1
}

filter = {
    '_id': ObjectId("6216025459fd2dd3f065d129")
}

if 'email' not in json_data:
    print("Nombre NO esta en data")
else:
    print("nombre SI esta en data")

user = db.usuarios.find_one(filter)
user_name = user['nombre']
print(user['nombre'])