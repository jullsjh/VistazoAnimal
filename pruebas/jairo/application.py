#imports
from dataclasses import dataclass
from sqlite3 import Date
from urllib import response
from bson import json_util
from bson.objectid import ObjectId
from functools import wraps
from hashlib import algorithms_available
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




@application.route("/", methods=['GET'])
def hello_world():
    return "<h1>API del zoologico levantada</h1>"




#--------------- Usuarios ---------------





#Login de un usuario
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



#Registrar un nuevo usuario 
@application.route('/users', methods=['POST'])
def create_user():
    try:
        #data = request.json()
        nombre = request.json['nombre']
        apellido1 = request.json['apellido1']
        apellido2 = request.json['apellido2']
        email = request.json['email']
        telefono = request.json['telefono']
        password = request.json['password']
        type_user = request.json['type']
        filter = {
            'email': email,
            'pass': generate_password_hash(password)
        }
        user = db.usuarios.find_one(filter)
        if user:
            return jsonify({'ERROR': 'Ese correo ya este registrado'})
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if nombre and apellido1 and apellido2 and email and telefono and password and type_user:
            hashed_password = generate_password_hash(password)
            new_user = {
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'email': email,
                'telefono': telefono,
                'pass': hashed_password,
                'type': type_user
                }
            db.usuarios.insert_one(new_user)
            response = jsonify({
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'email': email,
                'telefono': telefono,
                'type': type_user
            })
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo crear el usuario falta algun dato por introducir'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR_2':str(e)}), 400




