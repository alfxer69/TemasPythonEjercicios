import requests
from bs4 import BeautifulSoup  

#enviar solicitud get
url='https://repositorio.ues.edu.sv/items/012f5eb8-59b5-4006-a138-5652d03baa58'
try:
    response=requests.get(url)
except:
    print('Error al abrir la pagina')
else:
    if response.status_code==200:
        print('')
        print('Contenido de la solicitud del primer link: ')
        #supongamos que deseamos extraer el href del primer enlace
        soup=BeautifulSoup(response.content,'html.parser')
        first_link=soup.find('a')
        href=first_link['href']
        print(href)
        #Tambien existe el metodo get que es seguro si elatributono existe
        href=first_link.get('href')
        print()
        print('Contenido de la solicitud del primer link con get: ')
        print(href)
    else:
        print('error en a solicitud',response.status_code)
        
        