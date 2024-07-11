# Proyecto Final AGVD (MACAVE STADISTIC)
# Equipo 5
#   Castro Cazares Carlos Jahir (Responsable)
#   Martinez Resendiz Giovanni Hasid
#   Velazquez Aguilar Jaime Isai

# Almacenamiento de datos a partir del dataset

from conexionDB import cleanTable, insertEquipos, insertPartidos

#Extraccion y almacenamiento de los equipos
def equipos():
    f = open("dataset/equipos.csv", "r")
    cont=0
    for linea in f:
        if(cont>0):
            arr = linea.split(",")
            id = arr[0]
            equipo = arr[1]
            grupo = arr[2]
            logo = "images"+(arr[3])[0:-1]

            #Insertar datos a la base de datos
            insertEquipos((id, equipo, grupo, logo))
        cont+=1
    f.close()

#Extraccion y almacenamiento de los partidos
def partidos():
    f = open("dataset/partidos.csv", "r")
    cont=0
    for linea in f:
        if(cont>0):
            arr = linea.split(",")
            id = arr[0]
            equipo1 = arr[1]
            goles1 = arr[2]
            equipo2 = arr[3]
            goles2 = arr[4]
            tipo = arr[5]
            dia = arr[6]
            jugado = arr[7]

            #Insertar datos a la base de datos
            insertPartidos((id, equipo1, goles1, equipo2, goles2, tipo, dia, jugado))
        cont+=1
    f.close()
 

if __name__=="__main__":
    #Clean    
    print("Limpiando los datos")
    cleanTable()

    #Almacenamiento de los equipos
    print("Insertando los equipos de la temporada")
    equipos()
    
    #Almacenamiento de los partidos
    print("Insertando datos de los partidos")
    partidos()

    print("Terminado")
