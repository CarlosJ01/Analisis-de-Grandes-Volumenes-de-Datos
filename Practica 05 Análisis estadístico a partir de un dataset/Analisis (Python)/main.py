"""
Práctica 5: Análisis estadístico a partir de un dataset
Equipo 5
    Castro Cazares Carlos Jahir (Responsable)
    Martinez Resendiz Giovanni Hasid
    Velazquez Aguilar Jaime Isai
##################
#######################################
Librerias
    Pandas => pip install pandas
    LXML => pip install lxml
    progress => pip install progress
"""
import pandas as pd
from lxml import objectify
from progress.bar import Bar
from progress.spinner import Spinner
import os

# Direccion del servidor (Cambiar)
servidor = "http://localhost/AGVD/Practica05/"

# Metodo Main
if __name__ == '__main__':
    # Abriendo el documento de prices.xml
    xml_prices= objectify.parse('datasets/prices.xml')  # Parse XML data
    root = xml_prices.getroot()  # Root element

    # Elementos del xml y json para el pandas
    elementos = root.getchildren()
    precios = {
        'id': [],
        'regular': []
    }

    # Leyendo los e indexando los precios en xml
    with Bar('Leyendo XML de prices.xml', max=len(elementos)) as bar:
        child = {}
        sub = {}
        for i in range(len(elementos)):
            child = elementos[i]
            sub = child.getchildren()[0]
            if sub.attrib['type'] == "regular":
                precios['id'].append(child.attrib['place_id'])  # Get id
                precios['regular'].append(sub.text) # Get precio
            bar.next()

    # Creando dataframe de pandas para manipular los datos de mejor manera
    print("\n####################### DataFrame Obtenido ###############################")
    df_prices = pd.DataFrame(precios)
    print(df_prices)

    # Analizando la informacion
    print("\n####################### Obteniendo Datos Estadisticos ###############################")
    media = df_prices['regular'].astype(float).mean()  # Media
    mediana = df_prices['regular'].astype(float).median()  # Mediana
    moda = df_prices['regular'].astype(float).mode()  # Moda
    desv_est = df_prices['regular'].astype(float).std()  # Desviacion estandar
    mayor = df_prices['regular'].astype(float).max()  # Mayor
    id_mayor = df_prices[df_prices.regular.astype(float) == mayor].reset_index()['id'][0]
    menor = df_prices['regular'].astype(float).min()  # Menor
    id_menor = df_prices[df_prices.regular.astype(float) == menor].reset_index()['id'][0]

    print("Promedio del precio de la gasolina: " + str(media))
    print("Valor central de la gasolina: " + str(mediana))
    print("Valor más común de la gasolina: " + str(moda[0]))
    print("Grado de dispersión de los diferentes precios de la gasolina: " + str(desv_est))
    print("Precio más alto de la gasolina: " + str(mayor))
    print("Precio más bajo de la gasolina: " + str(menor))

    # Abriendo el documento de places.xml
    xml_places = objectify.parse('datasets/places.xml')  # Parse XML data
    root = xml_places.getroot()  # Root element
    elementos = root.getchildren()
    gasolineraMayor = {
        'nombre': '',
        'longitud': '',
        'latitud': ''
    }
    gasolineraMenor = {
        'nombre': '',
        'longitud': '',
        'latitud': ''
    }
    encontradoMayor = False
    encontradoMenor = False

    # Buscando las gasolineras mas barata y cara
    print('\n#####################################################################################')
    spinner = Spinner('Buscando la gasolinera en places')
    for i in range(len(elementos)):
        # Romper el ciclo si se encontraron los dos
        if encontradoMayor and encontradoMenor:
            break
        # Obtener el elmento
        child = elementos[i]  # Places
        # Encontrar el mayor
        if not encontradoMayor:
            if child.attrib['place_id'] == id_mayor:
                subelementos = child.getchildren()
                cordenadas = subelementos[2].getchildren()
                gasolineraMayor['nombre'] = subelementos[0].text
                gasolineraMayor['longitud'] = cordenadas[0].text
                gasolineraMayor['latitud'] = cordenadas[1].text
                encontradoMayor = True
        # Encontrar el menor
        if not encontradoMenor:
            if child.attrib['place_id'] == id_menor:
                subelementos = child.getchildren()
                cordenadas = subelementos[2].getchildren()
                gasolineraMenor['nombre'] = subelementos[0].text
                gasolineraMenor['longitud'] = cordenadas[0].text
                gasolineraMenor['latitud'] = cordenadas[1].text
                encontradoMenor = True
        spinner.next()

    # Mostrar las gasolineras encontradas
    print("\n\n####################### Gasolineras Encontradas ###############################")
    print("Gasolineria con el precio mas alto: ")
    print(gasolineraMayor)
    print("\nGasolineria con el precio mas bajo: ")
    print(gasolineraMenor)

    # Crear el link para mostrar el mapa
    print("\n\n####################### Link del Mapa ###############################\n")
    direccion = servidor + "?" + "nombre1="+ gasolineraMayor['nombre'] + "&longitud1=" + gasolineraMayor['longitud'] + "&latitud1=" + gasolineraMayor['latitud']\
                + "&nombre2="+ gasolineraMenor['nombre'] + "&longitud2=" + gasolineraMenor['longitud'] + "&latitud2=" + gasolineraMenor['latitud']\
                + "&presioMayor="+str(mayor) + "&presioMenor="+str(menor)
    print(direccion+"\n")
    # Abrir con windows
    os.system('start chrome "'+direccion+'"')
    # Abrir con OSX
    os.system('open "'+direccion+'"')
    # Abrir con Ubuntu
    os.system('/usr/bin/firefox "'+direccion+'"')
    
    print("\n* Si no abre el navegador copie y pegue la dirección de arriba en el navegador para abrir la pagina con el mapa y su localización de cada gasolinera\n")