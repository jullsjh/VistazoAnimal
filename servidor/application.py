#importamos flask
# from multiprocessing.connection import Client
from flask import Flask, request, abort, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')

#instanciamos la clase , creamos un nuevo objeto y le pasamos el __name__
application = Flask(__name__)

# BBDD
mongodb = client.VistazoAnimal


# ----------------------------- ANIMALES -----------------------------
# Devuelve TODOS los animales
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




# Buscar 1 animal
input_animal = input("Escribe nombre del animal que quieres buscar: \n")

@application.route("/", methods=['GET'])
def search_animal():
    filter = {'name': input_animal}
    projection = {
        '_id': 0, 
        'id_habitat': 0,
        'id_especie': 0}

    animales = list(mongodb.animales.find(filter, projection))
    for animal in animales:
        print(animal)
    
    # return jsonify(animales), 200
    return animales


# ----------------------------- USUARIOS -----------------------------






# 0 se muestra todo menos eso
# muestra lo que tiene 1
# projection es las columnas del select --> 0: no muestra, 1: muestra
# filter es el where





#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



