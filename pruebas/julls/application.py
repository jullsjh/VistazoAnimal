#importamos flask
# from multiprocessing.connection import Client
from flask import Flask, request, abort, jsonify, Response
from itsdangerous import json
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')

#instanciamos la clase , creamos un nuevo objeto y le pasamos el __name__
application = Flask(__name__)

# BBDD
mongodb = client.VistazoAnimal


# -------------------------------- GET --------------------------------
# --------- ANIMALES
@application.route("/all_animals", methods=['GET'])
def all_animals():
    filter = {}
    projection = {
        '_id': 0, 
        'id_habitat': 0,
        'id_especie': 0}

    animales = list(mongodb.animales.find(filter, projection))
    for animal in animales:
        print(animal)
    
    return jsonify(animales), 200

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

@application.route('/animales/buscar_animal/<string:nombre>', methods=['GET'])
def buscar_animal(nombre):
    try:
        filter = {
            'nombre': nombre
        }  
        projection = {
        '_id': 0, 
        'id_habitat': 0,
        'id_especie': 0}

        # aqui esta en obj BSON
        animales = mongodb.animales.find(filter, projection)
        # json_util.dumps convierte los datos bson a json
        respuesta = json_util.dumps(animales)
        return respuesta

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400


@application.route('/search_animals_from_habitat/<string:nombre>', methods=['GET'])
# busco habitar por nombre
def search_animals_from_habitat(nombre):
    try: 
        # devuelve todos los datos de 1 habitar
        filter = {'nombre': nombre}
        habitats = mongodb.habitats.find_one(filter)
        # me quedo SOLO con el id_habitat de habitat buscado
        filter2 = {'id_habitat': habitats['id_habitat']}
        
        animales = mongodb.animales.find(filter2)
        respuesta = json_util.dumps(animales)
        return respuesta

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400










# --------- HABITATS
@application.route("/habitats/all_habitats", methods=['GET'])
def all_habitats():
    filter = {}
    projection = {'_id': 0}

    habitats = list(mongodb.habitats.find(filter, projection))
    for habitat in habitats:
        print(habitat)
    
    return jsonify(habitats), 200

@application.route('/habitats/buscar/<id>', methods=['GET'])
def buscar_habitat(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        habitats = mongodb.habitats.find(filter)
        respuesta = json_util.dumps(habitats)
        return respuesta

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400






# -------------------------------- POST --------------------------------
# --------- ANIMALES
@application.route('/animales/nuevo', methods=['POST'])
def new_animal():
    try: 
        nombre = request.json['nombre']
        new_animal = {
            'nombre': nombre,
            'tamanno': request.json['tamaño'],
            'peso': request.json['peso'],
            'id_habitat': request.json['id_habitat'],
            'id_especie': request.json['id_especie']
        }
        mongodb.animales.insert_one(new_animal)
        response = jsonify({'message': 'Animal con nombre: ' + nombre + ' --> Insertado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

# --------- HABITATS
@application.route('/habitats/nuevo', methods=['POST'])
def new_habitat():
    try: 
        nombre = request.json['nombre']
        new_habitat = {
            'nombre': nombre,
            'id_habitat': request.json['id_habitat']
        }
        mongodb.habitats.insert_one(new_habitat)
        response = jsonify({'message': 'Habitat con nombre: ' + nombre + ' --> Insertado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400





# -------------------------------- PUT --------------------------------
# --------- ANIMALES
@application.route('/animales/actualizar/<id>', methods=['PUT'])
def update_animal(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        update = {
            '$set': {
                'nombre': request.json['nombre'],
                'tamanno': request.json['tamaño'],
                'peso': request.json['peso'],
                'id_habitat': request.json['id_habitat'],
                'id_especie': request.json['id_especie']
            }
        }
        mongodb.animales.update_one(filter, update)
        response = jsonify({'message': 'Animal con id: ' + id + ' --> Actualizado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

# --------- HABBITATS
@application.route('/habitats/actualizar/<id>', methods=['PUT'])
def update_habitat(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        update = {
            '$set': {
                'nombre': request.json['nombre'],
                'id_habitat': request.json['id_habitat']
            }
        }
        mongodb.habitats.update_one(filter, update)
        response = jsonify({'message': 'Habitat con id: ' + id + ' --> Actualizado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400





# -------------------------------- DELETE --------------------------------
# --------- ANIMALES
@application.route('/animales/borrar_id/<id>', methods=['DELETE'])
def delete_animal_from_id(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        mongodb.animales.delete_one(filter)
        response = jsonify({'message': 'Animal con id: ' + id + ' --> Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/animales/borrar_nombre/<string:nombre>', methods=['DELETE'])
def delete_animal_from_name(nombre):
    try:
        filter = {
            'nombre': nombre
        }  
        mongodb.animales.delete_one(filter)
        response = jsonify({'message': 'El animal: ' + nombre + ' --> Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

# --------- HABITATS
@application.route('/habitats/borrar_id/<id>', methods=['DELETE'])
def delete_habitat_from_id(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        mongodb.habitats.delete_one(filter)
        response = jsonify({'message': 'Habitat con id: ' + id + ' --> Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400







# SELECT nombre, apellido1 FROM usuarios WHERE apellido1 = 'pepito'
# 0 se muestra todo menos eso
# muestra lo que tiene 1
# loads: json a dict
# projection es las columnas del select --> 0: no muestra, 1: muestra
# filter es el where





#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



