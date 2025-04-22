from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog as fd
from tkinter import simpledialog, messagebox
import os
import subprocess
from reportlab.lib.pagesizes import A4, A3, letter
from reportlab.pdfgen import canvas
from tkinter import font, ttk
import tkinter.font as tkfont


raiz=Tk()
raiz.title('Editor de Texto')
mimenu=Menu(raiz)
raiz.config(menu=mimenu,width=1200,height=600,relief='ridge',bd=4)
raiz.resizable(False,False)

miframe=Frame(raiz)
miframe.pack(fill='both', expand=True)

texto=Text(miframe,wrap='word')
texto.config(relief='groove',font=('Arial',12),bd=4,padx=6,pady=4,wrap='word')


#-----------------Configuracion de Scrollbar--------------------
#Crear el scrollbar horizontal
scroll_x = Scrollbar(miframe, orient='horizontal', command=texto.xview)
# Crear el Scrollbar vertical
scroll_y = Scrollbar(miframe, orient='vertical', command=texto.yview)
# Configurar el TextO para que funcione con ambos Scrollbars
texto.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
# Posicionar los Scrollbars
scroll_y.pack(side='right',fill='y')  
scroll_x.pack(side='bottom',fill='x') 
texto.pack(side='left',fill='both', expand=True)  

directorio=''

#----------Posicion del cursor---------------
def actualizar_posicion(tecla_movida):
    ubicacion=texto.index(INSERT)
    fila,columna=ubicacion.split('.')
    etiqueta2.config(text=f"Fila: {fila} Columna: {columna}")

#----------Archivo Nuevo--------------------
def nuevo():
    global directorio
    estado1.set('Creamos Nuevo Archivo')
    directorio=''
    texto.delete(1.0,END)
    raiz.title(directorio+' - editor_texto')
    
#-----------Abrir Archivo------------------
def abrir():
    global directorio
    estado1.set('Abrimos Archivo')
    directorio=fd.askopenfilename(
        initialdir='.',
        filetypes=[('Archivos de texto',"*.txt")],
        title='Abrir un archivo de texto')
    if directorio!='':
       fichero=open(directorio,'r',encoding='utf-8')
       contenido=fichero.read()
       texto.delete(1.0,END)
       texto.insert('insert',contenido)
       fichero.close()
       raiz.title(directorio+' - editor_texto')

#--------Guardar Archivo-----------------------
def guardar():
    global directorio
    estado1.set('Guardamos Archivo')
    if directorio!='':
        contenido=texto.get(1.0,'end-1c')
        fichero=open(directorio,'w+',encoding='utf-8')
        fichero.write(contenido)
        fichero.close()
        estado1.set('Fichero guardado con exito')
    else:
        guardar_como()

#---------Guardar Como-----------------------        
def guardar_como():
    global directorio
    
    estado1.set('Guardar como...')
    fichero=fd.asksaveasfile(title='Guardar Archivo',
                                mode='w',defaultextension='.txt'
                                ,filetypes=[('Archivos de texto',"*.txt")])
    if fichero is not None:
        ruta=fichero.name
        contenido=texto.get(1.0,'end-1c')
        fichero=open(ruta,'w+',encoding='utf-8')
        fichero.write(contenido)
        fichero.close()
        estado1.set('Fichero Guardado Correctamente')
    else:
        estado1.set('Guardado Cancelado')
        ruta=''    


#---------------Modulo impresion en pdf--------------------

def imprimir_pdf():
    global texto
    
    estado1.set('Imprimir en PDF')
    contenido=texto.get(1.0,'end-1c')
    tamano_papel=A4
    lienzo = canvas.Canvas("documento.pdf", pagesize=tamano_papel)
    ancho, alto = tamano_papel
    # Establecer la posición inicial del texto
    x = 50
    y = alto - 50
       
    # Dibujar texto en el PDF
    for linea in contenido.split('\n'):
        lienzo.drawString(x, y, linea)
        y -= 14  # Espacio entre líneas
    lienzo.showPage()
    lienzo.save()
    archivo_pdf=r'E:\PythonAvanzado\tkinter\documento.pdf'
    abrir_pdf(archivo_pdf)
    

#-----------Abrir elarchivo en pdf para imprimir-------
def abrir_pdf(archivo_pdf):
    if os.name=='nt': #si trabajamos solo con windows
        os.startfile(archivo_pdf)
    

#------Definir regla con Canvas--------------
regla=Canvas(raiz,height=30,bg='lightgray')
regla.pack(fill='x')

#----Actualizar la regla cada 10 y 50 pixeles---------
def actualizar_regla(ancho_papel):
    regla.delete('all')
    for i in range(0,round(ancho_papel),10):
        x=i+10 #para no iniciar en el borde cada 10 pixeles
        if i%50==0: #Linea mas larga cada 50 pixeles
            regla.create_line(x,5,x,25,fill='black')
            regla.create_text(x+3,15,text=(i),anchor='n',font=('Arial',8))
        else:
            regla.create_line(x,15,x,25,fill='black')  
            
