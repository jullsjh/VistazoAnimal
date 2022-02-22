#importamos flask
from flask import Flask, request, abort
#instanciamos la clase , creamos un nuevo objeto y le pasamos el __name__
application = Flask(__name__)


#------------- 1. el @ se llama decorador, esto es una llamada http -------------
@application.route("/", methods=['GET'])#esto es el endpoint raiz
def hello_world():
    if request.method == 'GET':
        return "<h1>Hellossss: API Levantada!</h1>"
    return "<h1>Adios muy buenas</h1>"

# #por defecto esto se trata peticiones get
# @application.route("/saludo")
# def saludo():
#     return "<h1>Un saludo</h1>"


@application.route("/saludo", methods=['GET'])
def saludo():
    return "<h1>Un saludo 1</h1>"

@application.route("/saludo", methods=['POST'])
def despedida():
    return "<h1>Esto es un POST de despedida</h1>"



#2. --------------- flask nos permite parametrizar el endpoint, nunca se recibe un dato sin tratarlo ---------------
@application.route("/saludo/<name>", methods=['GET'])
def saludo_persona(name):
    if name.lower() == 'paco':
        abort(400)
    return f'<h1>un saludo {name}</h1>'

@application.errorhandler(400)
def error_400(error):
    return 'No tienes ni idea', 400



#3. ------------- se puede especificar el tipo de dato que vas a recibir con la palabra int: dentro del application.route -------------
@application.route("/saludo/<int:numero>", methods=['GET'])
def saludo_persona_numero(numero):
    print(type(numero))
    return f'<h1>hola {numero}</h1>'



# hola






#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



