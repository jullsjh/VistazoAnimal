from time import process_time_ns
import requests, json, os, jwt
from hashlib import sha256
BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))
token_user = None
headers={}
permisos = None

def login_usuario():
    global token_user
    global headers
    print("------------Login de usuario------------")
    email_usuario = input("Introduzca un email para loguearse en su cuenta: \n")
    pass_usuario = input("Introduzca una contraseña para loguearse en su cuenta \n")
    hashed_password = sha256(pass_usuario.encode('utf-8')).hexdigest()
    login_usuario = {
        'email': email_usuario,
        'pass': hashed_password
    }

    auth = requests.post(f'{BASE_URL}login', json=login_usuario)
    token_user = auth.json()['token']
    # token_2 = jwt.decode(token_user)
    # print(token_2)
    #permisos_user = auth.json()['id']
    print(token_user)
    headers = {
        'Authorization': 'Bearer ' + token_user
    }


#--------------- Usuarios ---------------

def obtener_permisos():
    global permisos
    r = requests.get(f'{BASE_URL}permisos', headers=headers)
    permisos_json = r.json()
    permisos = permisos_json['type']
    return permisos

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
    print("------------ Usuario ------------")
    user_id = input("Introduce el id del usuario a buscar: \n")
    r = requests.get(f'{BASE_URL}users/{user_id}', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

#request para borrar un usuario mediante su id
def borrar_usuario_id():
    print("------------ Borrar Usuario ------------")
    user_id = input("Introduce el id del usuario para borrar: \n")
    r = requests.delete(f'{BASE_URL}users/{user_id}', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

#request para modificar un usuario mediante su id
def modificar_usuario_id():
    print("------------ Modificar Usuario ------------")
    print("Espacio en blanco para NO modificar")
    user_id = input("Introduce el id del usuario para modificar: \n")
    nombre = input("Introduzca un nombre: \n")
    apellido1 = input("Introduzca su primer apellido: \n")
    apellido2 = input("Introduzca su segundo apellido: \n")
    email = input("Introduzca su email: \n")
    telefono = input("Introduzca su telefono: \n")
    password = input("Introduzca una contraseña: \n")
    type = input("introduza el tipo de usuario: \n")
    usuario_mod = {
        'nombre': nombre,
        'apellido1': apellido1,
        'apellido2': apellido2,
        'email': email,
        'telefono': telefono,
        'password': password,
        'type':type
    }
    r = requests.put(f'{BASE_URL}users/{user_id}',json=usuario_mod,headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)


#--------------- Ventas ---------------


def crear_venta_usuario_log():
    print("------------ Compra de entradas ------------")
    cantidad = input("Introduzca la cantidad: \n")
    nueva_venta = {
        'cantidad': cantidad
    }
    r = requests.post(f'{BASE_URL}users/sales',json=nueva_venta,headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def obtener_ventas_usuario_log():
    print("------------ Compras realizadas ------------")
    r = requests.get(f'{BASE_URL}users/sales',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def obtener_ventas_id_usuario():
    print("------------ Compras realizadas ------------")
    user_id = input("Introduce el id de usuarios para consultar ventas \n")
    r = requests.get(f'{BASE_URL}users/sales/{user_id}',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def borrar_venta_id():
    print("------------ Eliminar Compra ------------")
    user_id = input("Introduce el id de la venta que va a ser eliminada \n")
    r = requests.delete(f'{BASE_URL}users/sales/{user_id}',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def modificar_venta_id():
    print("------------ Modificacion Compra ------------")
    venta_id = input("Introduzca el id de la venta: \n")
    cantidad = input("Introduzca la nueva cantidad: \n")
    venta_mod = {
        'cantidad': cantidad
    }
    r = requests.put(f'{BASE_URL}users/sales/{venta_id}',json=venta_mod,headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)


#--------------- Especies ---------------


def crear_nueva_especie():
    print("------------ Creacion Especie ------------")
    nombre_vulgar = input("Introduzca el nombre vulgar: \n")
    nombre_cientifico = input("Introduzca el nombre cientifico: \n")
    descripcion = input("Introduzca la descripcion: \n")
    comida_nombre = input("Introduzca el nombre de la comida \n")
    nueva_especie = {
        'nombre_cientifico': nombre_cientifico,
        'nombre_vulgar': nombre_vulgar,
        'descripcion': descripcion,
        'comida_nombre': comida_nombre
    }
    r = requests.post(f'{BASE_URL}species',json=nueva_especie,headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def obtener_especies():
    print("------------ Especies existentes ------------")
    r = requests.get(f'{BASE_URL}species',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def obtener_especie_id():
    print("------------ Buscar especie ------------")
    especie_id = input("Introduce el id de de la especie para buscar \n")
    r = requests.get(f'{BASE_URL}species/{especie_id}',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

#Obtener los animales de una especie
def obtener_animales_especie():
    print("------------ Obtener animales especie ------------")
    nombre_cientifico = input("Introduce el nombre cientifico de la especie para obtener sus animales \n")
    r = requests.get(f'{BASE_URL}species/find/{nombre_cientifico}',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def eliminar_especie_id():
    print("------------ Eliminar Especie ------------")
    especie_id = input("Introduce el id de la especie que va a ser eliminada \n")
    r = requests.delete(f'{BASE_URL}species/{especie_id}',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def modificar_especie_id():
    print("------------ Modificar especie ------------")
    print("Espacio en blanco si no se quire modificar \n")
    especie_id = input("Introduzca el id de la especie para modificar \n")
    nombre_vulgar = input("Introduzca el nombre vulgar \n")
    nombre_cientifico = input("Introduzca el nombre cientifico \n")
    descripcion = input("Introduzca una descripcion \n")
    especie_mod = {
        'nombre_cientifico': nombre_cientifico,
        'nombre_vulgar': nombre_vulgar,
        'descripcion': descripcion
    }
    r = requests.put(f'{BASE_URL}species/{especie_id}',json=especie_mod,headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)


#--------------- VETERINARIOS ---------------

#Crear un veterinario asignando una especie
def crear_veterinario_con_especie():
    print("------------ Creacion Veterinario ------------")
    nombre = input("Introduce el nombre del veterinario: \n")
    apellido1 = input("Introduce el primer apellido del veterinario: \n")
    apellido2 = input("Introduce el segundo apellido del veterinario: \n")
    estado = input("Introduzca si el veterinario esta libre o asignado \n")
    especie_nombre = input("Introduzca el nombre de la especie \n")
    nuevo_vet = {
        'nombre': nombre,
        'apellido1': apellido1,
        'apellido2': apellido2,
        'especie_nombre': especie_nombre,
        'estado': estado
    }
    r = requests.post(f'{BASE_URL}veterinary',json=nuevo_vet,headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def obtener_veterinarios():
    print("------------ Obtener Veterinarios ------------")
    r = requests.get(f'{BASE_URL}veterinary',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def obtener_veterinario_id():
    print("------------ Obtener Veterinarios por id ------------")
    vet_id = input("Ingrese el id del veterinario para obtener \n")
    r = requests.get(f'{BASE_URL}veterinary/{vet_id}',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def eliminar_veterinario_id():
    print("------------ Eliminar Veterinarios por id ------------")
    vet_id = input("Ingrese el id del veterinario para obtener \n")
    r = requests.delete(f'{BASE_URL}veterinary/{vet_id}',headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def modificar_veterinario_id():
    print("------------ Modificar Veterinarios por id ------------")
    vet_id = input("Ingrese el id del veterinario a modificar \n")
    print("Introduzca los campos para actualizarlos")
    nombre = input("Introduce el nombre \n")
    apellido1 = input("Introduce el primer apellido\n")
    apellido2 = input("Introduce el segundo apellido \n")
    especie_nombre = input("Introduce el nombre de la especie \n")
    estado = input("Introduce un cambio en el estado \n")
    vet_mod = {
        'nombre': nombre,
        'apellido1': apellido1,
        'apellido2': apellido2,
        'especie_nombre': especie_nombre,
        'estado': estado
    }
    r = requests.put(f'{BASE_URL}veterinary/{vet_id}',json=vet_mod, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

#asignar una especie a un veterinario libre
def asignar_especie_veterinario():
    print("------------ Asignar especie a veterinario ------------")
    nombre = input("Ingrese el nombre del veterinario \n")
    apellido1 = input("Ingrese el primer apellido del veterinario \n")
    apellido2 = input("Ingrese el segundo apellido del veterinario \n")
    especie_nombre = input("Ingrese la especie para asignarla al veterinario")
    vet_assign = {
        'nombre': nombre,
        'apellido1': apellido1,
        'apellido2': apellido2,
        'especie_nombre': especie_nombre
    }
    r = requests.put(f'{BASE_URL}veterinary/assign',json=vet_assign, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)


#--------------- ANIMALES ---------------

def obtener_animales():
    print("------------ Obtener animales ------------")
    r = requests.get(f'{BASE_URL}animals', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def registrar_varios_animales():
    print("------------ Registar varios animales ------------")
    #numero_animales = input("Ingrese la cantidad de animales que va a ingresar")
    lista = []
    respuesta = "Y"
    while respuesta == "Y":
        nombre = input("Introduce un nombre para el animal \n")
        tamanno = input("Introduce el tamaño del animal \n")
        peso = input("Introduce el peso del animal \n")
        nombre_especie = input("Introduce el nombre cientifico de la especie \n")
        nombre_habitat = input("Introduce el nombre del habitat del animal \n")
        new_animal = {
            'nombre': nombre,
            'tamanno': tamanno,
            'peso': peso,
            'nombre_especie': nombre_especie,
            'nombre_habitat': nombre_habitat
        }
        lista.append(new_animal)
        print(lista)
        respuesta = input("Desea introducir mas animales? Y/N \n")
    r = requests.post(f'{BASE_URL}animals/create',json=lista, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def crear_animal():
    print("------------------- Insertar nuevo animal ------------------- \n")
    nombre = input("Nombre del animal: \n")
    tamanno = input("Tamaño del animal: \n")
    peso = input("Peso del animal: \n")
    nombre_habitat = input("Introduce el nombre del habitat del animal: \n")
    nombre_especie = input("Introduce el nombre cientifico de la especie del animal: \n")
    nuevo_animal = {
        'nombre': nombre,
        'tamanno': tamanno,
        'peso': peso,
        'nombre_habitat': nombre_habitat, #hay que introducir nombre
        'nombre_especie': nombre_especie #hay que introducir nombre
    }
    r = requests.post(f'{BASE_URL}animal', json=nuevo_animal, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def buscar_animal_id():
    print("------------------- Buscar un animal por su id ------------------- \n")
    animal_id = input("introduce id del animal: \n")
    r = requests.get(f'{BASE_URL}animals/search/{animal_id}', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def modificar_animal_id():
    print("-------------------  Modificar animal ------------------- \n")
    animal_id = input("Introduce el id del animal: \n")
    print("Introduce los datos a modificar")
    nombre = input("Nombre del animal: \n")
    tamanno = input("Tamaño del animal: \n")
    peso = input("Peso del animal: \n")
    nombre_habitat = input("Introduce el nombre del habitat del animal: \n")
    nombre_especie = input("Introduce el nombre cientifico de la especie del animal: \n")
    nuevo_animal = {
        'nombre': nombre,
        'tamanno': tamanno,
        'peso': peso,
        'nombre_habitat': nombre_habitat, 
        'nombre_especie': nombre_especie 
    }
    r = requests.put(f'{BASE_URL}animal/{animal_id}', json=nuevo_animal, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def eliminar_animal_id():
    print("------------------- Eliminar un animal ------------------- \n")
    id = input("Introduce el ID del animal que quieres eliminar: \n")
    borrar_animal = {
        'id': id,
    }
    r = requests.delete(f'{BASE_URL}animals/search/{id}', json=borrar_animal, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)


#--------------- HABITATS ---------------

def obtener_habitats():
    print("------------------- Obtener habitats ------------------- \n")
    r = requests.get(f'{BASE_URL}habitats', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def crear_habitat():
    print("------------------- Insertar nuevo habitat ------------------- \n")
    nombre = input("Nombre del habitat: ")
    nuevo_habitat = {
        'nombre': nombre,
    }
    r = requests.post(f'{BASE_URL}habitat', json=nuevo_habitat, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def modificar_habitat_id():
    print("------------------- Actualizar habitat ------------------- \n")
    id = input("Introduce el ID del habitat que quieres actualizar: \n")
    nombre = input("Nombre del nuevo habitat: \n")
    actualizar_habitat = {
        'nombre': nombre,
    }
    r = requests.put(f'{BASE_URL}habitat/{id}', json=actualizar_habitat, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def eliminar_habitat_id():
    print("------------------- Eliminar un habitat ------------------- \n")
    id = input("Introduce el ID del habitat que quieres eliminar: \n")
    borrar_habitat = {
        'id': id,
    }
    r = requests.delete(f'{BASE_URL}habitat/{id}', json=borrar_habitat, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)


#--------------- COMIDAS ---------------
def obtener_comidas():
    print("------------------- Obtener comidas ------------------- \n")
    r = requests.get(f'{BASE_URL}food', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def crear_comida():
    print("------------------- Insertar nueva comida ------------------- \n")
    nombre = input("Nombre de la comida: \n")
    cantidad = input("Introduce la cantidad: \n")
    nueva_comida = {
        'nombre': nombre,
        'cantidad': cantidad
    }
    r = requests.post(f'{BASE_URL}food', json=nueva_comida, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def modificar_comida_id():
    print("------------------- Actualizar comida ------------------- \n")
    id = input("Introduce el ID de la comida que quieres actualizar: ")
    nombre = input("Nombre de la nueva comida: \n")
    cantidad = input("Cantida nueva: \n")
    actualizar_comida = {
        'nombre': nombre,
        'cantidad': cantidad
    }
    r = requests.put(f'{BASE_URL}food/{id}', json=actualizar_comida, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def elminar_comida_id():
    print("------------------- Eliminar una comida ------------------- \n")
    id = input("Introduce el ID de la comida que quieres eliminar: \n")
    r = requests.delete(f'{BASE_URL}food/{id}', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def dar_comida_animal():
    print("------------------- Dar de comer a un animal ------------------- \n")
    # id = input("Introduce el ID de la comida que quieres actualizar: ")
    nombre = input("Nombre del animal al que vas a alimentar: \n")
    dar_comida = {
        'nombre_animal': nombre
    }
    r = requests.put(f'{BASE_URL}food/specie', json=dar_comida, headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def obtener_comida_especie():
    print("------------------- Obtener comida de especie ------------------- \n")
    nombre_especie=input("Introduce el nombre de la especie \n")
    r = requests.get(f'{BASE_URL}species/food/{nombre_especie}', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)

def obtener_especie_comida():
    print("------------------- Obtener comida de especie ------------------- \n")
    nombre_comida=input("Introduce el nombre de la comida \n")
    r = requests.get(f'{BASE_URL}food/species/{nombre_comida}', headers=headers)
    if r.status_code == 200:
        return json.dumps(r.json(),indent=4)
    else:
        return json.dumps(r.json(),indent=4)



#print(crear_usuario())
login_usuario()
print(obtener_permisos())
print("1. Animales \n")
print("2. Comida \n")
print("3. Especie \n")
print("4. Habitats \n")
print("5. Usuarios \n")
print("6. Ventas \n")
print("7. Veterinarios \n")
opcion = input("Escoja una tabla: \n")


if int(opcion) == 1:
    if int(permisos) == 1:
        print(obtener_animales())
        print(registrar_varios_animales())
        print(crear_animal())
        print(buscar_animal_id())
        print(modificar_animal_id())
        print(eliminar_animal_id())
    elif int(permisos) > 5:
        print(obtener_animales())
        print(buscar_animal_id())


elif int(opcion) == 2:
    print(obtener_comidas())
    print(crear_comida())
    print(modificar_comida_id())
    print(elminar_comida_id())
    print(dar_comida_animal())
    print(obtener_comida_especie())
    print(obtener_especie_comida())

if int(opcion) == 3:
    print(crear_nueva_especie())
    print(obtener_especies())
    print(obtener_especie_id())
    print(obtener_animales_especie())
    print(eliminar_especie_id())
    print(modificar_especie_id())

if int(opcion) == 4:
    print(obtener_habitats())
    print(crear_habitat())
    print(modificar_habitat_id())
    print(eliminar_habitat_id())

if int(opcion) == 5:
    print(obtener_usuarios())
    print(obtener_usuario_id())
    print(borrar_usuario_id())
    print(modificar_usuario_id())

if int(opcion) == 6:
    print(crear_venta_usuario_log())
    print(obtener_ventas_usuario_log())
    print(obtener_ventas_id_usuario())
    print(borrar_venta_id())
    print(modificar_venta_id())

if int(opcion) == 7:
    print(crear_veterinario_con_especie())
    print(obtener_veterinarios())
    print(obtener_veterinario_id())
    print(eliminar_veterinario_id())
    print(modificar_veterinario_id())
    print(asignar_especie_veterinario())