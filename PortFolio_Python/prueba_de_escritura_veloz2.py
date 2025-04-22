from tkinter import * 
from tkinter import messagebox
import timeit
import random
import re

#configuramos la raiz de laventana principal
raiz=Tk()
raiz.config(width=700,height=700,relief='groove',bd=5)
raiz.title('Prueba de Escritura Veloz')
raiz.resizable(False,False) #permanezca en su tamaño inicial


#activamos ingreso_texto donde se escribe
def activar_text():
    ingreso_texto.config(state='normal')

#activamos la etiqueta donde se mostrara la frase
def activar_etiqueta2():
    etiqueta2.config(state='normal')

#todas las funciones que se activaran al hacer click del boton_inicio
def acciones():
    iniciar_escritura()
    activar_text()
    activar_etiqueta2()
    
#aqui generamos las frases que basicamente son un conjunto de palabras que terminan en punto
def frase_aleatoria():
    file=open(r'E:\PythonAvanzado\tkinter\articulo.txt',encoding='utf-8')
    contenido=file.read().split('.')
    oracion_rand=random.choice(contenido).strip()
    return oracion_rand

def fun_coincidencia():
    #limpiamos el texto random
    oracion=texto
    oracion_limpia=re.sub(r'[^\w\s]', '', oracion)
    lista_palabras=oracion_limpia.split(' ')
    num_lista_palabras=len(lista_palabras)
    #limpiamos el texto  ingresado
    conten_limpio=re.sub(r'[^\w\s]', '', conten)
    conten_lista=conten_limpio.split(' ')
    num_conten_lista=len(conten_lista)
    #hallar las coincidencias para no solo evaluar la velocidad 
    #sino lo escrito sea lo mas exacto al texto random 
    coincidencias=0
    i=0
    while i < len(conten_lista):
        if conten_lista[i] in lista_palabras:
            lista_palabras.remove(conten_lista[i]) # Elimina de la lista_palabras para que no se repita
            conten_lista.pop(i)  # Elimina de la conten_lista y no incrementa el índice
            coincidencias += 1
        else:
            i += 1 #solo incrementa el indice sino encuentra coincidencia  
                   
    coincidencia=(coincidencias/num_lista_palabras)*100
    return coincidencia

#mensaje de error al no escribir nada y pretender tomar tiempo
def mensaje_error():    
    messagebox.showerror('Mensaje de Error','No existe texto no podemos medir')

#se activa cuando se escribio el texto
def mensaje_final(intervalo_time):
    num_coinc=fun_coincidencia()  
    messagebox.showinfo('Tiempo de escritura',f'Tomo {intervalo_time:.5} segundos y una coincidencia del {num_coinc:.4} porciento')

#validamos el texto ingresado
def validar_texto(ingreso_texto):
    global conten
    
    conten=ingreso_texto.get("1.0",'end-1c')
    if conten=='':
        mensaje=mensaje_error()
    else:
        mensaje=mensaje_final(intervalo_time)
    return mensaje

#estructura principal de la interfaz de usuario
#configuracion de botones y etiquetas
def start_GUI():
    global ingreso_texto,boton_terminar,boton_inicio,etiqueta2
            
    etiqueta1=Label(raiz,text='Ingrese el Texto Aleatorio:',font=('Helvetica',10))
    etiqueta1.pack()
        
    ingreso_texto=Text(raiz,width=40,height=20,relief='solid',bd=4,bg='white',state='disabled')
    ingreso_texto.pack()
    
    boton_terminar=Button(raiz,text='Terminar texto',state='disabled',command=terminar_medicion)
    boton_terminar.pack()
           
    boton_inicio=Button(raiz,text='Frase Aleatoria ',command=acciones)
    boton_inicio.pack()
    
    etiqueta2=Label(raiz,text='',wraplength=400,state='disabled')
    etiqueta2.pack()

#inicializamos variables
tiempo=0
start_time=float

#funcion para iniciar escritura
def iniciar_escritura():
    global texto
    global start_time
    
    
    texto=frase_aleatoria()
    etiqueta2.config(text='Frase: '+texto)
    ingreso_texto.delete(1.0,END)
    boton_inicio.config(state='disabled')
    boton_terminar.config(state='normal')
    start_time=timeit.default_timer()

intervalo_time=0
num_coinc=float
#Funcion para terminar escritura
#calcular el intervalo de tiempo hasta pulsar el boton terminar
def terminar_medicion():
    global intervalo_time,num_coinc
    
    intervalo_time=timeit.default_timer()-start_time
    boton_inicio.config(state='normal')
    boton_terminar.config(state='disabled')
    validar_texto(ingreso_texto)
    
#Funcion Principal llamamos a la interfaz de usuario.    
start_GUI()

raiz.mainloop()