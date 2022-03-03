
#imports
from sqlite3 import Date
from urllib import response
from bson import json_util
from bson.objectid import ObjectId
from functools import wraps
from hashlib import algorithms_available
from lib2to3.pgen2 import token
from flask import Flask, request, abort, jsonify, Response
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from enum import IntEnum
import os, json, jwt,requests
from pymongo import MongoClient

#conexion con la base de datos
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
db = client.VistazoAnimal


path_base = os.path.dirname(os.path.abspath(__file__))
application = Flask(__name__)


TOKEN_KEY = 'top-secret'


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
            #if token_data['type'] > role:
                #abort(401)
            return f(token_data['id'], *args, **kargs)
        return wrapper
    return decorator

@application.route("/", methods=['GET'])
def hello_world():
    return "<h1>API del zoologico levantada</h1>"




#--------------- Usuarios ---------------





#Login de un usuario
@application.route("/login", methods=['POST'])
def login():
    filter = {
        'email': request.form['email'],
        'pass': request.form['pass']
    }
    user = db.usuarios.find_one(filter)
    if user:
        token_data = {
            'id': str(user['_id']),
            'exp': datetime.utcnow() + timedelta(seconds=10800)
        }
        token = jwt.encode(token_data, TOKEN_KEY, algorithm='HS256')
        return jsonify({'token':token}), 200
    else:
        return "No se ha podido inciar sesion", 401




#Registrar un nuevo usuario 
@application.route('/users', methods=['POST'])
def create_user():
    try:
        nombre = request.json['nombre']
        apellido1 = request.json['apellido1']
        apellido2 = request.json['apellido2']
        email = request.json['email']
        telefono = request.json['telefono']
        password = request.json['pass']
        
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if nombre and apellido1 and apellido2 and email and telefono and password and id:
            hashed_password = generate_password_hash(password)
            new_user = {
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'email': email,
                'telefono': telefono,
                'pass': hashed_password
                }
            db.usuarios.insert_one(new_user)
            response = jsonify({
                '_id': str(id),
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'email': email,
                'telefono': telefono
            })
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo crear el usuario'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




