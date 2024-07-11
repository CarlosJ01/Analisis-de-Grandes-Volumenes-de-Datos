# Librerias
import pandas as pd

# Leer Archivos con los datos
def leerArchivos():
    # leer csv
    name_men = pd.read_csv('data/hombres.csv')
    name_men_list = name_men['nombre'].tolist()

    last_names = pd.read_csv('data/apellidos.csv')
    last_names_list = last_names['apellido'].tolist()

    # leer txt
    with open("data/correos.txt", "r") as archivo:
        lista_correos = list(map(str.rstrip, archivo))

    return {
        'nombres': name_men_list,
        'apellidos': last_names_list,
        'correos': lista_correos,
    }