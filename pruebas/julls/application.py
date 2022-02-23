#importamos flask
# from multiprocessing.connection import Client
from flask import Flask, request, abort, jsonify
from itsdangerous import json
from pymongo import MongoClient
from bson import json_util
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')

#instanciamos la clase , creamos un nuevo objeto y le pasamos el __name__
application = Flask(__name__)

# BBDD
mongodb = client.VistazoAnimal



# Buscar 1 animal
@application.route('/search_animal/<string:input_animal>', methods=['GET'])
def search_animal(input_animal):
    filter = {'nombre': input_animal}
    projection = {
        '_id': 0, 
        'id_habitat': 0,
        'id_especie': 0}

    animales = mongodb.animales.find(filter, projection)
    respuesta = json_util.dumps(animales)

    return respuesta











# SELECT nombre, apellido1 FROM usuarios WHERE apellido1 = 'pepito'
# 0 se muestra todo menos eso
# muestra lo que tiene 1
# projection es las columnas del select --> 0: no muestra, 1: muestra
# filter es el where
# loads: json a dict



#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



