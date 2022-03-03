from calendar import c
from time import process_time_ns
from traceback import print_tb
from pymongo import MongoClient
from bson.objectid import ObjectId
#conexion con la base de datos
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.VistazoAnimal
cont = 0
data_list = []
json_data = { 
    'animal0':{
        'nombre':'caiman',
        'tamanno': 400,
        'peso': 75,
        'nombre_especie': 'vulgaris secundis',
        'nombre_habitat': 'Acuario'
    },
    'animal1':{
        'nombre':'leopoldito',
        'tamanno': 500,
        'peso': 90,
        'nombre_especie': 'vulgaris secundis',
        'nombre_habitat': 'Desierto'
    }
}
data_list.append(json_data)
for d in data_list:
        #recuperar el id de de la especie
        filter_especie = {
            'nombre_cientifico' : d['animal' + str(cont)]['nombre_especie']
        }
        projection_especie = {
            '_id': 1
        }
        id_especie = db.especie.find_one(filter_especie,projection_especie)

        #recuperar el id del habitat
        filter_habitat = {
            'nombre' : d['animal' + str(cont)]['nombre_habitat']
        }

        projection_habitat = {
            '_id': 1
        }
        id_habitat = db.habitats.find_one(filter_habitat,projection_habitat)
        
        new_animal = {
            'nombre': d['animal' + str(cont)]['nombre'],
            'tamanno': d['animal' + str(cont)]['tamanno'],
            'peso': d['animal' + str(cont)]['peso'],
            'habitat_id': str(id_habitat),
            'especie_id': str(id_especie)
            }
            
        db.animales.insert_one(new_animal)
        cont = cont + 1
        print(d)