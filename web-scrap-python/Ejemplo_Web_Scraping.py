import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url='https://elpais.com/ciencia/2024-11-29/la-ingeniosa-tecnica-de-moctezuma-y-su-banda-de-orcas-para-cazar-tiburones-ballena-en-mexico.html'

try:
    response=requests.get(url)
except:
    print('Error al abrir la pagina')
#parsemos el HTML con BeautifulSoup y lo guardamos en un variable soup
soup=BeautifulSoup(response.text,'html.parser')
#print(soup)

#buscamos el <div> correspondiente y sacamos su contenido:
content=soup.find('div',{'data-dtm-region':'articulo_cuerpo'})
#print(content.text)

article=[]
#itermos el contenido de content y lo ingresamos a una lista
for i in content.find_all('p'):
    article.append(i.text)
#impresion de los parrafos del articulo
#print('\n'.join(article))

#imprimimos los enlaces dentro de la pagina
content=soup.find('div',{'data-dtm-region':'articulo_cuerpo'})
links=content.find_all('a')
#imprimir los enlaces
for link in links:
    print(f'Texto: {link.text},Href: {link["href"]}')

