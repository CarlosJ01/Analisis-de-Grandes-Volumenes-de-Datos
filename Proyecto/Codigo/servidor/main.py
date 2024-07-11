# Proyecto Final AGVD (MACAVE STADISTIC)
# Equipo 5
#   Castro Cazares Carlos Jahir (Responsable)
#   Martinez Resendiz Giovanni Hasid
#   Velazquez Aguilar Jaime Isai

# Algoritmo para el procesamiento de datos y resultados estadisticos y probabilidades

#Librerias
import numpy as np
import bottle
from bottle import route, run, template
from bottle import response

# Conexion con base de datos
from conexionDB import getPartidosJugados, getPartidosProximos, getInformacionEquipo

#Variable global
app = bottle.app()

def probabilidadPoisson(k, lambd):
    return (lambd ** k * np.exp(-lambd)) / np.math.factorial(k)

#CORS
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            return fn(*args, **kwargs)
    return _enable_cors

@app.route('/', method=['GET'])
def index():
    return '<h1>Bienvenido a MACAVE Stadistics</h1> <br>http://127.0.0.1:8080/datos => Este es la url con los datos de prediccion'

@route('/datos')
@enable_cors
def consulta_info():
    response.headers['Content-type'] = 'application/json'
    # Get todos los partidos
    partidos = getPartidosJugados()

    # Get los partidos que no han sido jugados
    proximos = getPartidosProximos()

    # Pronosticar (Estadistica y Probabilidad)
    data = {}
    for proximo in proximos:
        # Jugadores
        equipo1 = {
            'id': proximo[1], # Id del equipo
            'ataque': 0, # Media de goles
            'defensa': 0, # Media de encajes
            'exito': 0, # Tasa promedio de Exito
            'probabilidades': [0, 0, 0, 0, 0, 0] # Probabilidad de anotar de 0 - 5 Goles
        }
        equipo2 = {
            'id': proximo[3],
            'ataque': 0,
            'defensa': 0,
            'exito': 0,
            'probabilidades': [0, 0, 0, 0, 0, 0]
        }

        # Calcular estadisticas de cada equipo (Medias)
        totalGoles = 0

        for partido in partidos:
            # Total de goles de la copa
            totalGoles += partido[2] + partido[4]

            # Total de goles anotados y encajados por equipo 1
            if partido[1] == equipo1['id']:
                equipo1['ataque'] += partido[2]
                equipo1['defensa'] += partido[4]
            if partido[3] == equipo1['id']:
                equipo1['ataque'] += partido[4]
                equipo1['defensa'] += partido[2]

            # Total de goles anotados y encajados por equipo 2
            if partido[1] == equipo2['id']:
                equipo2['ataque'] += partido[2]
                equipo2['defensa'] += partido[4]
            if partido[3] == equipo2['id']:
                equipo2['ataque'] += partido[4]
                equipo2['defensa'] += partido[2]

        # Calculo de medias de anotaciones(ataque) y encajaciones(defensa) por equipo y media de goles de la copa
        totalPartidos = len(partidos)
        mediaGoles = totalGoles / totalPartidos
        equipo1['ataque'] /= totalPartidos
        equipo1['defensa'] /= totalPartidos

        equipo2['ataque'] /= totalPartidos
        equipo2['defensa'] /= totalPartidos

        # Tasa promedio de exito
        equipo1['exito'] = equipo1['ataque'] * equipo2['defensa'] * mediaGoles
        equipo2['exito'] = equipo2['ataque'] * equipo1['defensa'] * mediaGoles

        # Probabilidad de anotar de 0-5 Goles con Distribucion Poisson
        for k in range(len(equipo1['probabilidades'])):
            equipo1['probabilidades'][k] = probabilidadPoisson(k, equipo1['exito'])
            equipo2['probabilidades'][k] = probabilidadPoisson(k, equipo2['exito'])

        # Convinacion de probabilidades
        probabilidades = []
        for probabilidadE1 in equipo1['probabilidades']:
            probabilidadN = []
            for probabilidadE2 in equipo2['probabilidades']:
                probabilidadN.append(round((probabilidadE1 * probabilidadE2)*100, 2))
            probabilidades.append(probabilidadN)

        # Formato de datos para su envio
        equipo1['ataque'] = round(equipo1['ataque'], 2)
        equipo1['defensa'] = round(equipo1['defensa'], 2)
        equipo1['exito'] = round(equipo1['exito'], 2)
        equipo1['probabilidades'] = [round((p*100), 2) for p in equipo1['probabilidades']]

        equipo2['ataque'] = round(equipo2['ataque'], 2)
        equipo2['defensa'] = round(equipo2['defensa'], 2)
        equipo2['exito'] = round(equipo2['exito'], 2)
        equipo2['probabilidades'] = [round((p * 100), 2) for p in equipo2['probabilidades']]

        infoEquipo1 = getInformacionEquipo(equipo1['id'])[0]
        infoEquipo2 = getInformacionEquipo(equipo2['id'])[0]

        tipo = ''
        if (proximo[5] == 'J1'):
            tipo = 'Jornada 1'
        elif (proximo[5] == 'J2'):
            tipo = 'Jornada 2'
        elif (proximo[5] == 'J3'):
            tipo = 'Jornada 3'
        elif (proximo[5] == 'OF'):
            tipo = 'Octavos de Final'
        elif (proximo[5] == 'CF'):
            tipo = 'Cuartos de Final'
        elif (proximo[5] == 'SF'):
            tipo = 'Semifinal'
        elif (proximo[5] == 'F'):
            tipo = 'Final'

        partido = {
            'id': proximo[0],
            'equipo1': infoEquipo1[1],
            'logo1': infoEquipo1[3],
            'equipo2': infoEquipo2[1],
            'logo2': infoEquipo2[3],
            'tipo': tipo,
            'fecha': proximo[6].strftime('%d/%m/%Y')
        }

        data={
            'partido': partido,
            'marcadores': probabilidades,
            'equipo1': equipo1,
            'equipo2': equipo2
        }
        
    print(data)
    return data
    
if __name__=="__main__":
    app.run(port=8080)


