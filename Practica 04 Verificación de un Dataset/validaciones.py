from datetime import datetime
# Validacion para el nombre
def validarNombreCompleto (nombre):
    try:
        nombre = nombre.replace(' ', '')
        nombre = nombre.replace('.', '')
        if nombre.isalpha():
            return True
        return False
    except ValueError:
        return False

# Validacion para fecha
def validarFecha(fecha):
    try:
        datetime.strptime(fecha, "%d %B %Y")
        return True
    except ValueError:
        return False

# Validacion para id
def validarId(id):
    try:
        if int(id) < 0:
            return False
        return True
    except ValueError:
        return False

# Validacion para sueldos
def validarSueldo(salario):
    try:
        if float(salario) <= 0:
            return False
        return True
    except ValueError:
        return False

# Validacion para valor booleano
def validarBooleano(registro):
    if registro != 'True' and registro != 'False':
        return False
    return True