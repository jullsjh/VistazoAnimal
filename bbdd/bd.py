from pymongo import MongoClient

#conexion con la base de datos
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.VistazoAnimal

users = list(db.usuarios.find())

filter = {
        'nombre': 'Doro'
    }
projection = {
        'pass': 0
    }
        #print(id)
user = db.usuarios.find_one(filter,projection)
print(user)