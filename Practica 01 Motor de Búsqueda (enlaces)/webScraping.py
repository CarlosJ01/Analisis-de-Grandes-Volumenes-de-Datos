import requests
from bs4 import BeautifulSoup

#Extraer la informacion de webscraping
def getLinks(direccion):
    try:
        pagina = requests.get(direccion)
        html = BeautifulSoup(pagina.content, 'html.parser')
        conexion = True
    except:
        print('No puede conectarse a la página ' + str(direccion))
        conexion = False

    if conexion:
        links=[]
        urls = html.find_all('a')
        for url in urls:
            try:
                link = str(url.get('href'))
                if (link.find('https://') == 0 or link.find('http://') == 0):
                    links.append(url.get('href'))
            except:
                pass
        return links
    else:
        return []