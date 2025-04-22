#En esta pagina puedo encontrar los diferentes codigos de error de conexion web
#https://developer.mozilla.org/es/docs/Web/HTTP/Status
import tkinter as tk 
from tkinter import messagebox
from tkinter import scrolledtext as st 
import urllib.request
from urllib.error import URLError,HTTPError

#creamos la funcion para determinar la conectividad
def conexion_web():
    pagina_web=ingreso_url.get()
    #nos aseguramos de adicionar a cualquier pagina ingresa solo con www.... adionarle el http:.
    if not pagina_web.startswith('http://') and not pagina_web.startswith('https://'):
        pagina_web='http://'+pagina_web #añadimos el prefijo para obtener la conexion
    try:
        #buscamos la respuesta de la pagina
        respuesta=urllib.request.urlopen(pagina_web)
        #https://developer.mozilla.org/es/docs/Web/HTTP/Status/200 aqui se encontro el codigo de respuesta de la pagina
        if respuesta.getcode()==200:
            #si es verdadero mostrara un mensaje 
            messagebox.showinfo('Resultado de Conexion','!El sitio esta disponible')
            #Mostraremos el contenido html de la pagina en un scrollText
            contenido=respuesta.read()
            text_scroll.delete(1.0,tk.END)
            text_scroll.insert(tk.END,contenido)
        else:
            #de no tener respuesta mostrara el codigo 
            messagebox.showinfo('Resultado de Conexion',f'!El sitio nos da un codigo: {respuesta.getcode()}')
    except HTTPError as error:
        #Mensaje de error si no se tiene respuesta de http
        messagebox.showwarning('Error al conectar',f'HTTPerror: {error.code} - El sitio no esta disponible')
    except URLError as error:
        #Mensaje de error si no tiene respuesta la url
        messagebox.showwarning('Error al conectar',f'URLError: {error.reason} -El sitio no esta disponible')
    except Exception as error:
        #Mensaje por algun error inesperado
        messagebox.showwarning('Error al conectar',f'Error inesperado: {str(error)}')

#Configuracion principal de la ventana
raiz=tk.Tk()
raiz.title('Comprobar la conectividad de un sitio web')
raiz.config(width=400,height=200,relief='groove',bd=5,background='lightgray')
raiz.resizable(width=False,height=False)

#Creacion de la etiqueta
etiqueta_web=tk.Label(raiz,text='Ingrese la url del sitio Web:')
etiqueta_web.pack(pady=5)

#CReacion del Entry para ingresar la pagina
ingreso_url=tk.Entry(raiz,relief='groove',bd=3,width=40,background='white',justify='left')
ingreso_url.pack(pady=5)

#Configuracion delboton comprobar al pulsar procedemos con la funcion conexion_web 
boton_comprobar=tk.Button(raiz,text='Comprobar Conexión',command=conexion_web)
boton_comprobar.pack(pady=10)

#Creamos el scrolltext donde se mostrara el texto html de la pagina 
text_scroll=st.ScrolledText(raiz,width=60,height=30,wrap=tk.WORD)
text_scroll.pack(pady=10)

raiz.mainloop()

    
