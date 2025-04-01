import requests
from bs4 import BeautifulSoup

#enviar solicitud get
url='https://repositorio.ues.edu.sv/items/012f5eb8-59b5-4006-a138-5652d03baa58'

try:
    response=requests.get(url)
except:
    print('Error al enviar solicitud')
else:
    if response.status_code==200:
        print('Contenido de la solicitud es:')
        #parsea el contenido de HTML usando HTML parser
        soup=BeautifulSoup(response.content,'html.parser')
        #imprime el contenido de la solicitud
        print(soup.prettify())
        title=soup.find_all('title')
        print(title)
        #Buscar todoslos elementos <a> en el documento
        links=soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        print('Error en la solicitud',response.status_code)
