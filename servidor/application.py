#importamos flask
# from multiprocessing.connection import Client
from flask import Flask, request, abort
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB+Compass&ssl=false')

#instanciamos la clase , creamos un nuevo objeto y le pasamos el __name__
# application = Flask(__name__)

# BBDD
mongodb = client.VistazoAnimal


# ----------------------------- ANIMALES -----------------------------
# Buscar animal
input_animal = input("Escribe nombre del animal que quieres buscar \n")
filter = {'nombre': input_animal}
# filter = {'nombre': 'Brown pelican'}
# projection = {'id_habitat': 1}

animales = list(mongodb.animales.find(filter))
for animal in animales:
    print(animal)


# ----------------------------- USUARIOS -----------------------------


# 0 se muestra todo menos eso
# muestra lo que tiene 1
# projection es las columnas del select
# filter es el where





#Si el servidor se lleva a produccion se quita la parte de debug
# if __name__ == '__main__':
#     application.run(debug=True)



