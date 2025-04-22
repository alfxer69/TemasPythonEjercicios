from gtts import gTTS
import os

archivo=open(r'E:\PythonAvanzado\Pandas\nltk\portfolio\articulo.txt','r',encoding='utf=8').read().replace('\n',' ')
lenguaje='es'
oracion=gTTS(archivo,lang=lenguaje,slow=True)
oracion.save('texto_articulo.mp3')
os.system('start texto_articulo.mp3')