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


# -------------------------------- GET --------------------------------
# 1
@application.route("/all_animals", methods=['GET'])
def all_animals():
    # input_animal = 'bhjdawsvb' #input("Escribe nombre del animal que quieres buscar: \n")
    filter = {}
    projection = {
        '_id': 0, 
        'id_habitat': 0,
        'id_especie': 0}

    animales = list(mongodb.animales.find(filter, projection))
    for animal in animales:
        print(animal)
    
    return jsonify(animales), 200



# 2
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



# 3
@application.route('/search_animal_from_habitat/<string:input_habitat>', methods=['GET'])
def search_animal_for_habitat(input_habitat):
    filter = {'nombre': input_habitat}
    projection = {
        'id_habitat': 0}

    habitat = mongodb.habitats.find(filter, projection)
    respuesta = json_util.dumps(habitat)

    return respuesta



# --------- COMIDAS
# consultar comida
# consulta a 2 tablas: ej que ha comido el caiman?
@application.route('/comidas/<id>', methods=['GET'])
def comida_animal(input_comida):
    filter = { 'nombre': input_comida }
    projection = { }







# SELECT nombre, apellido1 FROM usuarios WHERE apellido1 = 'pepito'
# 0 se muestra todo menos eso
# muestra lo que tiene 1
# projection es las columnas del select --> 0: no muestra, 1: muestra
# filter es el where
# loads: json a dict



#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



