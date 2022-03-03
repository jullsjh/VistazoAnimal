from time import process_time_ns
from pymongo import MongoClient
from bson.objectid import ObjectId
#conexion con la base de datos
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.VistazoAnimal


filter = {
    '_id': ObjectId("621a8585c8771aa2cdd392cb")
}
projection = {
    'fecha': 1,
    'cantidad': 1
}
ventas = list(db.ventas.find(filter, projection))

user = db.usuarios.find_one(filter)

print(user['name'])