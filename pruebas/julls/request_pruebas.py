import requests, json, os

BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))


def search_animal():
    input_animal = input("Escribe el nombre del animal que quieres buscar: ")
    r = requests.get(f'{BASE_URL}search_animal/{input_animal}')

    if r.status_code != 200:
        return []
    else:
        return r.json()


animalitos = search_animal()
print(animalitos)

