"""
Práctica 1: Motor de Búsqueda (enlaces)
	Objetivo: Construir un motor de búsqueda de información en Internet
----------------------------------------------------------------------------
Libreria para MongoDB
    pip install pymongo
Libreria para Request
    pip install requests
Libreria de BeautifulSoup
    pip install beautifulsoup4
"""

#Librerias
from pymongo import MongoClient
from webScraping import getLinks

#Inicia el motor
def motorBusqueda(coleccion):
    salir = True
    while salir:
        # Optener el primer elemento que no esta revisado
        jsonQuery = coleccion.find_one({'revisada': False})
        if (jsonQuery):
            #Extraer los enlaces de la pagina
            print(str(jsonQuery['direccion']))
            links = getLinks(jsonQuery['direccion'])
            #Actualizar la revision de la pagina
            coleccion.update_one({"_id": jsonQuery['_id']}, {"$set": {"revisada": True}})
            # Obtener enlaces
            for url in links:
                pag_existe = coleccion.find_one({'direccion': url})
                if (pag_existe):
                    coleccion.update_one({"_id": pag_existe['_id']}, {"$set": {"ranking": (pag_existe['ranking'] + 1)}})
                else:
                    registroNuevo = {
                        "direccion": url,
                        "titulo": "",
                        "keywords": "",
                        "descripcion": "",
                        "palabra1": "",
                        "palabra2": "",
                        "palabra3": "",
                        "ranking": 0,
                        "revisada": False
                    }
                    coleccion.insert_one(registroNuevo)
        else:
            print("No hay mas paginas por buscar")
            salir = False

#Funcion Principal
def main():
    # Conectar con el servidor de mongo DB
    cliente = MongoClient()
    db = cliente['AGVD_Motor_Busqueda']  # Base de datos
    coleccion = db['Index_Paginas']  # Coleccion (Tabla)
    # Contar el numero de registros en la BD y si es 0 insertear el primer dato
    if coleccion.count_documents({}) == 0:
        # Insertar
        registroInicial = {
            "direccion": "http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm",
            "titulo": "",
            "keywords": "",
            "descripcion": "",
            "palabra1": "",
            "palabra2": "",
            "palabra3": "",
            "ranking": 0,
            "revisada": False
        }
        coleccion.insert_one(registroInicial)
    # Iniciamos el motor
    print('Buscando paginas en la WEB')
    motorBusqueda(coleccion)

if __name__ == '__main__':
    main()