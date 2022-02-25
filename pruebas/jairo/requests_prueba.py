import requests, json, os
from flask import jsonify

BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))






def login_usuario():
    print("------------Login de usuario------------")
    email_usuario = input("Introduzca un email para loguearse en su cuenta: \n")
    pass_usuario = input("Introduzca una contraseña para loguearse en su cuenta \n")
    login_usuario = {
        'email': email_usuario,
        'pass': pass_usuario
    }
    r = requests.post(f'{BASE_URL}comments', json=login_usuario)
    if r.status_code == 200:
        print("Bienvenido")
        hola = "hola"
        return hola
    else:
        print("No se pudo iniciar sesion")





#request para registrar un usuario
def crear_usuario():
    print("------------Registro de usuarios------------")
    email_usuario = input("Introduzca un email para crear su cuenta: \n")
    pass_usuario = input("Introduzca una contraseña para la cuenta \n")

    nuevo_usuario = {
        'email': email_usuario,
        'pass': pass_usuario
    }

    r = requests.post(f'{BASE_URL}comments',json=nuevo_usuario)

    if r.status_code == 200:
        return r.json, 200
    else:
        return jsonify({'ERROR': 'Error desconocido'}), 400





login_usuario()