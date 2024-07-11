"""
#######################################################
Práctica 3: Generación de Datasets
Objetivo: Generar datasets con datos aleatorios

Hacer un programa en Python (modo texto, aunque puede ser hecho en modo gráfico con Tkinter) que haga los siguientes pasos:
PASO 1: Preguntar datos
    Preguntar el número de registros a generar (filas).
    Preguntar el número de campos a generar (columnas), al menos debe soportar 10 campos.
    Preguntar por el tipo de datos que se almacenará en cada campo (los mínimos requeridos son entero, flotante, string, booleano, fecha, hora, aunque se pueden agregar más.).
    Preguntar por el tipo de dataset a generar (CSV, XML, JSON).
PASO 2: Generar el Dataset 1
    De acuerdo a los datos anteriores, se debe generar el "dataset_1" con datos aleatorios en cada campo.
    La primer fila corresponderá a los nombres de los campos.
    Los datos aleatorios serán cargados desde archivos de texto separados (por ejemplo nombres direcciones, etc.) o serán generados de manera aleatoria en ese momento (por ejemplo edades, temperaturas, etc.).
    Se debe generar el archivo "metadatos.txt" donde se debe incluir el nombre de los campos, tipo y descripción de cada uno de ellos.
PASO 3: Generar el Dataset 2 (incorrecto)
    Generar un "dataset_2" (igual al anterior con datos aleatorios) pero que se le inserten los siguientes errores de manera aleatoria (con máximo un 25% de registros con errores):
        Registros vacíos.
        Registros repetidos.
        Registros con algunos campos vacíos.
        Insertar datos erróneos (por ejemplo donde van sólo letras, insertar números).
        Intercambiar la letra "o" con el número "0".
        Datos fuera de rango (por ejemplo, edad = 500 ó edad = -5).
#######################################################
Librerias
Pandas
    pip install pandas
Numpy
    pip install numpy
#######################################################
"""
# Librerias
import pandas as pd
from readFiles import leerArchivos
from camposRandom import *
import numpy as np

# Tipo de datos
tipos = [
    [0, 'Nombre', 0],
    [1, 'Apellido', 0],
    [2, 'Edad', 0],
    [3, 'Genero', 0],
    [4, 'Correo', 0],
    [5, 'Estatura', 0],
    [6, 'Peso', 0],
    [7, 'Fecha', 0],
    [8, 'Hora', 0],
    [9, 'Soltero', 0]
]
# Configuracion
config = {
    'registros': 0,
    'campos': 0,
    'tipos': [],
    'formato': -1
}
# -----------------------------------------------

# Ingresar los tipos de datos de los campos
def tiposDatos():
    # Mostrar los tipos disponibles
    for tipo in tipos:
        if(tipo[2] == 0):
            print("\t["+str(tipo[0])+"] => "+str(tipo[1]))

    #Pedir el tipo y validarlo
    while True:
        seleccion = int(input("Selecciona una opción (Numero): "))
        for tipo in tipos:
            if tipo[2] == 0 and tipo[0] == seleccion:
                tipo[2] = 1
                config['tipos'].append(seleccion)
                return
# -----------------------------------------------

# Dataframe a XML
def generarXML(dataframe, nombre):
    def fila_a_xml(fila):
        xml = ['<item>']
        for i, col_name in enumerate(fila.index):
            xml.append('  <field name="{0}">{1}</field>'.format(col_name, fila.iloc[i]))
        xml.append('</item>')
        return '\n'.join(xml)

    xml = '\n'.join(dataframe.apply(fila_a_xml, axis=1))
    with open(nombre, 'w') as f:
        f.write(xml)
# -----------------------------------------------

