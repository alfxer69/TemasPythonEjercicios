import turtle as t 
import tkinter as tk 
from tkinter import messagebox
import pygame
import time

pygame.mixer.init()

#cargamos los sonidos para colisiones y musica de fondo
golpe_sonido=pygame.mixer.Sound(r'E:\PythonAvanzado\Pandas\nltk\portfolio\sonidos\hit-by-a-wood-230542.mp3') 
pygame.mixer.music.load(r'E:\PythonAvanzado\Pandas\nltk\portfolio\sonidos\Kashido - Swan Lake Theme.mp3')

#configuramos la interfaz grafica o ventana
ventana=t.Screen()
ventana.title('Game Arcade Pong Powered by Alfredo Muñoz Flores')
ventana.bgcolor('black')
ventana.setup(800,600)
ventana.tracer(0) #Activa o desactiva la animación de la tortuga actualiza los dibujos

#Varibles del scoring
score_A=0
score_B=0

#configurar el primer jugador
player_A=t.Turtle()
player_A.shape('square')
player_A.color('white')
player_A.penup()
player_A.goto(-350,0)
#se multiplica por 20 pixeles y modificamos la barra
player_A.shapesize(stretch_wid=5,stretch_len=1)

#configurar el segundo jugador
player_B=t.Turtle()
player_B.shape('square')
player_B.color('white')
player_B.penup()
player_B.goto(350,0)
player_B.shapesize(stretch_wid=5,stretch_len=1)

#Configuramos el balon de rebote
balon=t.Turtle()
balon.shape('circle')
balon.color('white')
balon.penup()
balon.goto(0,0)
balon.dx=0.2
balon.dy=-0.2

#configuracion de linea central
linea=t.Turtle()
linea.color('white')
linea.pensize(2)
linea.goto(0,400)
linea.goto(0,-400)

#Creando el scoring
score=t.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write('Player 1: 0            Player 2: 0',align='center',font=('Courier',24,'normal'))


#Funciones para dar movimiento a los objetos
def player_A_up():
    y=player_A.ycor()
    if y<250:
        y+=20
        player_A.sety(y)

def player_A_down():
    y=player_A.ycor()
    if y>-240:
        y-=20
        player_A.sety(y)

def player_B_up():
    y=player_B.ycor()
    if y<250:
        y+=20
        player_B.sety(y)

def player_B_down():
    y=player_B.ycor()
    if y>-240:
        y-=20
        player_B.sety(y)

#teclado destinado a mover las barras
ventana.listen()
ventana.onkeypress(player_A_up,'w')
ventana.onkeypress(player_A_down,'s')
ventana.onkeypress(player_B_up,'Up')
ventana.onkeypress(player_B_down,'Down')

#reproducir la musica de fondo con -1 se repite durante el juego.
pygame.mixer.music.play(-1)

#variables para manejar el tiempo y acelerar el juego
hora_inicio=time.time()
intervalo_incremento=60 #incremento cada minuto 

def fin_juego(winner):
    global score_A,score_B
    respuesta=messagebox.askquestion("Fin de juego",f'¡Jugador Ganador {winner} ¿Quieres Juegar Nuevamente?')
    if respuesta=='yes':
        jugar_nuevamente()
    else:
        ventana.bye()

def jugar_nuevamente():
    global score_A,score_B
    score_A=0
    score_B=0
    score.clear()
    score.write('Player 1: 0            Player 2: 0',align='center',font=('Courier',24,'normal'))
    balon.goto(0,0)
    balon.dx=0.5
    balon.dy=-0.5

#Bucle principal del pong    
while True:
    ventana.update()
    
    hora_actual=time.time()
    max_speed=1
    if hora_actual-hora_inicio>=intervalo_incremento and abs(balon.dx)<max_speed:
        balon.dx+=0.2 if balon.dx>0 else -0.2
        balon.dy+=0.2 if balon.dy>0 else -0.2
        hora_inicio=hora_actual
    
    #movimiento del balon
    balon.setx(balon.xcor()+balon.dx)
    balon.sety(balon.ycor()+balon.dy)
    
    #colisiones con los bordes por el balon
    if balon.ycor()>290:
        balon.dy*=-1
        golpe_sonido.play()
        
    if balon.ycor()<-290:
        balon.dy*=-1
        golpe_sonido.play()
        
    #Bordes derecha/izquierda
    if balon.xcor()>390:
        balon.goto(0,0)
        balon.dx*=-1
        score_A+=1
        score.clear()
        score.write(f'Player 1: {score_A}            Player 2: {score_B}',align='center',font=('Courier',24,'normal'))
                   
    if balon.xcor()<-390:
        balon.goto(0,0)
        balon.dx*=-1
        score_B+=1
        score.clear()
        score.write(f'Player 1: {score_A}            Player 2: {score_B}',align='center',font=('Courier',24,'normal'))
        
               
    if ((balon.xcor()>340 and balon.xcor()<350) 
            and (balon.ycor()<player_B.ycor()+50
            and balon.ycor()>player_B.ycor()-50)):
        balon.dx*=-1
        golpe_sonido.play()
    
    if ((balon.xcor()<-340 and balon.xcor()>-350)
            and (balon.ycor()<player_A.ycor()+50
            and balon.ycor()>player_A.ycor()-50)):
        balon.dx*=-1
        golpe_sonido.play()
        
    #verificaremos el ganador
    if score_A==3 or score_B==3:
        winner='Player 1' if score_A==3 else 'Player 2'
        fin_juego(winner)
    
    

    
                
        
        
        
