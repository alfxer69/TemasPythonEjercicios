import tkinter as tk 
from tkinter import messagebox,ttk
from time import strftime
import webbrowser
import random

raiz=tk.Tk()
raiz.config(width=500,height=200,relief='sunken',bd=5,background='lightgray')
raiz.title('Reloj con Alarma')

lista_horas=[]
lista_minutos=[]
lista_segundos=[]

for i in range(0,24):
    lista_horas.append(i)

for i in range(0,60):
    lista_minutos.append(i)
    
for i in range(0,60):
    lista_segundos.append(i)

texto1=tk.Label(raiz,text='Hora',bg='lightgray',fg='black',font=('Arial',12,'bold'))
texto1.grid(row=1,column=0,padx=5,pady=5)
texto2=tk.Label(raiz,text='Minuto',bg='lightgray',fg='black',font=('Arial',12,'bold'))
texto2.grid(row=1,column=1,padx=5,pady=5)
texto3=tk.Label(raiz,text='Segundo',bg='lightgray',fg='black',font=('Arial',12,'bold'))
texto3.grid(row=1,column=2,padx=5,pady=5)

combobox1=ttk.Combobox(raiz,values=lista_horas,justify='center',width='12',font='Arial')
combobox1.grid(row=2,column=0,padx=5,pady=5)
combobox1.current(0)
combobox2=ttk.Combobox(raiz,values=lista_minutos,justify='center',width='12',font='Arial')
combobox2.grid(row=2,column=1,padx=5,pady=5)
combobox2.current(0)
combobox3=ttk.Combobox(raiz,values=lista_segundos,justify='center',width='12',font='Arial')
combobox3.grid(row=2,column=2,padx=5,pady=5)
combobox3.current(0)

alarma=tk.Label(raiz,fg='violet',bg='black',font=('Radioland',20))
alarma.grid(column=0,row=3,sticky='nsew',ipadx=5,ipady=5)


def obtener_tiempo():
    
    x_hora=combobox1.get()
    x_minuto=combobox2.get()
    x_segundo=combobox3.get()
    
    hora=strftime('%H')
    minuto=strftime('%M')
    segundo=strftime('%S')
    
    hora_total=(hora+' : '+minuto+' : '+segundo)
    texto_hora.config(text=hora_total,font=('Radioland',25))
    
    hora_alarma=x_hora+' : '+x_minuto+' : '+x_segundo
    alarma['text']=hora_alarma
    
    if int(hora)==int(x_hora) and int(minuto)==int(x_minuto) and int(segundo)==int(x_segundo):
        abrir_youtube()
    
    texto_hora.after(500,obtener_tiempo)

def abrir_youtube():
    try:
        with open(r'E:\PythonAvanzado\Pandas\nltk\portfolio\paginas_youtube.txt','r') as archivo:
            contenidos=archivo.readlines()
            contenidos=[contenido.strip() for contenido in contenidos]
            if contenidos:
                contenido_aleatorio=random.choice(contenidos)
                webbrowser.open(contenido_aleatorio)
    except FileExistsError:
        messagebox.showwarning('Error','No se encontro el archivo de texto')
                    
texto_hora=tk.Label(raiz,fg='green2',bg='black')
texto_hora.grid(columnspan=3,row=0,sticky='nsew',ipadx=5,ipady=5)
    
obtener_tiempo()

raiz.mainloop()   