# Main
if __name__ == '__main__':
    # Pedir el numero de registros y campos
    while (config['registros'] <= 0):
        config['registros'] = int(input("Ingresa el numero de registros del Dataset: "))
    while (config['campos'] > 10 or config['campos'] <= 0):
        config['campos'] = int(input("Ingresa el numero de campos para el Dataset (max 10): "))
    print('#########################################################################')

    # Pedir el nombre y tipo de los campos
    for i in range(config['campos']):
        print('Ingresa el tipo de dato para el '+str(i+1)+'° campo: ')
        tiposDatos()
    print('#########################################################################')

    # Pedir el formato
    print('Ingresa el formato para exportarlo: ')
    print("""
        [0] => CSV
        [1] => JSON
        [2] => XML
    """)
    while (config['formato'] > 2 or config['formato'] < 0):
        config['formato'] = int(input('Selecciona una opción (numero): '))
    print('#########################################################################')

    # Generacion del Data Set
    print('. . . GENERANDO DATASET . . .')
    # Leer los archivos
    listas = leerArchivos()
    # Creacion de registros segun los campos dados
    registros = {}
    metadatos = "Campo \t|\t Tipo \t\t|\t Descripcion \n"
    metadatos += "---------------------------------------------------------------------------------------------\n"
    for x in config['tipos']:
        if(x == 0):
            registros['nombre'] = [randomNombre(listas['nombres']) for x in range(config['registros'])]
            metadatos += "Nombre \t|\t String \t|\t Nombres de personas \n"
        elif(x == 1):
            registros['apellido'] = [randomNombre(listas['apellidos']) for x in range(config['registros'])]
            metadatos += "Apellido|\t String \t|\t Apellidos de personas \n"
        elif (x == 2):
            registros['edad'] = randomEdad(config['registros'])
            metadatos += "Edad \t|\t Entero \t|\t Edad de una persona (18 - 120) \n"
        elif (x == 3):
            registros['genero'] = randomGenero(config['registros'])
            metadatos += "Genero \t|\t Caracter \t|\t Genero de una persona (H o M) \n"
        elif (x == 4):
            registros['correo'] = [randomCorreo(listas['correos']) for x in range(config['registros'])]
            metadatos += "Correo \t|\t String \t|\t Direccion de correo electronico \n"
        elif (x == 5):
            registros['estatura'] = randomEstatura(config['registros'])
            metadatos += "Estatura|\t Flotante \t|\t Estatura de una persona con 2 digitos de presicion (1.5 - 2) \n"
        elif (x == 6):
            registros['peso'] = randomPeso(config['registros'])
            metadatos += "Peso \t|\t Flotante \t|\t Peso de una persona en Kg con 2 digitos de presicion (50 - 150) \n"
        elif (x == 7):
            registros['fecha'] = [randomFecha() for x in range(config['registros'])]
            metadatos += "Fecha \t|\t String \t|\t Fecha de un dia en concreto entre 01-01-2000 al 26-03-2021 \n"
        elif (x == 8):
            registros['hora'] = [randomHora() for x in range(config['registros'])]
            metadatos += "Hora \t|\t String \t|\t Hora de un dia enre las 00:00:00 - 23:59:59 \n"
        elif (x == 9):
            registros['soltero'] = randomSoltero(config['registros'])
            metadatos += "Soltero |\t Boolean \t|\t Determina si una persona esta soltera (True o False) \n"
    # Creacion del DataSet
    dataset = pd.DataFrame(registros)
    print(dataset)
    print('#########################################################################')

    #Exportacion al formato
    print('. . . EXPORTACION DEL FORMATO DEL DATASET 1 . . .')
    if config['formato'] == 0:
        dataset.to_csv("dataset_1.csv", index=False)
        print("Se exportó el CSV correctamente en dataset_1.csv")
    elif config['formato'] == 1:
        dataset.to_json('dataset_1.json')
        print("Se exportó el JSON correctamente en dataset_1.json")
    elif config['formato'] == 2:
        generarXML(dataset, 'dataset_1.xml')
        print("Se exportó el XML correctamente en dataset_1.xml")
    print('#########################################################################')

    #Generacion del archivo de metadatos
    print('. . . EXPORTACION DEL ARCHIVO DE METADATOS . . .')
    with open('metadatos.txt', 'w') as f:
        f.write(metadatos)
    print("Se exportaron los metadatos en metadatos.txt")
    print('#########################################################################')

    print('. . . GENERANDO DATASET CON DATOS INCORRECTOS  . . .')
    for i in config['tipos']:
        if (i == 0):
            for x in range(len(registros['nombre'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    registros['nombre'][x]= registros['nombre'][x][:-3]
        elif (i == 1):
            for x in range(len(registros['apellido'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    registros['apellido'][x]= registros['apellido'][x][:-3]
        elif (i == 2):
            for x in  range(len(registros['edad'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    aleat = np.random.randint(0, 2, size=1)#Probabilidad para alterar negativo o por 100              
                    if(aleat==0):
                        registros['edad'][x] = registros['edad'][x]*-1
                    else:
                        registros['edad'][x] = registros['edad'][x]* 100
        elif (i == 3):
            for x in range(len(registros['genero'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    registros['genero'][x] = 'N'
        elif (i == 4):
            for x in range(len(registros['correo'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    aleat = np.random.randint(3, len(registros['correo'][x]), size=1)
                    registros['correo'][x] = registros['correo'][x][:-aleat[0]]
        elif (i == 5):
            for x in range(len(registros['estatura'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    registros['estatura'][x] = registros['estatura'][x] * 3
        elif (i == 6):
            for x in range(len(registros['peso'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    registros['peso'][x] = registros['peso'][x] * 4
        elif (i == 7):
            for x in range(len(registros['fecha'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    registros['fecha'][x] = ""
        elif (i == 8):
            for x in range(len(registros['hora'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    registros['hora'][x] = ""
        elif (i == 9):
            for x in range(len(registros['soltero'])):
                aleat = np.random.randint(0, 4, size=1) #Probabilidad que se altere
                if(aleat[0]==0):
                    registros['soltero'][x] = None
    dataset2 = pd.DataFrame(registros)
    print(dataset2)
    print('#########################################################################')

    #Exportacion al formato
    print('. . . EXPORTACION DEL FORMATO DEL DATASET 1 . . .')
    if config['formato'] == 0:
        dataset2.to_csv("dataset_2.csv", index=False)
        print("Se exportó el CSV correctamente en dataset_2.csv")
    elif config['formato'] == 1:
        dataset2.to_json('dataset_2.json')
        print("Se exportó el JSON correctamente en dataset_2.json")
    elif config['formato'] == 2:
        generarXML(dataset2, 'dataset_2.xml')
        print("Se exportó el XML correctamente en dataset_2.xml")
    print('#########################################################################')