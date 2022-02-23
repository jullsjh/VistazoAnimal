from turtle import update
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
# bbdd
mongodb = client.python2a


user = mongodb.find_one

filter = {'name': 'Pepe'}
projection = {'name': 1, 'direccion': 1}


# -------------------------- PARA BUSCAR --------------------------
users = list(mongodb.test.find(filter, projection))
for user in users:
    print(user)


# # -------------------------- PARA INSERTAR DOC ENTERO --------------------------
# # Si no existe el documento, crea uno nuevo
# new_user = {
#     'nick': 'admin',
#     'pass': 'abcd'
# }
# # users si no existe crea una coleccion nueva con ese nombre que le hemos dado,
# # entonces si cualquier coleccion no existe podemos crearla con el nombre que pongamos ahi
# # IF compruebo si ha ido bien
# result = mongodb.users.insert_one(new_user)
# if result.inserted_id:
#     print(result.inserted_id)

# # -------------------------- PARA BORRAR 1 --------------------------
# # filter = {'nick': 'admin'}
# # mongodb.users.delete_one(filter)


# # -------------------------- PARA ACTUALIZAR --------------------------
# # Tambien sirve para añadir campos que no existen
#     # $set --> cuando no existe un valor y añadirlo || $unset --> para borrar
# filter = {'nick': 'admin'}
# update = {'$set': {'admin': True, 'email': 'yo@yo.com'}}
# mongodb.users.update_one(filter, update)



