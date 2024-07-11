"""
    Práctica 7: Redes Bayesianas
    Objetivo: Predecir eventos utilizando Redes Bayesianas
    ######################################################
    Equipo 5
        Castro Cazares Carlos Jahir (Responsable)
        Martinez Resendiz Giovanni Hasid
        Velazquez Aguilar Jaime Isai
    ######################################################
    Python 3.8.8
    pandas => pip install pandas
"""
import pandas as pd

# Ruta del archivo CSV
rutaArchivo = "dataset/210518COVID19MEXICO.csv"

# Main
if __name__ == '__main__':
    # Leer CSV y extraer el numero de pacientes
    print("Leyendo el dataset de covid 19 . . .")
    datasetCovid = pd.read_csv(rutaArchivo)
    numeroPersonas = len(datasetCovid.index)
    print(datasetCovid)
    print("Existen "+str(numeroPersonas)+" personas en el dataset")

    # Extrayendo muertes por Covid-19 y probabilidad
    print("\nBuscando muertes por Covid . . .")
    muertesCovid = datasetCovid[datasetCovid['FECHA_DEF'] != '9999-99-99']
    numeroMuertos = len(muertesCovid.index)
    pMuerte = round(numeroMuertos / numeroPersonas, 4)  # Pacientes muertos / Total personas

    # Extrayendo probabilidad de morir con asma
    print("\nBuscando probabilidad de morir si tienes asma . . .")
    pMuertosAsma = round(len(muertesCovid[muertesCovid['ASMA'] == 1].index) / numeroMuertos, 4)  # Muertos con asma / Total de muertos
    pAsma = round(len(datasetCovid[datasetCovid['ASMA'] == 1].index) / numeroPersonas, 4) # Personas con asma / Total de personas
    pMuerteCovidAsma = round((pMuertosAsma * pMuerte) / pAsma, 4)  # Muertos con asma * Personas con asma / Total muertos

    # Extrayendo probabilidad de morir con hipertencion
    print("\nBuscando probabilidad de morir si tienes hipertencion . . .")
    pMuertosHiper = round(len(muertesCovid[muertesCovid['HIPERTENSION'] == 1].index) / len(muertesCovid.index), 4) # Muertos con hipertencion / Total de muertos
    pHiper = round(len(datasetCovid[datasetCovid['HIPERTENSION'] == 1].index) / numeroPersonas, 4) # Personas con hipertencion / Total de personas
    pMuerteCovidHiper = round((pMuertosHiper * pMuerte) / pHiper, 4)  # Muertos con hipertension * Personas con hipertension / Total muertos

    # Extrayendo probabilidad de morir con tabaquismo
    print("\nBuscando probabilidad de morir si tienes tabaquismo . . .")
    pMuertosTabaq = round(len(muertesCovid[muertesCovid['TABAQUISMO'] == 1].index) / len(muertesCovid.index), 4)  # Muertos con tabaquismo / Total de muertos
    pTabaq = round(len(datasetCovid[datasetCovid['TABAQUISMO'] == 1].index) / numeroPersonas, 4) # Personas con tabaquismo / Total de personas
    pMuerteCovidTabaq = round((pMuertosTabaq * pMuerte) / pTabaq, 4)  # Muertos con tabaquismo * Personas con tabaquismo / Total muertos

    print('\n#############################################################################################################')
    print('¿Cuál es la probabilidad de morir de COVID-19? => ' + str(pMuerte) + ' (' + str(round(pMuerte * 100, 2)) + '%)')
    print('¿Cuál es la probabilidad de morir de COVID-19 dado que tiene asma? => ' + str(pMuerteCovidAsma) + ' (' + str(round(pMuerteCovidAsma * 100, 2)) + '%)')
    print('¿Cuál es la probabilidad de morir de COVID-19 dado que tiene hipertensión? => ' + str(pMuerteCovidHiper) + ' (' + str(round(pMuerteCovidHiper * 100, 2)) + '%)')
    print('¿Cuál es la probabilidad de morir de COVID-19 dado que tiene tabaquismo? => ' + str(pMuerteCovidTabaq) + ' (' + str(round(pMuerteCovidTabaq * 100, 2)) + '%)')

    # Calculando el mas mortal
    maximo = (max([pMuerteCovidAsma, pMuerteCovidHiper, pMuerteCovidTabaq]))
    print('¿Cuál de los 3 enfermedades anteriores (asma, hipertensión y tabaquismo) resulta más mortal? => ', end="")
    if maximo == pMuerteCovidAsma:
        print("ASMA")
    elif maximo == pMuerteCovidHiper:
        print('HIPERTENSION')
    elif maximo == pMuerteCovidTabaq:
        print('TABAQUISMO')