#importamos flask
from flask import Flask, request, abort
#instanciamos la clase , creamos un nuevo objeto y le pasamos el __name__
application = Flask(__name__)







#Si el servidor se lleva a produccion se quita la parte de debug
if __name__ == '__main__':
    application.run(debug=True)



