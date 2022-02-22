#importamos flask
from curses import wrapper
from flask import Flask, request, abort, jsonify
from datetime import datetime, timedelta
from functools import wraps
from pymongo import MongoClient
import json, jwt
from markupsafe import re

#instanciamos la clase , creamos un nuevo objeto y le pasamos el __name__
application = Flask(__name__)
TOKEN_KEY = 'top-secret'


# El decorador basicamente es como una funcion
# CREO DECORADOR PARA EL TOKEN, para no poner el mismo codigo para proteger a cada funcion
# * --> se puede pasar nº indef de parametros
def check_auth(role):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kargs):
            # 8. protejo este endpoint
            token = request.headers['Authorization']
            # para que quite la palabra berer y por consola solo devuelva el token. 1 para que coja el token ya que es posicion 1
            token = token.split()[1]
            try:
                token_data = jwt.decode(token, TOKEN_KEY, algorithms=['HS256'])
            except Exception as e:
                print(str(e))
                abort(401)
            return f(token_data['id'], *args, **kargs)
            return wrapper
        return decorator


#------------- 1. el @ se llama decorador, esto es una llamada http -------------
@application.route("/", methods=['GET'])#esto es el endpoint raiz
def hello_world():
    if request.method == 'GET':
        return "<h1>Hellossss: API Levantada!</h1>"
    return "<h1>Adios muy buenas</h1>"

# #por defecto esto se trata peticiones get
# @application.route("/saludo")
# def saludo():
#     return "<h1>Un saludo</h1>"

@application.route("/saludo", methods=['GET'])
def saludo():
    return "<h1>Un saludo 1</h1>"

@application.route("/saludo", methods=['POST'])
def despedida():
    return "<h1>Esto es un POST de despedida</h1>"




#2. --------------- flask nos permite parametrizar el endpoint, nunca se recibe un dato sin tratarlo ---------------
@application.route("/saludo/<name>", methods=['GET'])
@check_auth
def saludo_persona(user_id, name):
    if name.lower() == 'paco':
        abort(400)
    return f'<h1>un saludo {name}</h1>'

@application.errorhandler(400)
def error_400(error):
    return 'No tienes ni idea', 400




#3. ------------- se puede especificar el tipo de dato que vas a recibir con la palabra int: dentro del application.route -------------
@application.route("/saludo/<int:numero>", methods=['GET'])
def saludo_persona_numero(numero):
    print(type(numero))
    return f'<h1>hola {numero}</h1>'




# 4. LOGIN con html: loginServer.html
# quien manda es el server, asi que si le pongo POST el html tiene que llevar POST
# @application.route("/login", methods=['POST'])
# def login():
#     if request.form['user'] == 'admin' and request.form['pass'] == '1234':
#         return f'<h1>Hola Admin</h1>', 200
#     return f'<h1>Hacker</h1>', 401




# -------------------- 5. recibo username y email que mete el usuario y comprueba si existe en el archivo json --------------------
# @application.route("/login", methods=['POST'])
# def login():
#     with open('users.json', 'r', encoding= 'UTF-8') as file:
#         users = json.loads(file.read())
#         for user in users:
#             if user['username'] == request.form['user'] and user['email'] == request.form['pass']:
#                 # 7. croe TOKEN para guardar sesion de usuario?
#                 token_data = {
#                     'id': user['id'],
#                     'name': user['name'],
#                     'type': 1,
#                     # exp es el tiempo que quiero que dure el token
#                     'exp': datetime.utcnow() + timedelta(seconds=60)
#                 }
#                 token = jwt.encode(token_data, TOKEN_KEY, algorithm='HS256')
#                 return f"Hola Admin", 200
#         return f'<h1>Hacker</h1>', 401

        # Este post devuelve un JSON con JSONIFY
        # for user in users:
        #     if user['username'] == request.form['user'] and user['email'] == request.form['pass']:
        #         return jsonify(user), 200
        # return f'<h1>Hacker</h1>', 401




# -------------------- 6. Creo un nuevo usuario en el archivo users.json --------------------
@application.route("/users", methods=['POST'])
@check_auth
def crear_usuario():
    data = request.get_json()
    print(data['users'])

    with open('users.json', 'r', encoding= 'UTF-8') as file:
        users = json.loads(file.read())
    users.append({
        'username': data['user'],
        'email': data['pass']
    })

    with open('users.json', 'r', encoding= 'UTF-8') as file:
        file.write(json.dumps(users, indent=4))
    return jsonify({'resul': 'Usuario creado'}), 200







# MONGO DB LOGIN
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')
mongodb = client.python2a
user = mongodb.find_one
filter = {'name': 'Pepe'}
projection = {'name': 1, 'direccion': 1}


@application.route("/login", methods=['POST'])
def login():
        users = list(mongodb.test.find(filter, projection))
        for user in users:
            if user['name'] == request.form['user'] and user['email'] == request.form['pass']:
                # 7. croe TOKEN para guardar sesion de usuario?
                token_data = {
                    'id': user['id'],
                    'name': user['name'],
                    'type': 1,
                    # exp es el tiempo que quiero que dure el token
                    'exp': datetime.utcnow() + timedelta(seconds=60)
                }
                token = jwt.encode(token_data, TOKEN_KEY, algorithm='HS256')
                return f"Hola Admin", 200
        return f'<h1>Hacker</h1>', 401





#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