#Conseguir todos los usuarios
@application.route('/users', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def get_users(user_id):
    try:
        users = db.usuarios.find()
        response = json_util.dumps(users)
        return Response(response, mimetype="application/json"), 200
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Obtener usuario mediante id
@application.route('/users/<id>', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def get_user_byId(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        projection = {
            'pass': 0
        }
        #print(id)
        user = db.usuarios.find_one(filter,projection)
        response = json_util.dumps(user)
        return Response(response, mimetype="application/json"), 200
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Eliminar un usuario mediante su Id
@application.route('/users/<id>', methods=['DELETE'])
@check_auth(UserRole.SUPERADMIN)
def delete_user(user_id, id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        db.usuarios.delete_one(filter)
        response = jsonify({'message': 'Usuario ' + id + ' Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400


#Modificar un usuario mediante su Id
@application.route('/users/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
def update_user(user_id, id):
    try:
        nombre = request.json['nombre']
        apellido1 = request.json['apellido1']
        apellido2 = request.json['apellido2']
        email = request.json['email']
        telefono = request.json['telefono']
        password = request.json['pass']
        
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if nombre and apellido1 and apellido2 and email and telefono and password and id:
            hashed_password = generate_password_hash(password)
            filter = {'_id': ObjectId(id)}
            update = {'$set': {
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'email': email,
                'telefono': telefono,
                'pass': hashed_password
                
                }}
            db.usuarios.update_one(filter, update)
            response = jsonify({'message': 'Usuario ' + id + ' Fue actualizado correctamente'})
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo modificar el usuario'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400















#--------------- Ventas ---------------









#Registrar una nueva venta para el usuario que haya iniciado sesion
@application.route('/users/sales', methods=['POST'])
@check_auth(UserRole.SUPERADMIN)
def create_sale(user_id):
    try:
        fecha = datetime.utcnow()
        cantidad = request.json['cantidad']
        if fecha and cantidad :
            nueva_venta = {
                'fecha': fecha,
                'cantidad': cantidad,
                'usuario_id': user_id
            }
            db.ventas.insert_one(nueva_venta)
            response = jsonify({
                'fecha': fecha,
                'cantidad': cantidad,
                'usuario_id': str(user_id),
            })
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo modificar el usuario'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400





#Recuperar todas las ventas del usuario logueado
@application.route('/users/sales', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def get_sales(user_id):
    try:
        filter = {
            'usuario_id': user_id
        }
        projection = {
            'fecha': 1,
            'cantidad': 1
        }
        
        ventas = db.ventas.find(filter, projection)      
        if ventas:
            response = json_util.dumps(ventas)
            return Response(response, mimetype="application/json"), 200
        else:
            return  jsonify({'ERROR': 'No se pudo obtener las ventas'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','Error2': str(e)}), 400




#Recuperar todas las ventas de un usuario mediante un id siendo administrador
@application.route('/users/sales/<id>', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def get_sales_byId(user_id,id):
    try:
        filter = {
            'usuario_id': id
        }
        projection = {
            'fecha': 1,
            'cantidad': 1
        }
        ventas = db.ventas.find(filter, projection)      
        if ventas:
            response = json_util.dumps(ventas)
            return Response(response, mimetype="application/json"), 200
        else:
            return  jsonify({'ERROR': 'No se pudo obtener las ventas'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','Error2': str(e)}), 400





#Borrar una venta mediante su id
@application.route('/users/sales/<id>', methods=['DELETE'])
@check_auth(UserRole.SUPERADMIN)
def delete_sales_byId(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        db.usuarios.delete_one(filter)
        response = jsonify({'message': 'Venta con id:  ' + id + ' Ha sido eliminada Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Modificar una venta
@application.route('/users/sales/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
def update_sales(user_id, id):
    try:
        cantidad = request.json['cantidad']
        #fecha es introduciad año/mes/dia ("2014,10,21")
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if cantidad :
            filter = {'_id': ObjectId(id)}
            update = {'$set': {
                'cantidad': cantidad,
                }}
            db.ventas.update_one(filter, update)
            response = jsonify({'message': 'Venta con id:  ' + id + ' Ha sido modificada Correctamente'})
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo modificar la venta'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR': str(e)}), 400










#--------------- Especies ---------------









#Registrar una nueva especie 
@application.route('/species', methods=['POST'])
@check_auth(UserRole.SUPERADMIN)
def create_specie(user_id):
    try:
        nombre_cientifico = request.json['nombre_cientifico']
        nombre_vulgar = request.json['nombre_vulgar']
        descripcion = request.json['descripcion']
        if nombre_cientifico and nombre_vulgar and descripcion :
            nueva_especie = {
                'nombre_cientifico': nombre_cientifico,
                'nombre_vulgar': nombre_vulgar,
                'descripcion': descripcion
            }
            db.especie.insert_one(nueva_especie)
            response = jsonify({
                'nombre_cientifico': nombre_cientifico,
                'nombre_vulgar': nombre_vulgar,
                'descripcion': descripcion
            })
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo insertar la especie'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400





#Recuperar todas las especies
@application.route('/species', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def get_species(user_id):
    try:
        especies = db.especie.find()      
        if especies:
            response = json_util.dumps(especies)
            return Response(response, mimetype="application/json"), 200
        else:
            return  jsonify({'ERROR': 'No se pudo obtener las especies'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




#Recuperar la especie mediante su id
@application.route('/species/<id>', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def get_species_byId(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        especies = db.especie.find(filter)      
        if especies:
            response = json_util.dumps(especies)
            return Response(response, mimetype="application/json"), 200
        else:
            return  jsonify({'ERROR': 'No se pudo obtener la especie buscada'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Recuperar todos los animales de una especie mediante el nombre de la especie

@application.route('/species/prueba/<string:nombre>', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def get_animals_by_specie(user_id,nombre):
    try:
        filter = {'nombre_vulgar': nombre}
        especie_inf = db.especie.find_one(filter)
        return json_util.dumps(especie_inf)
        if especie_inf :
            filter2 = {'especie_id': especie_inf[ObjectId(especie_inf['_id'])]}      
            animales = db.animales.find(filter2)
            response = json_util.dumps(animales)
            return Response(response, mimetype="application/json"), 200
    except Exception as e:
        return jsonify({'ERROR': str(e)}), 400



#Eliminar una especie mediante su id
@application.route('/species/<id>', methods=['DELETE'])
@check_auth(UserRole.SUPERADMIN)
def delete_species_byId(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        db.especie.delete_one(filter)
        response = jsonify({'message': 'Especie con id:  ' + id + ' Ha sido eliminada Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




#Modificar una especie mediante su id
@application.route('/species/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
def update_species(user_id, id):
    try:
        nombre_cientifico = request.json['nombre_cientifico']
        nombre_vulgar = request.json['nombre_vulgar']
        descripcion = request.json['descripcion']
        if nombre_cientifico and nombre_vulgar and descripcion :
            filter = {
                '_id': ObjectId(id)
            }
            update = {'$set':{
                'nombre_cientifico': nombre_cientifico,
                'nombre_vulgar': nombre_vulgar,
                'descripcion': descripcion
                }
            }
            db.especie.update_one(filter,update)
            response = jsonify({'message': 'Especie con id:  ' + id + ' Ha sido modificada correctamente'})
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo insertar la especie'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR': str(e)}), 400







#--------------- Habitat ---------------






#Conseguir todos los habitats
@application.route("/habitats", methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def all_habitats():
    filter = {}
    projection = {'_id': 0}
    habitats = list(db.habitats.find(filter, projection))
    for habitat in habitats:
        print(habitat)
    return jsonify(habitats), 200



#Buscar habitat por id
@application.route('/habitats/buscar/<id>', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def buscar_habitat(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        habitats = db.habitats.find(filter)
        respuesta = json_util.dumps(habitats)
        return respuesta

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Crear un habitat pasando un nombre y un id de habitat
@application.route('/habitats/nuevo', methods=['POST'])
@check_auth(UserRole.SUPERADMIN)
def new_habitat():
    try: 
        nombre = request.json['nombre']
        id_habitat = request.json['id_habitat']
        new_habitat = {
            'nombre': nombre,
            'id_habitat': id_habitat
        }
        db.habitats.insert_one(new_habitat)
        response = jsonify({'message': 'Habitat con nombre: ' + nombre + ' --> Insertado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Actualizar un habitat mediante un id
@application.route('/habitats/actualizar/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
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
        db.habitats.update_one(filter, update)
        response = jsonify({'message': 'Habitat con id: ' + id + ' --> Actualizado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




#Eliminar un habitat mediante su id
@application.route('/habitats/borrar_id/<id>', methods=['DELETE'])
@check_auth(UserRole.SUPERADMIN)
def delete_habitat_from_id(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        db.habitats.delete_one(filter)
        response = jsonify({'message': 'Habitat con id: ' + id + ' --> Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400







#--------------- Animales ---------------






#Conseguir todos los animales
@application.route("/animals", methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def all_animals():
    filter = {}
    projection = {
        '_id': 0, 
        'id_habitat': 0,
        'id_especie': 0}

    animales = list(db.animales.find(filter, projection))
    for animal in animales:
        print(animal)
    
    return jsonify(animales), 200






#Buscar un animal por su nombre
@application.route('/animal/<string:input_animal>', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def search_animal(input_animal):
    filter = {'nombre': input_animal}
    projection = {
        '_id': 0, 
        'id_habitat': 0,
        'id_especie': 0}

    animales = db.animales.find(filter, projection)
    respuesta = json_util.dumps(animales)

    return respuesta







#Buscar todos los animales de un habitat por su nombre
@application.route('/animals/<string:nombre>', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
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




#Crear un nuevo animal
@application.route('/animales/nuevo', methods=['POST'])
@check_auth(UserRole.SUPERADMIN)
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
        db.animales.insert_one(new_animal)
        response = jsonify({'message': 'Animal con nombre: ' + nombre + ' --> Insertado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400





#Modificar un animal mediante su id
@application.route('/animals/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
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
        db.animales.update_one(filter, update)
        response = jsonify({'message': 'Animal con id: ' + id + ' --> Actualizado Correctamente'})
        response.status_code = 200
        return response

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Borrar un animal mediante su id
@application.route('/animales/<id>', methods=['DELETE'])
@check_auth(UserRole.SUPERADMIN)
def delete_animal_from_id(id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        db.animales.delete_one(filter)
        response = jsonify({'message': 'Animal con id: ' + id + ' --> Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Borrar un animal mediante su nombre
@application.route('/animales/<string:nombre>', methods=['DELETE'])
@check_auth(UserRole.SUPERADMIN)
def delete_animal_from_name(nombre):
    try:
        filter = {
            'nombre': nombre
        }  
        db.animales.delete_one(filter)
        response = jsonify({'message': 'El animal: ' + nombre + ' --> Eliminado Correctamente'})
        response.status_code = 200
        return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400








@application.errorhandler(400)
def error_400(error):
    return 'Solicitud incorrecta', 400


#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



