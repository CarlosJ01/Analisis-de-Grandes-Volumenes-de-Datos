import requests
from bs4 import BeautifulSoup

# Llamnado al metodo
from limpieza import depurar

def extraccion(direccion):
    try:
        pagina = requests.get(direccion)
        html = BeautifulSoup(pagina.content, 'html.parser')
        conexion = True
    except:
        print('No puede conectarse a la página ' + str(direccion))
        conexion = False

    if conexion:
        arr = []
        # ------------------Titulo--------------------
        titulo = html.find('title')
        if (titulo != None):
            titulo = titulo.text
        else:
            titulo = ""
        arr.append(titulo)
        # ------------------METAS--------------------
        # Keyword
        keyword = html.find("meta", {"name": "keywords"})
        if (keyword != None):
            keyword = keyword.get('content')
        else:
            keyword = ""
        arr.append(keyword)
        # -------------- Get descripcion ----------------
        descripcion = html.find("meta", {"name": "description"})
        if (descripcion != None):
            descripcion = descripcion.get('content')
        else:
            descripcion = ""
        arr.append(descripcion)

        # ----------- Get texto ---------------------
        textos = html.find_all('p')
        cadena = ""
        for t in textos:
            cadena = cadena + " " + t.text
        # -------------- Get palabras -------------
        elementos = depurar(cadena)
        palabras = []
        if (len(elementos) < 3):
            indice = 3 - len(elementos)
            for elemento in elementos:
                palabras.append(elemento)
            for i in range(indice):
                palabras.append(['', 0])
        else:
            for elemento in elementos:
                palabras.append(elemento)
        arr.append(palabras)
        # --------------- Get enlaces ---------------
        links = []
        urls = html.find_all('a')
        for url in urls:
            try:
                link = str(url.get('href'))
                if (link.find('https://') == 0 or link.find('http://') == 0):
                    links.append(url.get('href'))
            except:
                pass
        arr.append(links)
        return arr
    else:
        return []