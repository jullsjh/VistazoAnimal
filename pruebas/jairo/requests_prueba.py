from time import process_time_ns
import requests, json, os

BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))
token_user = None
headers={}

def login_usuario():
    global token_user
    global headers
    print("------------Login de usuario------------")
    email_usuario = input("Introduzca un email para loguearse en su cuenta: \n")
    pass_usuario = input("Introduzca una contraseña para loguearse en su cuenta \n")
    login_usuario = {
        'email': email_usuario,
        'pass': pass_usuario
    }
    auth = requests.post(f'{BASE_URL}login', json=login_usuario)
    token_user = auth.json()['token']
    print(token_user)
    headers = {
        'Authorization': 'Bearer ' + token_user
    }




#--------------- Usuarios ---------------


#request para registrar un usuario
def crear_usuario():
    print("------------Registro de usuarios------------")
    nombre = input("Introduzca un nombre: \n")
    apellido1 = input("Introduzca su primer apellido: \n")
    apellido2 = input("Introduzca su segundo apellido: \n")
    email = input("Introduzca su email: \n")
    telefono = input("Introduzca su telefono: \n")
    password = input("Introduzca una contraseña: \n")
    nuevo_usuario = {
        'nombre': nombre,
        'apellido1': apellido1,
        'apellido2': apellido2,
        'email': email,
        'telefono': telefono,
        'password': password,
        'type':100
    }
    r = requests.post(f'{BASE_URL}users',json=nuevo_usuario)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

#request para obtener todos los usuarios
def obtener_usuarios():
    print("------------Usuarios------------")
    r = requests.get(f'{BASE_URL}users', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)



#request para obtener un usuario mediante su id
def obtener_usuario_id():
    print("------------Usuario------------")
    user_id = input("Introduce el id del usuario a buscar: \n")
    r = requests.get(f'{BASE_URL}users/{user_id}', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)


#print(crear_usuario())
login_usuario()
print("1. Animales \n")
print("2. Comida \n")
print("3. Especie \n")
print("4. Habitats \n")
print("5. Usuarios \n")
print("6. Ventas \n")
print("7. Veterinarios \n")
opcion = input("Escoja una tabla: \n")

if int(opcion) == 5:
    print(obtener_usuarios())
    
