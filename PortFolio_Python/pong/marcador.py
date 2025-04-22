import turtle
from sounds import *

class Marcador:
    def __init__(self):
        # Crear un objeto turtle para el marcador
        self.marcador = turtle.Turtle()
        self.marcador.speed(0)
        self.marcador.color("white")
        self.marcador.penup()
        self.marcador.hideturtle()  # Esconder el objeto turtle, solo mostrar texto
        self.marcador.goto(0, 260)  # Posición inicial del marcador
        self.jugador_1_puntaje = 0
        self.jugador_2_puntaje = 0
        self.actualizar_marcador()

    def actualizar_marcador(self):
        # Borrar el marcador anterior
        self.marcador.clear()
        # Escribir el nuevo marcador
        self.marcador.write(f"Player 1  [ {self.jugador_1_puntaje} - {self.jugador_2_puntaje} ]  Player 2",
                            align="center", font=("Verdana", 24, "normal"))

    def aumentar_puntaje_jugador_1(self):
        self.jugador_1_puntaje += 1
        self.actualizar_marcador()
        reproducir_sonido_marcador()

    def aumentar_puntaje_jugador_2(self):
        self.jugador_2_puntaje += 1
        self.actualizar_marcador()
        reproducir_sonido_marcador()
