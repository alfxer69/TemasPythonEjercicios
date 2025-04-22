from tkinter import *

raiz=Tk()
raiz.title('Calculadora')
raiz.config(width=800,height=200,bg='blue',relief='groove',bd=5)
raiz.iconbitmap(r'E:\PythonAvanzado\tkinter\imagenconquer.ico')

miframe=Frame(raiz)
miframe.config(width=400,height=400)
miframe.pack()
numeropantalla=StringVar()

operacion=""
resultado=0

reset_pantalla=True

#----------------pantalla------------------------------

pantalla=Entry(miframe,textvariable=numeropantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=5)
pantalla.config(background='black',fg='#03f943',justify='right')

#-----------------pulsasiones teclado-------------------

def numeropulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeropantalla.set(num)
        reset_pantalla=False
    else:
        numeropantalla.set(numeropantalla.get()+num)

#--------------------funcion suma-----------------------

def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=float(num)
    operacion="suma"
    reset_pantalla=True
    numeropantalla.set(resultado)
#--------------------funcion resta------------------------
resultado2=0
x=0
def resta(num):
    global operacion
    global resultado
    global resultado2
    global x
    global reset_pantalla
    
    if x==0:
        
        resultado2=float(num)
        
        resultado=resultado2
        
    else:
        if x==1:
            resultado=resultado2-float(num)
            print(resultado2)
        else:
            resultado=int(resultado)-float(num)
        numeropantalla.set(resultado)
        resultado=numeropantalla.get()
    operacion='resta'
    x+=1
    reset_pantalla=True

#----------------funcion producto------------------------
y=0
def producto(num):
    global resultado
    global reset_pantalla
    global operacion
    global y
    global num1
        
    if y==0:
        num1=float(num)
        resultado=num1
    else:
        if y==1:
            resultado=num1*float(num)
        else:
            resultado=int(resultado)*float(num)
        numeropantalla.set(resultado)
        resultado=numeropantalla.get()
    y+=1
    operacion='producto'
    reset_pantalla=True

#-----------------funcion dividir------------------------

m=0
def dividir(num):
    global resultado
    global operacion
    global m
    global reset_pantalla
    global num1
    
    
    if m==0:
        
        num1=float(num)
        resultado=num1
    else:
        if m==1:
            resultado=num1/float(num)
        else:
            resultado=float(resultado)/float(num)
        numeropantalla.set(resultado)
        resultado=numeropantalla.get()
    m+=1
    operacion='dividir'
    reset_pantalla=True
#-------------------funcion el_resultado------------------
def el_resultado():
    global resultado
    global x 
    global y
    global m
    
    
    if operacion=='suma':
        numeropantalla.set(resultado+int(numeropantalla.get()))
        resultado=0
    elif operacion=='resta':
        numeropantalla.set(int(resultado)-int(numeropantalla.get()))
        resultado=0
        x=0
    elif operacion=='producto':
        numeropantalla.set(int(resultado)*int(numeropantalla.get()))
        y=0
        resultado=0
    elif operacion=='dividir':
        numeropantalla.set(int(resultado)/int(numeropantalla.get()))
        m=0
        resultado=0
    


#----------------fila 1--------------------------------

boton7=Button(miframe,text='7',width=3,command=lambda:numeropulsado('7'))
boton7.grid(row=2,column=1)
boton8=Button(miframe,text='8',width=3,command=lambda:numeropulsado('8'))
boton8.grid(row=2,column=2)
boton9=Button(miframe,text='9',width=3,command=lambda:numeropulsado('9'))
boton9.grid(row=2,column=3)
botondiv=Button(miframe,text='/',width=3,command=lambda:dividir(numeropantalla.get()))
botondiv.grid(row=2,column=4)

#----------------fila 2---------------------------------------

boton4=Button(miframe,text='4',width=3,command=lambda:numeropulsado('4'))
boton4.grid(row=3,column=1)
boton5=Button(miframe,text='5',width=3,command=lambda:numeropulsado('5'))
boton5.grid(row=3, column=2)
boton6=Button(miframe,text='6',width=3,command=lambda:numeropulsado('6'))
boton6.grid(row=3,column=3)
botonmult=Button(miframe,text='x',width=3,command=lambda:producto(numeropantalla.get()))
botonmult.grid(row=3,column=4)

#-----------------fila 3--------------------------------

boton1=Button(miframe,text='1',width=3,command=lambda:numeropulsado('1'))
boton1.grid(row=4,column=1)
boton2=Button(miframe,text='2',width=3,command=lambda:numeropulsado('2'))
boton2.grid(row=4, column=2)
boton3=Button(miframe,text='3',width=3,command=lambda:numeropulsado('3'))
boton3.grid(row=4,column=3)
botonrest=Button(miframe,text='-',width=3,command=lambda:resta(numeropantalla.get()))
botonrest.grid(row=4,column=4)

#-----------------fila 4--------------------------------

boton0=Button(miframe,text='0',width=3,command=lambda:numeropulsado('0'))
boton0.grid(row=5,column=1)
botoncoma=Button(miframe,text=',',width=3,command=lambda:numeropulsado(','))
botoncoma.grid(row=5, column=2)
botonigua=Button(miframe,text='=',width=3,command=lambda:el_resultado())
botonigua.grid(row=5,column=3)
botonsuma=Button(miframe,text='+',width=3,command=lambda:suma(numeropantalla.get()))
botonsuma.grid(row=5,column=4)

raiz.mainloop()
