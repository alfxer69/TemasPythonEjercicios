import tkinter as tk 
from langdetect import detect


raiz=tk.Tk()
raiz.config(width=200,height=100,relief='solid',bd=5)
raiz.title('Detector de Idioma')


def detector_lenguaje():
    texto=str(entrada_texto.get())
    print(texto)
    try:
        idioma=detect(texto)
        etiqueta_respuesta.config(text=f'El idioma del texto es: {idioma}')
    except:
        etiqueta_respuesta.config(text='No se pudo detectar idioma')

etiqueta=tk.Label(text='Ingrese una frase para detectar su idioma: ',font=('Arial',11))
etiqueta.pack(pady=10)

entrada_texto=tk.Entry(raiz,width=60,relief='ridge',bd=5,background='white')
entrada_texto.pack(pady=10)

boton_detector=tk.Button(raiz,text='Detectar Idioma',font=('Arial',10),command=detector_lenguaje)
boton_detector.pack(pady=10)

etiqueta_respuesta=tk.Label(text=f'',font=('Arial',12))
etiqueta_respuesta.pack(pady=15)



raiz.mainloop()



