"""
#######################################################
Práctica 4: Verificación de un Dataset
Objetivo: Verificar el contenido y la integridad de un Dataset

Equipo 5
    Castro Cazares Carlos Jahir (Responsable)
    Martinez Resendiz Giovanni Hasid
    Velazquez Aguilar Jaime Isai
#######################################################
Instalar Pandas
    -pip install pandas
"""
# Librerias
import csv
import pandas as pd
from validaciones import validarBooleano, validarSueldo, validarId, validarFecha, validarNombreCompleto

# Metodo Main
if __name__ == '__main__':
    # Leyendo el archivo csv dañado
    print("Leyendo el archivo . . .")
    with open('dataset_005/datasetErrores.csv', encoding='UTF8', newline='') as File:
        dataset = csv.reader(File)
        registros = []
        for registro in dataset:
            registros.append(registro)
        print("Archivo leido ("+str(len(registros))+" registros leidos)")
        print("###############################################################")
        print("\x1b[0;31m" + "El dataset no tiene los encabezados de los datos")
        print("\033[0m"+"###############################################################")

    # Analizando el dataset
    datasetCorregido = []
    ids = []
    print("Analizando el dataset . . .")
    for i in range(len(registros)):
        registro = registros[i]
        if len(registro) == 5:
            # Variable para saber si ingresara al nuevo dataset
            ingresar = True

            # Prueba para el nombre
            if not validarNombreCompleto(registro[0]):
                ingresar = False
                print("\x1b[0;33m" + "El registro #" + str(i + 1) + " su valor para el campo nombres no tiene el formato adecuado")

            # Prueba para validar la fecha
            if not validarFecha(registro[1]):
                ingresar = False
                print("\x1b[0;33m" + "El registro #" + str(i + 1) + " su valor para el campo fecha no tiene el formato adecuado")

            # Prueba para el id
            if registro[2] in ids:
                ingresar = False
                print("\x1b[0;33m" + "El registro #" + str(i + 1) + " esta repetido")
            else:
                if not validarId(registro[2]):
                    ingresar = False
                    print("\x1b[0;33m" + "El registro #" + str(i + 1) + " su valor para el campo id es negativo")

            # Prueba para el registro de sueldo
            if not validarSueldo(registro[3]):
                ingresar = False
                print("\x1b[0;33m" + "El registro #" + str(i + 1) + " su valor para el campo salario es negativo")
            else:
                registro[3] = round(float(registro[3]), 2)

            # Prueba del registro booleano
            if not validarBooleano(registro[4]):
                ingresar = False
                print("\x1b[0;33m" + "El registro #"+str(i+1)+" su valor para el campo casado no es booleano")

            # Ingresar al nuevo dataset
            if ingresar:
                print(registro)
                datasetCorregido.append(registro)
                ids.append(registro[2])
        else:
            print("\x1b[0;31m" + "El registro #"+str(i+1)+" tiene mas de 5 campos")
        print("\033[0m")

    # Crear el nuevo dataset corregido
    print("###############################################################")
    print("\x1b[0;32m" + "Numero de registros despues de la verificacion "+str(len(datasetCorregido)))
    print("\033[0m")
    registros = {}
    registros['id'] = [x[2] for x in datasetCorregido]
    registros['nombres'] = [x[0] for x in datasetCorregido]
    registros['fechaNac'] = [x[1] for x in datasetCorregido]
    registros['sueldos'] = [x[3] for x in datasetCorregido]
    registros['casado'] = [x[4] for x in datasetCorregido]
    datasetNuevo = pd.DataFrame(registros)
    print(datasetNuevo)
    datasetNuevo.to_csv("dataset_corregido.csv", index=False, encoding='UTF8')
    print("\x1b[0;32m" + "El dataset corregido se guardo en dataset_corregido.csv")
    print("\033[0m")
