import requests, json, os

BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))

#request para crear un usuario
def crear_usuario():
    print("------------Creacion de usuarios------------")
    email_usuario = input("Introduzca un email: \n")
    pass_usuario = input("Introduzca una contraseña para la cuenta")

    nuevo_usuario = {
        'nick': email_usuario,
        'pass': pass_usuario
    }

    r = requests.post(f'{BASE_URL}comments',json=nuevo_usuario)

    if r.status_code == 200:
        print("Se ha introducido el usuario correctamente")
    return None






crear_usuario()