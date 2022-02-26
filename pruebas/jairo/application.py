#imports
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
    ADMIN = 5
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




#Registrar una nueva venta para el usuario que haya iniciado sesion
@application.route('/users/sales', methods=['POST'])
@check_auth(UserRole.SUPERADMIN)
def create_venta(user_id):
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
            '_id': ObjectId(user_id)
        }
        projection = {
            'fecha': 1,
            'cantidad': 1
        }
        ventas = db.find(filter, projection)
        if ventas:
            response = json_util.dumps(ventas)
            response.status_code = 200
            return response
        else:
            return  jsonify({'ERROR': 'No se pudo obtener las ventas'})
    except Exception as e:
        return jsonify({'ERROR': 'Error desconocido'}), 400




#Recuperar todas las ventas de un usuario siendo administrador































@application.errorhandler(400)
def error_400(error):
    return 'Solicitud incorrecta', 400

#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)