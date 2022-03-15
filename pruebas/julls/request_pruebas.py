from flask import request
import requests, json, os

BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))

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
login_usuario()



# --------------------------------------------ANIMALES----------------------------------------
def all_animals():
    r = requests.get(f'{BASE_URL}animals', headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(all_animals())

def buscar_animal():
    global token_user
    global headers
    print("------------------- Buscar un animal por su nombre ------------------- \n")
    nombre = input("Nombre del animal: ")
    buscar_animal = {'nombre': nombre}
    r = requests.get(f'{BASE_URL}animals/search', json=buscar_animal, headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(buscar_animal())

def new_animal():
    global token_user
    global headers
    print("------------------- Insertar nuevo animal ------------------- \n")
    nombre = input("Nombre del animal: ")
    tamanno = input("Tamaño del animal: ")
    peso = input("Peso del animal: ")
    nombre_habitat = input("Introduce el nombre del habitat del animal: ")
    nombre_especie = input("Introduce el nombre cientifico de la especie del animal: ")
    nuevo_animal = {
        'nombre': nombre,
        'tamanno': tamanno,
        'peso': peso,
        'nombre_habitat': nombre_habitat, #hay que introducir nombre
        'nombre_especie': nombre_especie #hay que introducir nombre
    }
    r = requests.post(f'{BASE_URL}animals', json=nuevo_animal, headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(new_animal())

def update_animal():
    global token_user
    global headers
    print("------------------- Actualizar animal ------------------- \n")
    id = input("Introduce el ID del animal que quieres actualizar: ")
    nombre = input("Nombre del nuevo animal: ")
    tamanno = input("Tamaño del nuevo animal: ")
    peso = input("Peso del nuevo animal: ")
    nombre_habitat = input("Introduce el nombre del habitat del animal: ")
    nombre_especie = input("Introduce el nombre cientifico de la especie del animal: ")
    actualizar_animal = {
        'nombre': nombre,
        'tamanno': tamanno,
        'peso': peso,
        'nombre_habitat': nombre_habitat, #hay que introducir nombre
        'nombre_especie': nombre_especie #hay que introducir nombre
    }
    r = requests.put(f'{BASE_URL}animals/{id}', json=actualizar_animal, headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(update_animal())

def delete_animal():
    global token_user
    global headers
    print("------------------- Eliminar un animal ------------------- \n")
    id = input("Introduce el ID del animal que quieres eliminar: ")
    borrar_animal = {
        'id': id,
    }
    r = requests.delete(f'{BASE_URL}animals/search/{id}', json=borrar_animal, headers=headers)
    if (r.status_code == 200):
        return r.json
    else:
        return r.json
# print(delete_animal())


# --------------------------------------------HABITATS----------------------------------------
def all_habitats():
    r = requests.get(f'{BASE_URL}habitats', headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(all_habitats())

def new_habitat():
    global token_user
    global headers
    print("------------------- Insertar nuevo habitat ------------------- \n")
    nombre = input("Nombre del habitat: ")
    nuevo_habitat = {
        'nombre': nombre,
    }
    r = requests.post(f'{BASE_URL}habitat', json=nuevo_habitat, headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(new_habitat())

def update_habitat():
    global token_user
    global headers
    print("------------------- Actualizar habitat ------------------- \n")
    id = input("Introduce el ID del habitat que quieres actualizar: ")
    nombre = input("Nombre del nuevo habitat: ")
    actualizar_habitat = {
        'nombre': nombre,
    }
    r = requests.put(f'{BASE_URL}habitat/{id}', json=actualizar_habitat, headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(update_habitat())

def delete_habitat():
    global token_user
    global headers
    print("------------------- Eliminar un habitat ------------------- \n")
    id = input("Introduce el ID del habitat que quieres eliminar: ")
    borrar_habitat = {
        'id': id,
    }
    r = requests.delete(f'{BASE_URL}habitat/{id}', json=borrar_habitat, headers=headers)
    if (r.status_code == 200):
        return r.json
    else:
        return r.json
# print(delete_habitat())


# --------------------------------------------COMIDAS----------------------------------------
def all_comidas():
    r = requests.get(f'{BASE_URL}food', headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(all_comidas())

def new_comida():
    global token_user
    global headers
    print("------------------- Insertar nueva comida ------------------- \n")
    nombre = input("Nombre de la comida: ")
    cantidad = input("Introduce la cantidad: ")
    nueva_comida = {
        'nombre': nombre,
        'cantidad': cantidad
    }
    r = requests.post(f'{BASE_URL}food', json=nueva_comida, headers=headers)
    if (r.status_code == 200):
        return r.json
    else:
        return r.json()
# print(new_comida())

def update_comida():
    global token_user
    global headers
    print("------------------- Actualizar comida ------------------- \n")
    id = input("Introduce el ID de la comida que quieres actualizar: ")
    nombre = input("Nombre de la nueva comida: ")
    cantidad = input("Nombre de la nueva cantidad: ")
    actualizar_comida = {
        'nombre': nombre,
        'cantidad': cantidad
    }
    r = requests.put(f'{BASE_URL}food/{id}', json=actualizar_comida, headers=headers)
    if (r.status_code == 200):
        return r.json()
    else:
        return r.json()
# print(update_comida())

def dar_comida_animal():
    global token_user
    global headers
    print("------------------- Dar de comer a un animal ------------------- \n")
    # id = input("Introduce el ID de la comida que quieres actualizar: ")
    nombre = input("Nombre del animal al que vas a alimentar: ")
    dar_comida = {
        'nombre_animal': nombre
    }
    r = requests.put(f'{BASE_URL}food/specie', json=dar_comida, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        return r.json()
# print(dar_comida_animal())

def delete_comida():
    global token_user
    global headers
    print("------------------- Eliminar una comida ------------------- \n")
    id = input("Introduce el ID de la comida que quieres eliminar: ")
    borrar_comida = {
        'id': id,
    }
    r = requests.delete(f'{BASE_URL}food/{id}', json=borrar_comida, headers=headers)
    if (r.status_code == 200):
        return r.json
    else:
        return r.json
# print(delete_comida())












