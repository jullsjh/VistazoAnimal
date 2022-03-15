from pymongo import MongoClient
from bson.objectid import ObjectId
#conexion con la base de datos
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.VistazoAnimal

# data_list = []
# json_data = [
#     {
#         'nombre':'lince',
#         'tamanno': 400,
#         'peso': 75,
#         'nombre_especie': 'mammalia',
#         'nombre_habitat': 'Acuario'
#     },
#     {
#         'nombre':'caiman',
#         'tamanno': 500,
#         'peso': 90,
#         'nombre_especie': 'amphibia',
#         'nombre_habitat': 'Desierto'
#     }
# ]

# for data in json_data:
#     #recuperar el id de de la especie
#     filter_especie = {
#         'nombre_cientifico' : data['nombre_especie']
#     }
#     projection_especie = {
#         '_id': 1
#     }
#     especie = db.especies.find_one(filter_especie, projection_especie)

#     #recuperar el id del habitat
#     filter_habitat = {
#         'nombre' : data['nombre_habitat']
#     }

#     projection_habitat = {
#         '_id': 1
#     }
#     habitat = db.habitats.find_one(filter_habitat, projection_habitat)
#     if especie is None or habitat is None:
#         print('fallo')
#         exit()
#     new_animal = { 
#         'nombre': data['nombre'],
#         'tamanno': data['tamanno'],
#         'peso': data['peso'],
#         'habitat_id': habitat['_id'],
#         'especie_id': especie['_id']
#         }
        
#     db.animales.insert_one(new_animal)
#     print(data)


# data = {
# 	"nombre": "Jairo",
# 	"apellido1": "Gutierrez",
# 	"apellido2": "Sivila",
# 	"especie_nombre": "vulgaris"
# }

# filter = {
#     'nombre': data['nombre'],
#     'apellido1':data['apellido1'],
#     'apellido2':data['apellido2']
# }
# projection  = {
# 'estado':1
# }
# #recuperamos todos los datos del veterinario
# veterinario = db.veterinarios.find_one(filter)
# #recuperamos la especie por el nombre
# filter_especie = {
# 'nombre_cientifico': data['especie_nombre']
# }
# projection_especie = {
#     '_id':1
# }
# especie = db.especie.find_one(filter_especie,projection_especie)
# print(veterinario)
# if veterinario['estado'] == "asignado":
#     print('Este veterinario ya esta asignado')
# else:
#     especie_id = especie['_id']
#     update = {'$set': {
#         'estado': 'asignado',
#         'especie_id': especie_id
#     }}
#     db.veterinarios.update_one(filter, update)
#     print('HA IDO BIEN')

id = "6230da7f302f789e1f7569ae"
filter = {
    '_id': ObjectId(id)
}
veterinary = db.veterinarios.find_one(filter)
print(veterinary)