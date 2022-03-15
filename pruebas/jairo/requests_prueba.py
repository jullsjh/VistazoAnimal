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
    # login_usuario = {
    #     'email': email_usuario,
    #     'pass': pass_usuario
    # }
    login_usuario = {
        'email': "j@gmail.com",
        'pass': "jairo1234"
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
    usuario_mod = {
        'nombre': nombre,
        'apellido1': apellido1,
        'apellido2': apellido2,
        'email': email,
        'telefono': telefono,
        'password': password,
        'type':100
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




if int(opcion) == 3:
    print(crear_nueva_especie())
    print(obtener_especies())
    print(obtener_especie_id())
    print(obtener_animales_especie())
    print(eliminar_especie_id())
    print(modificar_especie_id())

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