#Conseguir todos los usuarios
@application.route('/users', methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def get_users(user_id):
    try:
        users = db.usuarios.find()
        response = json_util.dumps(users)
        return Response(response, mimetype="application/json"), 200
    except Exception:
        return jsonify({'ERROR': 'No se pudieron obtener los usuarios'}), 400



#Obtener usuario mediante id
@application.route('/users/<id>', methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def get_user_byId(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        projection = {
            'pass': 0
        }
        #print(id)
        if db.usuarios.find_one(filter,projection):
            user = db.usuarios.find_one(filter,projection)
            response = json_util.dumps(user)
            return Response(response, mimetype="application/json"), 200
        else:
            return jsonify({'ERROR': 'id no existente dentro de la base de datos'}), 400
    except Exception:
        return jsonify({'ERROR': 'id no existente dentro de la base de datos'}), 400



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
        return jsonify({'ERROR': 'No se pudo eliminar el usuario'}), 400


#Modificar un usuario mediante su id
@application.route('/users/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
def update_user(user_id, id):
    try:
        filter = {
            '_id': ObjectId(str(id))
        }
        user = db.usuarios.find_one(filter)
        data = request.get_json()
        if 'nombre' not in data:
            nombre = user['nombre']
        else:
            nombre = data['nombre']
        if 'apellido1' not in data:
            apellido1 = user['apellido1']
        else:
            apellido1 = data['apellido1']
        if 'apellido2' not in data:
            apellido2 = user['apellido2']
        else:
            apellido2 = data['apellido2']
        if 'email' not in data:
            email = user['email']
        else:
            email = data['email']
        if 'telefono' not in data:
            telefono = user['telefono']
        else:
            telefono = data['telefono']
        if 'password' not in data:
            password = user['pass']
        else:
            password = data['password']
        if 'type' not in data:
            type_user = user['type']
        else:
            type_user = data['type']
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if nombre and apellido1 and apellido2 and email and telefono and password and type_user:
            hashed_password = generate_password_hash(password)
            update = {'$set': {
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'email': email,
                'telefono': telefono,
                'pass': hashed_password,
                'type': type_user
                }}
            db.usuarios.update_one(filter, update)
            response = jsonify({'message': 'Usuario ' + id + ' Fue actualizado correctamente'})
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo modificar el usuario, faltan datos para crear el usuario'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'ERROR_2': str(e)}), 400














#--------------- Ventas ---------------









#Registrar una nueva venta para el usuario que haya iniciado sesion
@application.route('/users/sales', methods=['POST'])
@check_auth(UserRole.USUARIO)
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
@check_auth(UserRole.USUARIO)
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




#Recuperar todas las ventas de un usuario mediante un id siendo empleado/administrador
@application.route('/users/sales/<id>', methods=['GET'])
@check_auth(UserRole.EMPLEADO)
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
@check_auth(UserRole.EMPLEADO)
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
@check_auth(UserRole.EMPLEADO)
def update_sales(user_id, id):
    try:
        data= request.get_json()
        filter_rep = {
            '_id': ObjectId(str(id))
        }
        filter_usuario = {
            'nombre': data['nombre'],
            'apellido1': data['apellido1'],
            'apellido2':data['apellido2']
        }
        venta = db.ventas.find_one(filter_rep)
        usuario = db.usuarios.find_one(filter_usuario)
        if 'cantidad' not in data:
            cantidad = venta['cantidad']
        if 'nombre' not in data or 'apellido1' not in data or 'apellido2' not in data:
            return  jsonify({'ERROR': 'No se ha especificado correctamente el usuario de la venta'})
        else:
            usuario_id = usuario['_id'] 
            filter = {'_id': ObjectId(id)}
            update = {'$set': {
                'cantidad': cantidad,
                'usuario_id': usuario_id
                }}
            db.ventas.update_one(filter, update)
            response = jsonify({'message': 'Venta con id:  ' + id + ' Ha sido modificada Correctamente'})
            response.status_code = 201
            return response
            #fecha es introducida año/mes/dia ("2014,10,21")
            #['$oid']) if '$oid' in id else ObjectId(id) 
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR': str(e)}), 400










#--------------- Especies ---------------









#Crear una nueva especie 
@application.route('/species', methods=['POST'])
@check_auth(UserRole.EMPLEADO)
def create_specie(user_id):
    try:
        nombre_cientifico = request.json['nombre_cientifico']
        nombre_vulgar = request.json['nombre_vulgar']
        descripcion = request.json['descripcion']
        filter_rep = {
            'nombre_cientifico':nombre_cientifico,
            'nombre_vulgar':nombre_vulgar
        }
        especie = db.especie.find_one(filter_rep)
        if especie:
            return  jsonify({'ERROR': 'Esa especie ya existe en la base de datos'})
        else:
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
@check_auth(UserRole.EMPLEADO)
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
@check_auth(UserRole.EMPLEADO)
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
@application.route('/species/find/<string:nombre>', methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def get_animals_by_specie(user_id,nombre):
    try:
        filter = {'nombre_vulgar': nombre}
        especie_inf = db.especie.find_one(filter)
        #return json_util.dumps(especie_inf)
        if especie_inf :
            especie_id = especie_inf['_id']
            filter2 = {'especie_id': str(especie_id)} 
            animales = db.animales.find(filter2)
            response = json_util.dumps(animales)
            return Response(response, mimetype="application/json"), 200
    except Exception as e:
        return jsonify({'ERROR': str(e)}), 400




#Eliminar una especie mediante su id
@application.route('/species/<id>', methods=['DELETE'])
@check_auth(UserRole.EMPLEADO)
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
@check_auth(UserRole.EMPLEADO)
def update_species(user_id, id):
    try:
        data = request.get_json()
        nombre_cientifico = data['nombre_cientifico']
        nombre_vulgar = data['nombre_vulgar']
        descripcion = data['descripcion']
        filter_rep = {
            '_id':ObjectId(id)
        }
        especie = db.especie.find_one(filter_rep)
        if 'nombre_cientifico' not in data:
            nombre_cientifico = especie['nombre_cientifico']
        else:
            nombre_cientifico = data['nombre_cientifico']
        if 'nombre_vulgar' not in data:
            nombre_vulgar = especie['nombre_vulgar']
        else:
            nombre_vulgar = data['nombre_vulgar']
        if 'descripcion' not in data:
            descripcion = especie['descripcion']
        else:
            descripcion = data['descripcion']
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






#--------------- VETERINARIOS ---------------




#Obtener veterinario por id 
@application.route('/veterinary/<id>', methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def get_veterinary_byId(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        veterinario = db.veterinarios.find(filter)      
        if veterinario:
            response = json_util.dumps(veterinario)
            return Response(response, mimetype="application/json"), 200
        else:
            return  jsonify({'ERROR': 'No se pudo obtener el veterinario buscado'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




#Obtener todos los veterinarios
@application.route('/veterinary', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def get_veterinary(user_id,id):
    try:
        veterinario = db.veterinarios.find(filter)      
        if veterinario:
            response = json_util.dumps(veterinario)
            return Response(response, mimetype="application/json"), 200
        else:
            return  jsonify({'ERROR': 'No se pudo obtener el veterinario buscada'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400





#Eliminar un veterinario por id
@application.route('/veterinary/<id>', methods=['DELETE'])
@check_auth(UserRole.EMPLEADO)
def delete_veterinary_byId(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }  
        busqueda = db.veterinarios.delete_one(filter)
        if busqueda:
            response = jsonify({'message': 'Veterinario con id:  ' + id + ' Ha sido eliminado Correctamente'})
            response.status_code = 200
            return response
        else:
            return jsonify({'ERROR': 'ID introducido no existe'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#Modificar un veterinario mediante su id
@application.route('/veterinay/<id>', methods=['PUT'])
@check_auth(UserRole.SUPERADMIN)
def update_veterinary(user_id, id):
    try:
        filter = {
            '_id': ObjectId(str(id))
        }
        veterinary = db.usuarios.find_one(filter)
        data = request.get_json()
        if 'nombre' not in data:
            nombre = veterinary['nombre']
        else:
            nombre = data['nombre']
        if 'apellido1' not in data:
            apellido1 = veterinary['apellido1']
        else:
            apellido1 = data['apellido1']
        if 'apellido2' not in data:
            apellido2 = veterinary['apellido2']
        else:
            apellido2 = data['apellido2']
        #cuando se introduce la especie se introduce el nombre y no la id
        if 'especie_nombre' not in data:
            especie = veterinary['especie']
        else:
            especie = data['especie']
        if 'estado' not in data:
            estado = veterinary['estado']
        else:
            estado = data['estado']
        #['$oid']) if '$oid' in id else ObjectId(id) 
        if nombre and apellido1 and apellido2 and especie and estado:
            #obtenemos el id de la especie
            especie_id = especie['_id']
            update = {'$set': {
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'especie_id': especie_id,
                'estado': estado
                }}
            db.veterinarios.update_one(filter, update)
            response = jsonify({'message': 'Usuario ' + id + ' Fue actualizado correctamente'})
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo modificar el usuario, faltan datos para crear el usuario'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'ERROR': str(e)}), 400




#crear veterinario asignando su especie correspondiente
@application.route('/veterinary', methods=['POST'])
@check_auth(UserRole.EMPLEADO)
def create_veterinary(user_id):
    try:
        data = request.get_json()
        filter = {
            'nombre': data['especie_nombre']
        }
        projection  = {
            '_id':1
        }
        especie = db.especies.find_one(filter,projection)
        nombre = data['nombre']
        apellido1 = data['apellido1']
        apellido2 = data['apellido2']
        especie_id = especie['_id']
        estado = data['estado']
        if nombre and apellido1 and apellido2 and especie_id and estado:
            nuevo_veterinario = {
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
                'especie_id': especie_id
            }
            filter_vet = {
                'nombre': nombre,
                'apellido1': apellido1,
                'apellido2': apellido2,
            }
            repetido = db.veterinarios.find_one(filter_vet)
            if repetido:
                return jsonify({'ERROR':'Registro repetido'}), 400
            else:
                result = db.veterinarios.insert_one(nuevo_veterinario)
            if result.inserted_id:
                return jsonify({'OK':'Se ha insertado el veterinario correctamente'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400



#asignar especie a un veterinario en concreto y que ese veterinario deje de estar disponible, 
@application.route('/veterinary/assign', methods=['PUT'])
@check_auth(UserRole.EMPLEADO)
def assign_specie_veterinary(user_id):
    try:
        data = request.get_json()
        filter = {
            'nombre': data['nombre'],
            'apellido1':data['apellido1'],
            'apellido2':data['apellido2'],
        }
        projection  = {
            'estado':1
        }
        #recuperamos todos los datos del veterinario
        veterinario = db.veterinarios.find_one(filter,projection)
        #recuperamos la especie por el nombre
        filter_especie = {
            'nombre_cientifico': data['especie_nombre']
        }
        projection_especie = {
            '_id':1
        }
        especie = db.especie.find_one(filter_especie,projection_especie)
        print(especie)
        if veterinario['estado'] == 'asignado':
            return jsonify({'ERROR':'Este veterinario ya esta asignado'}), 400
        else:
            especie_id = especie['_id']
            update = {'$set': {
                'estado': 'asignado',
                'especie_id': especie_id
                }}
            db.veterinarios.update_one(filter, update)
            return jsonify({'OK':'Se ha asignado al veterinario correctamente'}), 200
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR2': str(e)}), 400





#Funciones Julls -----------------------------------------------------------------------


#--------------- ANIMALES ---------------

#registrar varios animales con todos sus datos
@application.route('/animals/create', methods=['POST'])
@check_auth(UserRole.EMPLEADO)
def create_species(user_id):
    try:
        json_data = request.get_json()
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
                return jsonify({'ERROR':'Ha habido un problema con el nombre de habitat/especie'})
            new_animal = { 
                'nombre': data['nombre'],
                'tamanno': data['tamanno'],
                'peso': data['peso'],
                'habitat_id': habitat['_id'],
                'especie_id': especie['_id']
                }
            result = db.animales.insert_one(new_animal)
        return jsonify({'OK':'Se han podido ingresar los animales'}), 201
    except Exception as e:
        return jsonify({'ERROR': 'No se ha podido crear la lista de animales'}), 400


#Obtener todos los animales
@application.route("/animals", methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def get_animals(user_id):
    try:
        animales = list(db.animales.find())
        if animales:
            return jsonify(animales), 200
        else:
            return jsonify({'ERROR': 'No se ha podido recuperar los animales'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400


#Creacion de un nuevo animal mediante un json
@application.route('/animal', methods=['POST'])
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
            especie = db.especie.find_one({'nombre_cientifico':data['nombre_especie']})
            habitat = db.habitats.find_one({'nombre':data['nombre_habitat']})
            new_animal = {
                'nombre': data['nombre'],
                'tamanno': data['tamanno'],
                'peso': data['peso'],
                'id_habitat': especie['_id'],
                'id_especie': habitat['_id']
            }
            db.animales.insert_one(new_animal)
            nombre = data['nombre']
            return jsonify({'message': 'Animal con nombre: ' + nombre + ' Insertado Correctamente'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




#Eliminar un animal por id
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




#Buscar un animal por su nombre
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



#Modificar un animal ya existente 
@application.route('/habitat/<id>', methods=['PUT'])                 
@check_auth(UserRole.SUPERADMIN)
def update_animal(user_id, id):
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

                     

#Buscar todos los animales de un habitat por nombre habitat
@application.route('/animals/habitat/<string:nombre>', methods=['GET'])
@check_auth(UserRole.SUPERADMIN)
def search_animals_from_habitat(user_id,nombre):
    try: 
        # devuelve todos los datos de 1 habitat
        filter = {'nombre': nombre}
        habitat = db.habitats.find_one(filter)
        # me quedo SOLO con el id_habitat de habitat buscado
        filter2 = {'habitat_id': habitat['_id']}
        animales = db.animales.find(filter2)
        if animales:
            respuesta = json_util.dumps(animales)
            return respuesta
        else:
            return jsonify({'ERROR': 'No se ha podido recuperar los animales del habitat'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR_EXP': str(e)}), 400










#--------------- HABITATS ---------------

#Obtener todos los habitats
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



#Obtener un habitat por su nombre
@application.route('/habitats/<string:habitat>', methods=['GET'])
@check_auth(UserRole.USUARIO)
def search_habitat(user_id,habitat):
    try:
        filter = {'nombre': habitat}
        habitat = db.habitats.find_one(filter)
        if habitat:
            respuesta = json_util.dumps(habitat)
            return respuesta
        else:
            return jsonify({'ERROR': 'No se ha podido encontrar el habitat introducido'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR2': str(e)}), 400



#Modificar un habitat mediante su id
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


#Creacion de un nuevo habitat enviando un json
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
            response = jsonify({'message': 'habitat con ' + id + ' Fue creado correctamente'})
            response.status_code = 201
            return response
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'ERROR_2': str(e)}), 400



#Eliminar un habitat mediante su id
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
            response = jsonify({'message': 'habitat con ' + id + ' Fue eliminado correctamente'})
            response.status_code = 201
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo eliminar el habitat'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido', 'ERROR2': str(e)}), 400





#--------------- COMIDAS ---------------





#Obtener informacion sobre todas las comidas
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



#buscar un comida por su id
@application.route('/food/search/<id>', methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def search_food(user_id,id):
    try:
        filter = {
            '_id': ObjectId(id)
        }
        comidas = db.comida.find(filter)
        if comidas:
            respuesta = json_util.dumps(comidas)
            return respuesta
        else:
            return jsonify({'ERROR': 'No se han podido obtener datos de la comida'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400


#Crear una nueva comida
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


#Modificar una comida mediante su id
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



#Borrar una comida mediante su id
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





#Consultar la comida de una especie 
@application.route('/species/food/<string:nombre_cientifico>', methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def search_food_byspecie(user_id,nombre_cientifico):
    try: 
        especie = db.especie.find_one({'nombre_cientifico':nombre_cientifico})
        comida_filter = {'_id': especie['comida_id']}
        comida = db.comida.find_one(comida_filter)
        if comida:
            respuesta = json_util.dumps(comida)
            return respuesta
        else:
            return jsonify({'ERROR': 'No se pudo obtener la comida de esa especie'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




#Busco todos las especies que comen una comida en particular
@application.route('/food/species/<string:nombre>', methods=['GET'])
@check_auth(UserRole.EMPLEADO)
def search_species_by_food(user_id,nombre):
    try:
        comida = db.comida.find_one({'nombre':nombre})
        especies = db.especie.find({'comida_id':comida['_id']})
        if especies:
            respuesta = json_util.dumps(especies)
            return respuesta, 200
        else:
            return jsonify({'ERROR': 'No se han podido recuperar las especies'}), 400

    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR_2':str(e)}), 400



#Dar de comer a un animal y que se reduzca la cantidad de comida del animal
@application.route('/food/specie', methods=['PUT'])
@check_auth(UserRole.EMPLEADO)
def givefood_animal(user_id):
    try:
        data = request.get_json()
        animal = db.animales.find_one({'nombre':data['nombre_animal']})
        especie = db.especie.find_one({'_id':animal['especie_id']})
        comida = db.comida.find_one({'_id':especie['comida_id']})
        filter = {
            '_id': comida['_id']
        }
        cantidad_int = int(comida['cantidad'])
        cantidad_int = cantidad_int - 10
        update = {
            '$set': {
                'cantidad': str(cantidad_int)
            }
        }
        comida = db.comida.update_one(filter,update)
        if comida:
            return jsonify({'OK': 'Se ha dado de comer correctamente a los animales'}), 400, 200
        else:
            return jsonify({'ERROR': 'No se han podido recuperar las especies'}), 400
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido','ERROR_2':str(e)}), 400






@application.errorhandler(400)
def error_400(error):
    return 'Solicitud incorrecta', 400

#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)