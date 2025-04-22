import pygame
import random
import json

pygame.init()

ancho=550
background=(251,247,245)
pantalla=pygame.display.set_mode((ancho,ancho))    
pygame.display.set_caption('SUDOKU')

color=(0,0,0)

#cargamos una tabla hecho en json donde se encuentran tablas que pueden o no tener solucion
def cargar_tableros():
    with open(r'E:\PythonAvanzado\Pandas\nltk\portfolio\tablero_sudoku.json','r') as archivo:
        contenido=json.load(archivo)
    return contenido['tableros']        

#tomamos un tablero de forma aletoria del archivo json    
def mostrar_tablero_aleatorio():
    tableros=cargar_tableros()
    #buscamos un tablero aleatorio 
    tablero_aletorio=random.choice(tableros)
    for fila in tablero_aletorio:
        print(fila)
    return tablero_aletorio

#mostramos los numeros en la tabla  
def mostrar_numeros(tablero):
    font=pygame.font.SysFont(None,40)
    for fila in range(9):
        for columna in range(9):
            numero=tablero[fila][columna]
            if numero!=0:
                texto=font.render(str(numero),True,(0,0,0))
                pantalla.blit(texto,(50+columna*50+15,50+50*fila+15))
        
#dibujamos la cuadricula para ubicar los numeros
def dibujar_cuadriculas():
    for i in range(0,10):
        linea=pygame.draw.line(pantalla,color=(0,0,0),start_pos=((50*i)+50,50),end_pos=(50+(50*i),500),width=2)
        linea=pygame.draw.line(pantalla,color=(0,0,0),start_pos=(50,50*i+50),end_pos=(500,50*i+50),width=2)
        if i%3==0:
            linea=pygame.draw.line(pantalla,color=(0,0,0),start_pos=(50+(50*i),50),end_pos=(50+(50*i),500),width=4)
            linea=pygame.draw.line(pantalla,color=(0,0,0),start_pos=(50,50*i+50),end_pos=(500,50*i+50),width=4)

#algoritmos de backtracking para hallar la solucion del sudoku
def solucionar_sudoku(tablero):
    for i in range(0,9):
        for j in range(0,9):
            if tablero[i][j]==0:
                for n in range(1,10):
                    if numero_valido(tablero,i,j,n):
                        tablero[i][j]=n
                        #backtraking
                        if solucionar_sudoku(tablero):
                            return True
                        else:
                            tablero[i][j]=0
                return False
    #se soluciono el juego
    return True

#se verifica si el numero es valido en la celda
def numero_valido(tablero,i,j,n):
    fila=tablero[i]
    columna=[f[j] for f in tablero]
    sub_bloque=[tablero[a][b]
                for a in range (9)
                for b in range (9)
                if i//3==a//3 and j//3==b//3]
    return n not in fila and n not in columna and n not in sub_bloque

#Mostramos la solucion del tablero total si no lo tiene lo indicamos
def mostrar_solucion(tablero):
    if solucionar_sudoku(tablero):
        print('Sudoku Resuelto')
        return True,tablero
    else:
        print('No se puede resolver el soduko')
        return False,tablero

#creamos un boton para indicar que se active el algoritmo y resuelva
def dibujar_boton():
        boton_rect=pygame.Rect(220,510,120,30)
        pygame.draw.rect(pantalla,(0,255,0),boton_rect)
        font=pygame.font.SysFont(None,20)
        texto=font.render('Mostrar Solucion',True,(0,0,0))
        pantalla.blit(texto,(225,515))
        return boton_rect

#creamos una etiqueta con los mensajes si se soluciono o no el problema
def dibujar_etiqueta(estado):
    font=pygame.font.SysFont(None,20)
    if estado is not None:
        if estado:
            mensaje='Sudoku Resuelto'
            color_mensaje=(0,128,0)#Verde si se resuelve
        else:
            mensaje='No se puede resolver Sudoku'
            color_mensaje=(255,0,0)#Rojo si no se resuelve
        texto=font.render(mensaje,True,color_mensaje)
        pantalla.blit(texto,(50,10))#Mensaje parte superior

def main():
    
    tablero_aleatorio=mostrar_tablero_aleatorio()     
    sudoku_resuelto=None
                
    run=True
    #bucle principal
    while run:
        pantalla.fill(background)
        
        dibujar_cuadriculas()
        
        mostrar_numeros(tablero_aleatorio)
        
        dibujar_etiqueta(sudoku_resuelto)
        
        boton_rect=dibujar_boton()
                
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.MOUSEBUTTONDOWN:#pulsar el mouse
                if event.button==1:#boton izquierda del mouse
                    if boton_rect.collidepoint(event.pos):
                        sudoku_resuelto,tablero_aleatorio=mostrar_solucion(tablero_aleatorio)
    
        pygame.display.update()
       
    pygame.quit()
    
main()
