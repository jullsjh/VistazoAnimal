from calendar import c
from time import process_time_ns
from traceback import print_tb
from pymongo import MongoClient
from bson.objectid import ObjectId
#conexion con la base de datos
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.VistazoAnimal

data_list = []
json_data = [
    {
        'nombre':'lince',
        'tamanno': 400,
        'peso': 75,
        'nombre_especie': 'mammalia',
        'nombre_habitat': 'Acuario'
    },
    {
        'nombre':'caiman',
        'tamanno': 500,
        'peso': 90,
        'nombre_especie': 'amphibia',
        'nombre_habitat': 'Desierto'
    }
]

for data in json_data:
    #recuperar el id de de la especie
    filter_especie = {
        'nombre_cientifico' : data['nombre_especie']
    }
    projection_especie = {
        '_id': 1
    }
    especie = db.especies.find_one(filter_especie, projection_especie)

    #recuperar el id del habitat
    filter_habitat = {
        'nombre' : data['nombre_habitat']
    }

    projection_habitat = {
        '_id': 1
    }
    habitat = db.habitats.find_one(filter_habitat, projection_habitat)
    if especie is None or habitat is None:
        print('fallo')
        exit()
    new_animal = { 
        'nombre': data['nombre'],
        'tamanno': data['tamanno'],
        'peso': data['peso'],
        'habitat_id': habitat['_id'],
        'especie_id': especie['_id']
        }
        
    db.animales.insert_one(new_animal)
    print(data)