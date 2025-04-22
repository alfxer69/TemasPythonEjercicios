import turtle
from sounds import *

class Paleta:
    def __init__(self, x, y):
        self.paleta = turtle.Turtle()
        self.paleta.speed(0)
        self.paleta.shape("square")
        self.paleta.color("white")
        self.paleta.shapesize(stretch_wid=6, stretch_len=1)
        self.paleta.penup()
        self.paleta.goto(x, y)

    # Método para mover la paleta hacia arriba
    def mover_arriba(self):
        y = self.paleta.ycor()
        if y < 240:  # Limitar movimiento para que no salga de la pantalla
            y += 20
        self.paleta.sety(y)
        reproducir_sonido_mover_paleta()

    # Método para mover la paleta hacia abajo
    def mover_abajo(self):
        y = self.paleta.ycor()
        if y > -240:  # Limitar movimiento para que no salga de la pantalla
            y -= 20
        self.paleta.sety(y)
        reproducir_sonido_mover_paleta()