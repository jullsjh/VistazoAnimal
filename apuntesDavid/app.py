# ------------------------ TUTORIAL YT ------------------------
from crypt import methods
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)


# propiedad donde definimos donde esta la bbdd, servidor, nombre bbdd, puerto...
app.config['MONGO_URI'] = 'mongodb://localhost:27017//tutorialYTdb'
# le paso la config a la conexion para poder manipular las colecciones/insertar datos etc
PyMongo(app)


# Ruta para CREAR datos
@app.route('/users', methods=['POST'])
def create_user():
    pass








if __name__ == "__main__":
    app.run(debug=True)
