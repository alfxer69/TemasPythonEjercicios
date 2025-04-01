import requests
from bs4 import BeautifulSoup

#enviar solicitud get
url='https://www.bbc.com/mundo/articles/czxk0wqe931o'
try:
    #respuesta de la solicitud
    response=requests.get(url)
except:
    print('Error al abrir la pagina')
else:
    #comparamos con la respuesta del servidor
    if response.status_code==200:
        print('')
        soup=BeautifulSoup(response.content,'html.parser')
        first_link=soup.find('a')
        print(first_link.text)
        parent=first_link.parent
        print('Acceder al padre de un elemento: ')
        print(parent.name)
        print('')
        #iterar sobre los hijos de un elemento
        print('Iterar sobre los hijos de un elemento: ')
        for child in parent.children:
            print(child.name)
        #acceder al siguiente y anterior hermano de un elemento
        print('')   
        print('Acceder al siguiente hermano de un elemento: ')
        next_sibling=first_link.next_sibling
        print(next_sibling) 
        print('')
        print('Acceder al hermano anterior de un elemento: ')
        previous_sibling=first_link.previous_sibling
        print(previous_sibling)
        print('')
        print('Impresion del texto first_link:')
        print(first_link.text)
    else:
        print('error en a solicitud',response.status_code)