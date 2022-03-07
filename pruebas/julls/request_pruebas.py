from flask import request
import requests, json, os

BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))


# -------------------------------- GET --------------------------------
# 1
def search_animal():
    input_animal = input("Escribe el nombre del animal que quieres buscar: ")
    r = requests.get(f'{BASE_URL}search_animal/{input_animal}')

    if r.status_code != 200:
        return []
    else:
        return r.json()

animalitos = search_animal()
print(animalitos)

# 2
# obtengo todas las praderas (aunque no se si este def es necesario)
def get_all_habitats():
    r = requests.get(f'{BASE_URL}habitats')
    if r.status_code != 200:
        return []
    else:
        return r.json()
        
habitats = get_all_habitats()
print(habitats)

def search_animal_from_habitat():
    input_habitat = input("Escribe el nombre del habitat del animal que quieres buscar: ")
    r = requests.get(f'{BASE_URL}search_animal_from_habitat/{input_habitat}')

    if r.status_code != 200:
        return []
    else:
        return r.json()

habitats = search_animal_from_habitat()
print(habitats)








# --------------------------------------------NUEVO----------------------------------------
# ------------- ANIMALES
# -------------------------------- GET --------------------------------
# -------------------------------- POST --------------------------------
def new_animal():
    print("------------------- Registro de animales ------------------- \n")
    nombre = input("Nombre del animal: ")
    tamanno = input("Tamaño del animal: ")
    peso = input("Peso del animal: ")
    id_habitat = input("Introduce el ID habitat del animal: ")
    id_especie = input("Introduce el ID especie del animal: ")

    nuevo_animal = {
        'nombre': nombre,
        'tamanno': tamanno,
        'peso': peso,
        'id_habitat': id_habitat,
        'id_especie': id_especie
    }

    r = requests.post(f'{BASE_URL}/animales/nuevo', json=nuevo_animal)
    if (r.status_code == 200):
        return r.json
    else:
        return {'ERROR': 'Error desconocido'}


# -------------------------------- PUT --------------------------------
# -------------------------------- DELETE --------------------------------





