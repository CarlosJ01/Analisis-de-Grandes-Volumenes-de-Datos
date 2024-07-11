# Conecciones con la base de datos para CRUD

import mysql.connector

conexion = {
    'host': "localhost",
    'usuario': "root",
    'password': "",
    'basedatos': "macave",
    'puerto': 3307
}

#Limpieza database
def cleanTable():
    mydb = mysql.connector.connect(
        host=conexion['host'],
        user=conexion['usuario'],
        password=conexion['password'],
        database=conexion['basedatos'],
        port=conexion['puerto']
    )
    cursor = mydb.cursor()

    sql = "DELETE FROM partidos WHERE id > 0"
    cursor.execute(sql)
    mydb.commit()

    sql = "DELETE FROM equipos WHERE id > 0"
    cursor.execute(sql)
    mydb.commit()

    cursor.close()

# Insertar equipos en la base de datos
def insertEquipos(input):
    mydb = mysql.connector.connect(
        host=conexion['host'],
        user=conexion['usuario'],
        password=conexion['password'],
        database=conexion['basedatos'],
        port=conexion['puerto']
    )
    cursor = mydb.cursor()
    sql = "INSERT INTO equipos (id, nombre, grupo, logo) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, input)
    mydb.commit()
    cursor.close()

# Insertar partidos
def insertPartidos(input):
    mydb = mysql.connector.connect(
        host=conexion['host'],
        user=conexion['usuario'],
        password=conexion['password'],
        database=conexion['basedatos'],
        port=conexion['puerto']
    )
    cursor = mydb.cursor()
    sql = "INSERT INTO partidos (id, id_equipo_1, goles_1, id_equipo_2, goles_2, tipo, dia, jugado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, input)
    mydb.commit()
    cursor.close()

# Partidos Jugados
def getPartidosJugados():
    mydb = mysql.connector.connect(
        host=conexion['host'],
        user=conexion['usuario'],
        password=conexion['password'],
        database=conexion['basedatos'],
        port=conexion['puerto']
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM partidos WHERE jugado = 1")
    return cursor.fetchall()

# Partidos Proximos
def getPartidosProximos():
    mydb = mysql.connector.connect(
        host=conexion['host'],
        user=conexion['usuario'],
        password=conexion['password'],
        database=conexion['basedatos'],
        port=conexion['puerto']
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM partidos WHERE jugado = 0")
    return cursor.fetchall()

# Get Informacion Equipo
def getInformacionEquipo(id):
    mydb = mysql.connector.connect(
        host=conexion['host'],
        user=conexion['usuario'],
        password=conexion['password'],
        database=conexion['basedatos'],
        port=conexion['puerto']
    )
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM equipos WHERE id = {id}")
    return cursor.fetchall()