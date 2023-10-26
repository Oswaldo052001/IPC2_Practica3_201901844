##IMPORTS
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

## LLAMADAS ENPOINTS
from endpoints.pelicula import pelicula_service


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
socket = SocketIO(app, cors_allowed_origins="*")

##ENDPOINTS 
""" Blueprint

    CineGuatemala

    -> Pelicula 
        . Crear pelicula        (LISTO)
        . Buscar pelicula       (LISTO)
        . Actualizar pelicula   (LISTO)
"""

app.register_blueprint(pelicula_service, url_prefix="/api")


##ENDPOINTS
@app.route('/', methods = ['GET','POST','PUT'])
def init():
     return jsonify({
        "Curso"    : "Introducción a la programación y computación 1"
    })

## INIT
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port='3000', debug = True)

