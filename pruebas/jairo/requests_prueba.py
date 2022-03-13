import email
import requests, json, os

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
        'password': password
    }
    r = requests.post(f'{BASE_URL}users',json=nuevo_usuario)
    if r.status_code == 200:
        return r.json
    else:
        return {'ERROR': 'Error desconocido'}





print("1. Animales")
print("2. Comida")
print("3. Especie")
print("4. Habitats")
print("5. Usuarios")
print("6. Ventas")
print("7. Veterinarios")
opcion = input("Escoja una tabla: \n")

if opcion == 1:
    crear_usuario()
