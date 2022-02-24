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






