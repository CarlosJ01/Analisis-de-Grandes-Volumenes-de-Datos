#Libreria para Bottle levantar un Web Services
#   pip install bottle
#Libreria para MongoDB
#    pip install pymongo

import bottle
import re
from bottle import response
from limpieza import depurar
from pymongo import MongoClient

app = bottle.app()

#CORS
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@app.route('/cors', method=['OPTIONS', 'GET'])
@enable_cors
def cors():
    response.headers['Content-type'] = 'application/json'
    return '[1]'

@app.route('/buscar/<query>', method=['OPTIONS', 'POST'])
@enable_cors
def buscar(query):
    #Depurar la frase a buscar
    palabras = depurar(query)

    #Conexion con Mongo DB
    cliente = MongoClient()
    db = cliente['AGVD_Motor_Busqueda']
    coleccion = db['Index_Paginas_Web']

    like = re.compile('.*'+palabras[0][0]+'.*', re.IGNORECASE)
    links0 = coleccion.find({"keywords": like, 'revisada': True}).sort('ranking')
    links1 = coleccion.find({"palabra1": like, 'revisada': True}).sort('ranking')
    links2 = coleccion.find({"palabra2": like, 'revisada': True}).sort('ranking')
    links3 = coleccion.find({"palabra3": like, 'revisada': True}).sort('ranking')

    data = {}
    data['links'] = []
    for link in links0:
        data['links'].append({'url': link['direccion'], 'titulo': link['titulo'], 'keywords': link['keywords'],
                              'descripcion': link['descripcion']})
    for link in links1:
        data['links'].append({'url': link['direccion'], 'titulo': link['titulo'], 'keywords': link['keywords'],
                              'descripcion': link['descripcion']})
    for link in links2:
        data['links'].append({'url': link['direccion'], 'titulo': link['titulo'], 'keywords': link['keywords'],
                              'descripcion': link['descripcion']})
    for link in links3:
        data['links'].append({'url': link['direccion'], 'titulo': link['titulo'], 'keywords': link['keywords'],
                              'descripcion': link['descripcion']})
    return (data)

app.run(port=8080)