#importamos flask
# from multiprocessing.connection import Client
import os, json, jwt,requests
from flask import Flask, request, abort, jsonify
from itsdangerous import json
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
from enum import IntEnum
from functools import wraps
from datetime import datetime, timedelta


client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')

#instanciamos la clase , creamos un nuevo objeto y le pasamos el __name__
application = Flask(__name__)
# BBDD
db = client.VistazoAnimal
# variables globales para todo
token_user = None
headers={}

TOKEN_KEY = 'top-secret'

#Permisos de cada rol
#-Superadmin puede realizar todas los requests
#-Empleado puede recuperar,crear y editar todas las colecciones
#-Usuario puede registrar ventas y recuperar todas las colecciones
class UserRole(IntEnum):
    SUPERADMIN = 1
    EMPLEADO = 5
    USUARIO = 100



#comprobacion del token de autorizacion
def check_auth(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kargs):
            token = request.headers['Authorization']
            token = token.split()[1]
            try:
                token_data = jwt.decode(token, TOKEN_KEY, algorithms=['HS256'])
            except Exception as e:
                print(str(e))
                abort(401)
            if token_data['type'] > role:
                return jsonify({'ERROR':'No tienes los permisos necesarios'}), 400
            return f(token_data['id'], *args, **kargs)
        return wrapper
    return decorator

@application.route("/login", methods=['POST'])
def login():
    try:
        data= request.get_json()
        email = data['email']
        password = data['pass']
        #hashed_password = generate_password_hash(password)
        filter = {
            'email': email,
            'pass': password
        }
        user = db.usuarios.find_one(filter)
        if user:
            token_data = {
                'id': str(user['_id']),
                'exp': datetime.utcnow() + timedelta(seconds=10800),
                'type': user['type']
            }
            token = jwt.encode(token_data, TOKEN_KEY, algorithm='HS256')
            return jsonify({'token':token}), 200
        else:
            return jsonify({'ERROR':'No se ha podido iniciar sesión, correo/contraseña incorrectos'}), 401
    except Exception as e:
        return jsonify({'ERROR': 'No se ha podido iniciar sesión','ERROR_2':str(e)}), 400











