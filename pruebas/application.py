#imports
from ast import Return
from functools import wraps
from hashlib import algorithms_available
from lib2to3.pgen2 import token
from tkinter import PROJECTING
from xml.sax.saxutils import prepare_input_source
from flask import Flask, request, abort, jsonify
from datetime import datetime, timedelta
from functools import wraps
from enum import IntEnum
import os, json, jwt
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
            
            return f(token_data['id'], *args, **kargs)
        return wrapper
    return decorator



@application.route("/", methods=['GET'])
def hello_world():
    return "<h1>Bienvenido a la API de vistazo animal</h1>"

#creacion del token en el login
@application.route("/login", methods=['POST'])
def login():
    filter = {
        #introducimos el correo y la contraseña
        'email': request.form['email'],
        'pass': request.form['pass']
    }
    
    user = db.usuarios.find_one(filter)
    if user:
        token_data = {
            'id': str(user['_id']),
            'exp': datetime.utcnow() + timedelta(seconds=6000)
        }
        token = jwt.encode(token_data, TOKEN_KEY, algorithm='HS256')
        return jsonify({'token':token}), 200
    return "No se ha podido inciar sesion", 401




#creacion de usuarios
@application.route('/users', methods=['POST'])
@check_auth(UserRole.ADMIN)
def crear_usuario(user_id):
    print(user_id)
    usuarios = list(db.usuarios.find())
    for usuario in usuarios:
        print(usuario)
    print("Has conseguido crear usuario")
    return "<h1>Hola, World!</h1>"












@application.errorhandler(400)
def error_400(error):
    return 'Solicitud incorrecta', 400

#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)