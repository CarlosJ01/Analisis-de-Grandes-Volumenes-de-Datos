# Intalacion de librerias
Para que la practica funcione debra de instalar las siguientes librerias: <br>
    - Libreria para MongoDB <br>
        - pip install pymongo <br>
    - Libreria para Request <br>
        - pip install requests <br>
    - Libreria de BeautifulSoup <br>
        - pip install beautifulsoup4 <br>
    - Libreria de NLTK <br>
        - pip install nltk <br>
        - python -m nltk.downloader all <br>
    - Libreria para Bottle levantar un Web Services <br>
        - pip install bottle <br>
Ademas de tener instalado MongoDB, Un servidor Apache y Python 3.8.8 <br>
# Funcionamiento
Para correr el motor de busqueda debera de correr el archivo main.py en la carpeta Motor-Busqueda, esto arrancara el motor y empezara a buscar paginas<br>
 - python Motor-Busqueda\main.py<br>
Para que funcione la pagina de busqueda debera de poner la carpeta de (Paguina del Buscador) dentro de un servidor apache, y abrirlo en el navegador desde localhost.<br>
Ademas debera de correr el archivo de WS_Buscador.py para arrancar el web services y conteste las peticiones de la pagina, este es el que extrae la informacion de mogoDB<br>
 - python Motor-Busqueda\WS_Buscador.py<br>
Por ultimo solo acceda a la pagina desde local host y escriba la palabra a buscar.<br>
# Evidencias
![Evidencia](/Motor.png)
![Evidencia](/Base_de_Datos.png)
![Evidencia](/Web_Services.png)
![Evidencia](/Buscador.png)
![Evidencia](/Buscador_Paginas.png)