# -------------------------------- ANIMALES --------------------------------
@application.route("/animals", methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def get_animals(user_id):
    try:
        animales = list(db.animales.find())
        respuesta = json_util.dumps(animales)

        if animales:
            return respuesta, 200
        else:
            return jsonify({'ERROR': 'No se ha podido recuperar los animales'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'Error2': str(e)}), 400

# falta!!!!!!!!!!
@application.route('/animals/search/<string:input_animal>', methods=['GET'])
@check_auth(UserRole.USUARIO)
def search_animal(user_id,input_animal):
    try:
        filter = {'nombre': input_animal}
        animales = db.animales.find(filter)
        if animales:
            respuesta = json_util.dumps(animales)
            return respuesta
        else:
            return jsonify({'ERROR': 'No se ha podido encontrar el animal introducido'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/animals', methods=['POST'])
@check_auth(UserRole.SUPERADMIN)
def new_animal(user_id):
    try:
        #Comprobacion de que no existe el animal
        data = request.get_json()
        filter_rep = {
            'nombre': data['nombre']
        }
        busqueda = db.animales.find_one(filter_rep)
        if busqueda:
            return jsonify({'message': 'Animal ya existente intentelo de nuevo'}), 400
        else:
            # busca por nombre_especie para traer TODOS los datos
            especie = db.especie.find_one({'nombre_cientifico':data['nombre_especie']})
            habitat = db.habitats.find_one({'nombre':data['nombre_habitat']})
            new_animal = {
                'nombre': data['nombre'],
                'tamanno': data['tamanno'],
                'peso': data['peso'],
                'habitat_id': habitat['_id'],
                'especie_id': especie['_id'] #al tener todos los datos me quedo con id 
            }
            db.animales.insert_one(new_animal)
            nombre = data['nombre']
            return jsonify({'message': 'Animal con nombre: ' + nombre + ' Insertado Correctamente'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/animals/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
def update_animal(user_id, id):
    try:
        data = request.get_json()
        filter = {
            '_id': ObjectId(str(id))
        }
        # busca por nombre
        especie = db.especie.find_one({'nombre_cientifico':data['nombre_especie']})
        habitat = db.habitats.find_one({'nombre':data['nombre_habitat']})
        update = {
            '$set': {
                'nombre': data['nombre'],
                'tamanno': data['tamanno'],
                'peso': data['peso'],
                'especie_id': especie['_id'],
                'habitat_id': habitat['_id']
            }
        }
        db.animales.update_one(filter, update)
        response = jsonify({'message': 'Comida con id: ' + id + ' --> Actualizado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/animals/search/<id>', methods=['DELETE'])
@check_auth(UserRole.EMPLEADO)
def delete_animal_byId(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        busqueda = db.animales.delete_one(filter)
        if busqueda:
            response = jsonify({'message': 'Animal con id:  ' + id + ' Ha sido eliminado Correctamente'})
            response.status_code = 200
            return response
        else:
            return jsonify({'ERROR': 'ID introducido no existe'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



# -------------------------------- HABITATS --------------------------------
@application.route("/habitats", methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def get_habitats(user_id):
    try:
        habitats = list(db.habitats.find())
        if habitats:
            respuesta = json_util.dumps(habitats)
            return respuesta, 200
        else:
            return jsonify({'ERROR': 'No se ha podido recuperar los habitats'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR2': str(e)}), 400

@application.route('/habitat', methods=['POST'])
@check_auth(UserRole.SUPERADMIN)
def create_habitat(user_id):
    try:
        data = request.get_json()
        filter = {
            'nombre': data['nombre']
        }
        habitat = db.habitats.find_one(filter)
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if habitat :
            return  jsonify({'ERROR': 'No se pudo crear el nuevo habitat ya existe uno con ese nombre'})
        else:
            nuevo_habitat =  {
                'nombre': data['nombre']
                }
            db.habitats.insert_one(nuevo_habitat)
            response = jsonify({'message': 'Habitat con nombre: ' + data['nombre'] + ' Fue creado correctamente'})
            response.status_code = 201
            return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'ERROR_2': str(e)}), 400

@application.route('/habitat/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
def update_habitat(user_id, id):
    try:
        data = request.get_json()
        filter = {
            '_id': ObjectId(str(id))
        }
        habitat = db.habitats.find_one(filter)
        data = request.get_json()
        if 'nombre' not in data:
            nombre = habitat['nombre']
        else:
            nombre = data['nombre']
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if nombre :
            update = {'$set': {
                'nombre': nombre
                }}
            db.habitats.update_one(filter, update)
            response = jsonify({'message': 'habitat con ' + id + ' Fue actualizado correctamente'})
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo modificar el usuario, faltan datos para crear el usuario'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'ERROR': str(e)}), 400

@application.route('/habitat/<id>', methods=['DELETE'])
@check_auth(UserRole.SUPERADMIN)
def delete_habitat_by_Id(user_id, id):
    try:
        filter = {
            '_id': ObjectId(str(id))
        }
        habitat = db.habitats.delete_one(filter)
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if habitat :
            response = jsonify({'message': 'Habitat con ' + id + ' Fue eliminado correctamente'})
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo eliminar el habitat'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'ERROR2': str(e)}), 400



# -------------------------------- COMIDAS --------------------------------
@application.route("/food", methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def get_foods(user_id):
    try:
        comidas = list(db.comida.find())
        if comidas:
            return json_util.dumps(comidas), 200
        else:
            return jsonify({'ERROR': 'No se han podido obtener datos de la comida'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'ERROR2': str(e)}), 400

@application.route('/food', methods=['POST'])
@check_auth(UserRole.EMPLEADO)
def new_food(user_id):
    try:
        nombre = request.json['nombre']
        cantidad = request.json['cantidad']
        busqueda = db.comida.find_one({'nombre':nombre})
        if busqueda:
            return jsonify({'ERROR': 'No se pudo crear una nueva comida, comida ya existente'}), 400
        else:
            new_comida = {
                'nombre': nombre,
                'cantidad': cantidad
            }
            insert = db.comida.insert_one(new_comida)
            if insert.inserted_id:
                response = jsonify({'message': 'Comida con nombre: ' + nombre + ' --> Insertado Correctamente'})
                response.status_code = 200
                return response
            else:
                return jsonify({'ERROR': 'No se pudo crear una nueva comida'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/food/<id>', methods=['PUT'])
@check_auth(UserRole.EMPLEADO)
def update_food(user_id,id):
    try:
        data = request.get_json()
        filter = {
            '_id': ObjectId(id)
        }
        update = {
            '$set': {
                'nombre': data['nombre'],
                'cantidad': data['cantidad']
            }
        }
        db.comida.update_one(filter, update)
        response = jsonify({'message': 'Comida con id: ' + id + ' --> Actualizado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/food/specie', methods=['PUT'])
@check_auth(UserRole.EMPLEADO)
def givefood_animal(user_id):
    try:
        data = request.get_json()
        animal = db.animales.find_one({'nombre':data['nombre_animal']})
        especie = db.especie.find_one({'_id':animal['especie_id']})
        comida = db.comida.find_one({'_id':especie['comida_id']})
        filter = {
            '_id': ObjectId(comida['_id'])
        }
        cantidad_int = int(comida['cantidad'])
        cantidad_int = cantidad_int - 10
        update = {
            '$set': {
                'cantidad': cantidad_int
            }
        }
        resultado = db.comida.update_one(filter,update)
        if resultado.modified_count > 0:
            return jsonify({'OK': 'OK'}), 200
        else:
            return jsonify({'ERROR': 'Error desconocido'}), 404
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR_2':str(e)}), 400

@application.route('/food/<id>', methods=['DELETE'])
@check_auth(UserRole.EMPLEADO)
def delete_food_by_id(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        db.comida.delete_one(filter)
        response = jsonify({'message': 'Comida con id: ' + id + ' --> Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




















# -------------------------------- GET --------------------------------
# 2
@application.route('/search_animal/<string:input_animal>', methods=['GET'])
def search_animal(input_animal):
    filter = {'nombre': input_animal}
    projection = {
        '_id': 0, 
        'id_habitat': 0,
        'id_especie': 0}

    animales = db.animales.find(filter, projection)
    respuesta = json_util.dumps(animales)

    return respuesta



# 3
@application.route('/search_animal_from_habitat/<string:input_habitat>', methods=['GET'])
def search_animal_for_habitat(input_habitat):
    filter = {'nombre': input_habitat}
    projection = {
        'id_habitat': 0}

    habitat = db.habitats.find(filter, projection)
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
        habitats = db.habitats.find_one(filter)
        # me quedo SOLO con el id_habitat de habitat buscado
        filter2 = {'id_habitat': habitats['id_habitat']}
        
        animales = db.animales.find(filter2)
        respuesta = json_util.dumps(animales)
        return respuesta

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400


# -----------------------------------------------NUEVO: COMIDAS--------------------------------------------------------------------------------------
# consultar que come un animal
@application.route('/animales/comida/<string:nombre>', methods=['GET'])
def search_comida_animal(nombre):
    try: 
        # devuelve todos los datos de 1 animal
        filter = {'nombre': nombre}
        animales = db.animales.find_one(filter)
        # me quedo SOLO con el comida_id del animal buscado
        filter2 = {'comida_id': animales['comida_id']}
        projection = {
            '_id': 0, 
            'tamanno': 0,
            'peso': 0,
            'id_habitat': 0,
            'id_especie': 0
        }

        animales = db.animales.find(filter2, projection)
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
        animales = db.animales.find_one(filter)
        # me quedo SOLO con el comida_id del animal buscado
        filter2 = {'comida_id': animales['comida_id']}
        projection = {
            '_id': 0, 
            'tamanno': 0,
            'peso': 0,
            'id_habitat': 0,
            'id_especie': 0
        }

        animales = db.animales.find(filter2, projection)
        respuesta = json_util.dumps(animales)
        return respuesta

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



