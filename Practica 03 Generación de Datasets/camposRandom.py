# Librerias
import numpy as np
import random
from datetime import datetime

def randomNombre(nombres):
    name = np.random.choice(nombres)
    return (name.split(' ')[0].capitalize())

def randomApellido(listaApellidos):
    apellido = np.random.choice(listaApellidos)
    return (apellido.split(' ')[0].capitalize())

def randomEdad(n):
    return np.random.randint(18, 120, size=n)

def randomGenero(n):
    return np.random.choice(['H', 'M'], size=n)

def randomCorreo(listaCorreos):
    return np.random.choice(listaCorreos)

def randomEstatura(n):
    return np.around(np.random.uniform(1.5, 2, size=n), 2)

def randomPeso(n):
    return np.around(np.random.uniform(50, 150, size=n), 2)

def randomFecha():
    return (datetime(2000, 1, 1) + (datetime(2021, 3, 27) - datetime(2000, 1, 1)) * random.random()).date()

def randomHora():
    return (datetime(2021, 3, 26) + (datetime(2021, 3, 27) - datetime(2021, 3, 26)) * random.random()).time()

def randomSoltero(n):
    return np.random.choice([True, False], size=n)