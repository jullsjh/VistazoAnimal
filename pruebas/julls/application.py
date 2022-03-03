#importamos flask
# from multiprocessing.connection import Client
from flask import Flask, request, abort, jsonify
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




#Buscar todos los animales de un habitat por nombre habitat
@application.route('/animals/<string:nombre>', methods=['GET'])
# @check_auth(UserRole.SUPERADMIN)
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



# -----------------------------------------------NUEVO: COMIDAS--------------------------------------------------------------------------------------

# -------------------------------- GET --------------------------------
@application.route("/comidas", methods=['GET'])
def all_comidas():
    filter = {}
    projection = {'_id': 0}

    comidas = list(mongodb.comidas.find(filter, projection))
    for comida in comidas:
        print(comida)
    
    return jsonify(comidas), 200


@application.route('/comidas/buscar/<id>', methods=['GET'])
def buscar_comida(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        comidas = mongodb.comidas.find(filter)
        respuesta = json_util.dumps(comidas)
        return respuesta

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400


# consultar que come un animal
@application.route('/animales/comida/<string:nombre>', methods=['GET'])
def search_comida_animal(nombre):
    try: 
        # devuelve todos los datos de 1 animal
        filter = {'nombre': nombre}
        animales = mongodb.animales.find_one(filter)
        # me quedo SOLO con el comida_id del animal buscado
        filter2 = {'comida_id': animales['comida_id']}
        projection = {
            '_id': 0, 
            'tamanno': 0,
            'peso': 0,
            'id_habitat': 0,
            'id_especie': 0
        }

        animales = mongodb.animales.find(filter2, projection)
        respuesta = json_util.dumps(animales)
        return respuesta

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400


# SIN TERMINAR xq necesitariamos añadir campo idAnimal en tabla comidas
# busco todos los animales que comen X comida
@application.route('/animales/misma_comida/<string:nombre>', methods=['GET'])
def search_animales_misma_comida(nombre):
    try: 
        # devuelve todos los datos de 1 animal
        filter = {'nombre': nombre}
        animales = mongodb.animales.find_one(filter)
        # me quedo SOLO con el comida_id del animal buscado
        filter2 = {'comida_id': animales['comida_id']}
        projection = {
            '_id': 0, 
            'tamanno': 0,
            'peso': 0,
            'id_habitat': 0,
            'id_especie': 0
        }

        animales = mongodb.animales.find(filter2, projection)
        respuesta = json_util.dumps(animales)
        return respuesta

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400





# -------------------------------- POST --------------------------------
@application.route('/comidas/nuevo', methods=['POST'])
def new_comida():
    try: 
        nombre = request.json['nombre']
        cantidad = request.json['cantidad']
        new_comida = {
            'nombre': nombre,
            'cantidad': cantidad
        }
        mongodb.comidas.insert_one(new_comida)
        response = jsonify({'message': 'Comida con nombre: ' + nombre + ' --> Insertado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400





# -------------------------------- PUT --------------------------------
@application.route('/comidas/actualizar/<id>', methods=['PUT'])
def update_comida(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        update = {
            '$set': {
                'nombre': request.json['nombre'],
                'cantidad': request.json['cantidad']
            }
        }
        mongodb.comidas.update_one(filter, update)
        response = jsonify({'message': 'Comida con id: ' + id + ' --> Actualizado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




# -------------------------------- DELETE --------------------------------
@application.route('/comidas/borrar_id/<id>', methods=['DELETE'])
def delete_comida_from_id(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        mongodb.comidas.delete_one(filter)
        response = jsonify({'message': 'Comida con id: ' + id + ' --> Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400








# SELECT nombre, apellido1 FROM usuarios WHERE apellido1 = 'pepito'
# 0 se muestra todo menos eso
# muestra lo que tiene 1
# projection es las columnas del select --> 0: no muestra, 1: muestra
# filter es el where
# loads: json a dict
# dumps: cualquier obj python a json



#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