def cambiar_tamano_papel(tamano):
    
    ancho=actualizar_tamano_texto(tamano)
    #ajuste aproximado alancho en caracteres
    texto.config(width=int(ancho/8),state='normal')
    actualizar_regla(ancho)  
    
#----------Definiendo el ancho de papel----------
def actualizar_tamano_texto(tamano):
    x,y=tamano
    return x
#Por defecto se selecciona A4
cambiar_tamano_papel(A4)

#-----------------Formato Fuentes------------------------------
# Función para actualizar el ejemplo de la fuente
def actualizar_vista_previa():
    fuente = font.Font(family=var_fuente.get(), size=var_tamano.get(), weight=var_peso.get(), slant=var_inclinacion.get())
    label_vista_previa.config(font=fuente)

def aplicar_fuente():
    fuente = font.Font(family=var_fuente.get(), size=var_tamano.get(), weight=var_peso.get(), slant=var_inclinacion.get())
    texto.config(font=fuente)

def elegir_fuente():
    global var_fuente, var_tamano, var_peso, var_inclinacion, label_vista_previa,fuente_lista
    
    fuente_dialogo = Toplevel(raiz)
    fuente_dialogo.title("Seleccionar Fuente")
    
    # Lista de fuentes disponibles
    fuentes_disponibles = list(font.families())

    # Variables para almacenar la configuración de fuente
    var_fuente =StringVar(value="Arial")
    var_tamano =IntVar(value=12)
    var_peso =StringVar(value="normal")
    var_inclinacion =StringVar(value="roman")

    # seleccionar tipo de fuente
    Label(fuente_dialogo, text="Tipo de fuente:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
    fuente_lista = ttk.Combobox(fuente_dialogo, textvariable=var_fuente, values=fuentes_disponibles)
    fuente_lista.grid(row=0, column=1, padx=10, pady=5)

    # seleccionar tamaño
    Label(fuente_dialogo, text="Tamaño:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
    Spinbox(fuente_dialogo, from_=6, to=72, textvariable=var_tamano).grid(row=1, column=1, padx=10, pady=5)

    #seleccionar estilo (normal/negrita)
    Label(fuente_dialogo, text="Estilo:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
    Radiobutton(fuente_dialogo, text="Normal", variable=var_peso, value="normal").grid(row=2, column=1, sticky='w')
    Radiobutton(fuente_dialogo, text="Negrita", variable=var_peso, value="bold").grid(row=2, column=1, padx=80, sticky='w')

    #seleccionar inclinación (normal/itálica)
    Label(fuente_dialogo, text="Inclinación:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
    Radiobutton(fuente_dialogo, text="Normal", variable=var_inclinacion, value="roman").grid(row=3, column=1, sticky='w')
    Radiobutton(fuente_dialogo, text="Itálica", variable=var_inclinacion, value="italic").grid(row=3, column=1, padx=80, sticky='w')

    #Texto de vista previa dentro del diálogo
    label_vista_previa = Label(fuente_dialogo, text="Vista previa de la fuente", font=("Arial", 12))
    label_vista_previa.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    #Botón para aplicar cambios y actualizar la vista previa
    Button(fuente_dialogo, text="Actualizar vista previa", command=actualizar_vista_previa).grid(row=5, column=0, columnspan=2, pady=10)
    Button(fuente_dialogo, text="Aplicar al texto principal", command=aplicar_fuente).grid(row=6, column=0, columnspan=2, pady=10)

#-------------------Edicion Deshacer------------------
def deshacer():
    texto.delete('1.0',END)
    estado1.set('Deshacer el texto')

palabra_buscada=''
indice_busqueda='1.0'

#--------------------Edicion buscar--------------------
def buscar():
    global palabra_buscada,indice_busqueda
    
    palabra_buscada=simpledialog.askstring('Buscar','Ingresa la palabra a buscar')
    if not palabra_buscada:
        return
    indice_busqueda='1.0'
    estado1.set('Buscar palabra')
    buscar_siguiente()

#---------------------Edicion buscar siguiente----------------
def buscar_siguiente():
    global indice_busqueda,palabra_buscada 
    estado1.set('Buscar Siguiente')  
    if not  palabra_buscada:
        messagebox.showwarning('Buscar','Primero selecciona la opcion "Buscar" para ingresar una palabra' )
        return
    #limpiamos el resaltado anterior 
    texto.tag_remove('highlight','1.0',END)
    #Buscamos la siguiente ocurrencia
    posicion=texto.search(palabra_buscada,indice_busqueda,stopindex=END)

    if posicion:
        posicion_final=f'{posicion}+{len(palabra_buscada)}c'
        texto.tag_add('highlight',posicion,posicion_final)
        texto.tag_config('highlight',background='yellow')
        #actualizamos elindice para buscar la siguiente 
        indice_busqueda=posicion_final
        texto.mark_set('insert',posicion_final)
        #hacemos que la posicion final sea visible 
        texto.see(posicion_final)
    else:
        #reiniciamos si no hay mas palabras iguales
        indice_busqueda='1.0'
        messagebox.showinfo('Fin de busqueda','No hay mas coincidencias')

#-----------------Edicion buscar anterior----------------------
def buscar_anterior():
    global palabra_buscada, indice_busqueda
    estado1.set('Buscar Anterior')
    if not palabra_buscada:
        messagebox.showwarning('Buscar', "Primero selecciona la opción 'Buscar' para ingresar una palabra.")
        return
    
    # Limpiar resaltado anterior
    texto.tag_remove('highlight', '1.0', END)
    
    # Buscar la ocurrencia anterior
    posicion=texto.search(palabra_buscada, indice_busqueda, stopindex="1.0", backwards=True)
    
    if posicion:
        posicion_final=f"{posicion}+{len(palabra_buscada)}c"
        texto.tag_add("highlight", posicion, posicion_final)
        texto.tag_config("highlight", background="yellow")
        
        # Actualizar el índice para buscar la ocurrencia anterior
        indice_busqueda=posicion
        texto.mark_set("insert", posicion)
        texto.see(posicion)
    else:
        # Reiniciar si no se encuentra más ocurrencias
        indice_busqueda=END
        messagebox.showinfo("Fin de la búsqueda", "No se encontraron más ocurrencias.")

#----------------Ver Zoom------------------------------------
def zoom():
    zoom_w=Toplevel(raiz)
    zoom_w.title('Opciones de Zoom')
    zoom_w.config(width=500,height=500)
    zoom_w.resizable(False,False)
    estado1.set('Ventana Ver para alejar o acercar')
    
    Label(zoom_w, text="Opciones de Zoom").pack(padx=10,pady=10)
    
    Button(zoom_w,text='Acercar',command=acercar).pack(padx=10,pady=10)
    Button(zoom_w,text='Alejar',command=alejar).pack(padx=10,pady=10)

def alejar():
    longitud=int(texto['font'].split()[1])+2
    texto.config(font=('Arial',longitud))
    
def acercar():
    longitud=int(texto['font'].split()[1])-2
    texto.config(font=('Arial',longitud))
    
#------------------Menu Ayuda--------------------------
def ayuda():
    ayuda_w=Toplevel(raiz)
    ayuda_w.title('Ayuda')
    ayuda_w.config(width=800,height=800,relief='solid',bd=5)
    #creamos un textbox entro de la ventana ayuda 
    ayuda_texto=Text(ayuda_w,wrap='word')
    ayuda_texto.config(background='lightgray')
    ayuda_texto.insert('1.0','Esta es seccion de ayuda del Editor de Texto.\n'
                       'El editor cuenta con un cuadro de texto donde se puede'
                       ' escribir un documento al cual puedes hacer los cambios que requieras.\n'
                       'Ademas en la parte inferior derecha tenemos una etiqueda de estado'
                       ' en la parte izquierda tenemos la posicion del cursor la fila y columna\n'
                       'Se cuentas con un menu con las siguientes opciones:\n'
                       'Archivo-Editar-Formato-Ver-Ayuda\n'
                       'Archivo:\n' 
                       'Nuevo: aqui puedes crear un archivo nuevo\n'
                       'Abrir: abrir un directorio para llamar a un archivo\n'
                       'Guardar: podemos grabar un documento de texto\n'
                       'Guardar Como: podemos grabar un documento con otro nombre\n'
                       'Imprimir en PDF: podemos abrir el documento en pdf para gestionar la impresion\n'
                       'Editar:\n'
                       'Deshacer: borrar un documento de texto dentro del textbox\n'
                       'Buscar: podemos buscar una palabra y la sombrea de amarillo\n'
                       'Buscar siguiente: podemos buscar la misma palabra en el texto\n'
                       'Buscar Anterior: podemos buscar retrocediendo a la anterior encontrada\n'
                       'Formato:\n'
                       'Tipo de Fuente: podemos seleccionar el tipo de fuente que deseamos'
                       ' cambiar el tamaño de las letras,su estilo como negrita su inclinacion'
                       ' podemos ver con esta opcion como quedaria el texto con los cambios'
                       ' luego de hacer los cambios deseados podemos aplicar y todo el texto cambiara\n'
                       'Tamaños de papel: podemos escoger el tamaño de papel aqui tenemos tres '
                       ' opciones A4, A3 y letter este cambio ayuda a poder ajustar nuestro texto'
                       ' asimismo podemos verificar como cambia la regla en la parte inferior segun el tamaño'
                       'Ver:\n'
                       'Zoom: con esta opcion podemos acercar o alejar el texto con esta opcion'
                       ' no cambia el tamaño del texto solo lo agranda o reduce\n'
                       'Ayuda:\n'
                       'Ver ayuda: aqui podemos ver las diferentes opciones que tiene este editor.\n'
                       'Acerca De..: verifica el creador, fecha del editor y version del programa')
    ayuda_texto.config(state='disabled')
    ayuda_texto.pack(expand=True,fill='both')

def acerca_de():
    acerca_d=Toplevel(raiz)
    acerca_d.title('Acerca de...')
    acerca_d.config(relief='solid',bd=5)
    
    Text_acerca=Text(acerca_d,wrap='word')
    Text_acerca.config(width=40,height=5,background='lightgray')
    Text_acerca.pack(expand=True,fill='both')
    
    fuente_grande=tkfont.Font(family='Arial',size=14,weight='bold')
    fuente_mediana=tkfont.Font(family='Arial',size=12)
    fuente_pequena=tkfont.Font(family='Arial',size=10)
    
    Text_acerca.tag_configure('Creador',font=fuente_grande,justify='center')
    Text_acerca.tag_configure('Programa',font=fuente_mediana,justify='center')
    Text_acerca.tag_configure('Version',font=fuente_pequena,justify='center')
    
    Text_acerca.insert('1.0','Creador: Alfredo Muñoz Flores\n\n\n','Creador')
    Text_acerca.insert('2.0','Programa: Editor de Texto\n\n\n','Programa')
    Text_acerca.insert('3.0','Version: Version 1.0\n\n\n','Version')  
    Text_acerca.config(state='disabled')
    
    
      
#-------------------Menu/archivo-----------------------
archivomenu=Menu(mimenu,tearoff=0)
archivomenu.add_command(label='Nuevo',command=nuevo)
archivomenu.add_command(label='Abrir',command=abrir)
archivomenu.add_command(label='Guardar',command=guardar)
archivomenu.add_command(label='Guardar Como...',command=guardar_como)
archivomenu.add_command(label='Imprimir en PDF',command=imprimir_pdf)
archivomenu.add_separator()
archivomenu.add_command(label='Salir',command=raiz.quit)
mimenu.add_cascade(menu=archivomenu,label='Archivo')

#------------Menu/edicion---------------------
edicionmenu=Menu(mimenu,tearoff=0)
edicionmenu.add_command(label='Deshacer',command=deshacer)
edicionmenu.add_command(label='Buscar',command=buscar)
edicionmenu.add_command(label='Buscar Siguiente',command=buscar_siguiente)
edicionmenu.add_separator()
edicionmenu.add_command(label='Buscar Anterior...',command=buscar_anterior)
mimenu.add_cascade(menu=edicionmenu,label='Editar')

#-------------Menu/Formato---------------------
formatomenu=Menu(mimenu,tearoff=0)
formatomenu.add_command(label='Tipo de Fuente',command=elegir_fuente)
mimenu.add_cascade(menu=formatomenu,label='Formato')
menu_tamanos = Menu(formatomenu, tearoff=0)
menu_tamanos.add_command(label="A4", command=lambda :cambiar_tamano_papel(A4))
menu_tamanos.add_command(label="A3", command=lambda :cambiar_tamano_papel(A3))
menu_tamanos.add_command(label="letter", command=lambda :cambiar_tamano_papel(letter))
# Agregar el submenú de tamaños al menú formato
formatomenu.add_cascade(label="Tamaños de Papel", menu=menu_tamanos)
    
#-------------Menu/Ver-------------------------
vermenu=Menu(mimenu,tearoff=0)
vermenu.add_command(label='Zoom',command=zoom)
mimenu.add_cascade(menu=vermenu,label='Ver')

#--------------Menu/Ayuda----------------------
ayudamenu=Menu(mimenu,tearoff=0)
ayudamenu.add_command(label='Ver la Ayuda',command=ayuda)
ayudamenu.add_separator()
ayudamenu.add_command(label='Acerca de....',command=acerca_de)
mimenu.add_cascade(menu=ayudamenu,label='Ayuda')

#Etiqueta inferior
estado1=StringVar()
estado1.set('Bienvenido al Editor')
etiqueta1=Label(raiz,textvariable=estado1,justify='left')
etiqueta1.pack(side='left')

#Etiqueta posicion
etiqueta2 = Label(raiz, text="Fila: 1 Columna: 0")
etiqueta2.pack(side='right')
# Detectar la posicion al mover cualquier tecla 
texto.bind('<KeyRelease>', actualizar_posicion)
texto.bind("<ButtonRelease-1>", actualizar_posicion)

raiz=mainloop()