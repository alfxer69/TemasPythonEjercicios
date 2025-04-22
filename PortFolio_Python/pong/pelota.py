import turtle
from sounds import *

class Pelota:
    def __init__(self, marcador):
        self.pelota = turtle.Turtle()
        self.pelota.speed(0)  # Velocidad de la animación de la pelota
        self.pelota.shape("circle")
        self.pelota.color("white")
        self.pelota.penup()
        self.pelota.goto(0, 0)  # Comienza en el centro de la pantalla
        self.sonido_reproducido = False # Flag para controlar si se ha reproducido un audio

        self.marcador = marcador  # Guardar la instancia del marcador

        # Velocidad inicial de la pelota en los ejes X e Y
        self.dx = 1.5  # Velocidad en el eje X
        self.dy = 1.5  # Velocidad en el eje Y

    def mover(self):
        # Mover la pelota según su velocidad actual
        self.pelota.setx(self.pelota.xcor() + self.dx)
        self.pelota.sety(self.pelota.ycor() + self.dy)

        # Detectar colisiones con la parte superior e inferior de la pantalla
        if self.pelota.ycor() > 290:  # Rebota en el borde superior
            self.pelota.sety(290)
            self.dy *= -1  # Invertir la dirección en Y
            reproducir_sonido_pared()

        if self.pelota.ycor() < -280:  # Rebota en el borde inferior
            self.pelota.sety(-280)
            self.dy *= -1  # Invertir la dirección en Y
            reproducir_sonido_pared()
        
        # Detectar si la pelota pasa alguna de las paletas
        if self.pelota.xcor() > 480:
            self.pelota.goto(0, 0)  # Volver la pelota al centro
            self.dx *= -1  # Cambiar la dirección
            self.marcador.aumentar_puntaje_jugador_1()  # Usar la instancia del marcador

        elif self.pelota.xcor() < -480:
            self.pelota.goto(0, 0)  # Volver la pelota al centro
            self.dx *= -1  # Cambiar la dirección
            self.marcador.aumentar_puntaje_jugador_2()  # Usar la instancia del marcador
        
        if self.pelota.xcor() > 400 or self.pelota.xcor() < -400:
            self.pelota.color("red")  # Cambiar el color a rojo cuando pase la paleta
            if not self.sonido_reproducido:
                reproducir_sonido_punto()
                self.sonido_reproducido = True # Flageamos, ya que ya se ha reproducido el sonido.
        else:
            self.pelota.color("white")  # Restablecer el color cuando esté en juego
            self.sonido_reproducido = False # Reestablecemos condición para que vuelva a sonar la próxima vez.

    def colision_paleta(self, paleta):
        # Detectar colisiones con las paletas
        if (self.pelota.xcor() > 390 and self.pelota.distance(paleta.paleta) < 50) or \
           (self.pelota.xcor() < -390 and self.pelota.distance(paleta.paleta) < 50):
            self.dx *= -1  # Invertir la dirección en X
            reproducir_sonido_rebote()
