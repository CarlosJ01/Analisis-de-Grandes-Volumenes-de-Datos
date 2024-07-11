"""
Práctica 2: Motor de Búsqueda (indexado)
	Objetivo: Construir un motor de búsqueda de información en Internet
----------------------------------------------------------------------------
Libreria para MongoDB
    pip install pymongo
Libreria para Request
    pip install requests
Libreria de BeautifulSoup
    pip install beautifulsoup4
Libreria de NLTK
    pip install nltk
    python -m nltk.downloader all
"""
import pymongo
from pymongo import MongoClient
from webScraping import extraccion


# Inicia el motor
def motorBusqueda(coleccion):
    salir = True
    while salir:
        # Optener el primer elemento que no esta revisado
        jsonQuery = coleccion.find_one({'revisada': False})
        if (jsonQuery):
            print(jsonQuery['direccion'])
            datos = extraccion(jsonQuery['direccion'])
            print(datos)
            print('')
            if (len(datos) == 0):
                coleccion.update_one({"_id": jsonQuery['_id']}, {"$set": {"revisada": True}})
            else:
                coleccion.update_one({"_id": jsonQuery['_id']}, {
                    "$set": {
                        "titulo": datos[0],
                        "keywords": datos[1],
                        "descripcion": datos[2],
                        "palabra1": datos[3][0][0],
                        "ranking1": datos[3][0][1],
                        "palabra2": datos[3][1][0],
                        "ranking2": datos[3][1][1],
                        "palabra3": datos[3][2][0],
                        "ranking3": datos[3][2][1],
                        "revisada": True
                    }
                })
                # Obtener enlaces
                for url in datos[4]:
                    pag_existe = coleccion.find_one({'direccion': url})
                    if (pag_existe):
                        coleccion.update_one({"_id": pag_existe['_id']}, {"$set": {"ranking": (pag_existe['ranking'] + 1)}})
                    else:
                        coleccion.insert_one({
                            "direccion": url,
                            "titulo": "",
                            "keywords": "",
                            "descripcion": "",
                            "palabra1": "",
                            "ranking1": 0,
                            "palabra2": "",
                            "ranking2": 0,
                            "palabra3": "",
                            "ranking3": 0,
                            "ranking": 0,
                            "revisada": False
                        })
        else:
            print("No hay mas paginas por buscar")
            salir = False

# Funcion principal
def main():
    # Conectar con el servidor de mongo DB
    cliente = MongoClient()
    db = cliente['AGVD_Motor_Busqueda']  # Base de datos
    coleccion = db['Index_Paginas_Web']  # Coleccion (Tabla)

    # Contar el numero de registros en la BD y si es 0 insertear el primer dato
    if coleccion.count_documents({}) == 0:
        # Insertar
        registroInicial = {
            "direccion": "http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm",
            "titulo": "",
            "keywords": "",
            "descripcion": "",
            "palabra1": "",
            "ranking1": 0,
            "palabra2": "",
            "ranking2": 0,
            "palabra3": "",
            "ranking3": 0,
            "ranking": 0,
            "revisada": False
        }
        coleccion.insert_one(registroInicial)

    # Iniciamos el motor
    motorBusqueda(coleccion)

#Inicio
if __name__ == '__main__':
    main()
