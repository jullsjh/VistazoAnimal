# ------------------------ TUTORIAL YT ------------------------
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)

# propiedad donde definimos donde esta la bbdd, servidor, nombre bbdd, puerto...
app.config['MONGO_URI'] = 'mongodb://localhost:27017//tutorialYTdb'
# le paso la config a la conexion para poder manipular las colecciones/insertar datos etc
mongo = PyMongo(app)




@app.route('/users', methods=['POST'])
def create_user():
    # recibo datos del cliente
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    # si existe esto, lo guardo en la bbdd
    if username and email and password:
        hashed_password = generate_password_hash(password)
        # db es una propiedad que permite acceder a la bbdd, si no existe, crea la tabla
        id = mongo.db.users.insert(
            {'username': username, 'email': email, 'password': hashed_password})
        # obj con la descripcion del nuevo dato que se ha creado 
        response = jsonify({
            '_id': str(id),
            'username': username,
            'password': password,
            'email': email
        })
        response.status_code = 201
        return response
    else:
        return not_found()




@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    # json_util convierte los datos bson a json
    response = json_util.dumps(users)
    # como es leido como string desde el cliente, le pongo la cabecera mimetype para que el cliente pueda pintarlo con colores e imprimir lista de json
    return Response(response, mimetype="application/json")


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = mongo.db.users.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    response.status_code = 200
    return response


@app.route('/users/<_id>', methods=['PUT'])
def update_user(_id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if username and email and password and _id:
        hashed_password = generate_password_hash(password)
        mongo.db.users.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': username, 'email': email, 'password': hashed_password}})
        response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
        response.status_code = 200
        return response
    else:
      return not_found()









@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response





if __name__ == "__main__":
    app.run(debug=True)
