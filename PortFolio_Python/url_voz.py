from urllib.request import urlopen 
import urllib.request #peticiones a una url
import re 
from inscriptis import get_text
import nltk
from nltk import sent_tokenize,word_tokenize
import heapq
from gtts import gTTS
import os

nltk.download('punkt') #divide el texto en frases (tokenizacion)
nltk.download('stopwords') #palabras sin significado solo conectores

from nltk.corpus import stopwords

#comenzamos a abrir y escrapear la pagina
pagina = (r'https://www.manosunidas.org/observatorio/cambio-climatico/calentamiento-global')
html=urllib.request.urlopen(pagina).read().decode('utf-8')
text=get_text(html)
articulo_text=text

#limpiando el texto de caracteres especiales
articulo_text=re.sub(r'\[[0-9]*\]',' ',articulo_text)
articulo_text=re.sub(r'\s+',' ',articulo_text)

formato_articulo_text=re.sub(r'[^]a-zA-Z0-9áéíóú.,;[:-¿?ñ]',' ',articulo_text)
formato_articulo_text=re.sub(r'\s+',' ',formato_articulo_text)

#formamos la lista de oraciones
lista_palabras=sent_tokenize(formato_articulo_text,language='spanish')

#inicializamos los stopword de nltk 
stop_words=nltk.corpus.stopwords.words('spanish')

#formamos un diccionario con la frecuencia de las palabras
frecuencia_palabras={}

#comenzamos a iterar oracion por oracion
for oracion in lista_palabras:
    #recorremos palabra por palabra
    palabras=word_tokenize(oracion,language='spanish')
    for palabra in palabras:
        if palabra not in stop_words:
            if palabra not in frecuencia_palabras.keys():
                frecuencia_palabras[palabra]=1 #si no esta en el diccionario
            else:
                frecuencia_palabras[palabra]+=1 #si esta en el diccionario

#Verificacmos la frecuencia maxima dentro del diccionario frecuencia_palabras 
maxima_frecuencia=max(frecuencia_palabras.values())

#hallamos el puntaje por cada palabra dentro de la oracion
for palabra in frecuencia_palabras.keys():
    frecuencia_palabras[palabra]=frecuencia_palabras[palabra]/maxima_frecuencia

#calcular puntajes de las oraciones
puntaje_oracion={}

for oracion in lista_palabras:
    for palabra in word_tokenize(oracion,language='spanish'):
        if palabra in frecuencia_palabras.keys():
            if oracion not in puntaje_oracion.keys():
                puntaje_oracion[oracion]=frecuencia_palabras[palabra]
            else:
                puntaje_oracion[oracion]+=frecuencia_palabras[palabra]

#seleccionamos las mejores oraciones
oracion_resumen=heapq.nlargest(10,puntaje_oracion,key=puntaje_oracion.get)

#imprimir resumen
resumen=' '.join(oracion_resumen)
print(resumen)

#Creando un archivo txt para guardarlo
archivo=open('resumen.txt','w',encoding='utf-8')
archivo.write(resumen)
archivo.close()

#convirtiendo a un archivo de el resumen
with open('resumen.txt','r',encoding='utf-8') as archivo:
    texto=archivo.read()

#Generamos el archivo y el audio
audio=gTTS(texto,lang='es',slow=False)
audio.save('resumen.mp3')
os.system('start resumen.mp3')