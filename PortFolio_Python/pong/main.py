import turtle
from paleta import Paleta
from pelota import Pelota
from marcador import Marcador  # Importar la clase Marcador

def salir():
    turtle.bye()  # Cierra la ventana del juego

def main():
    # Crear la ventana del juego
    ventana = turtle.Screen()
    ventana.title("Pong Arcade")
    ventana.bgcolor("black")
    ventana.setup(width=900, height=600)
    ventana.tracer(0)

    # Crear el marcadoro
    marcador = Marcador()

    # Crear las paletas y la pelota
    paleta_izquierda = Paleta(-400, 0)
    paleta_derecha = Paleta(400, 0)
    pelota = Pelota(marcador)  # Pasar el marcador a la pelota

    # Controles de la paleta izquierda
    ventana.listen()
    ventana.onkeypress(paleta_izquierda.mover_arriba, "w")
    ventana.onkeypress(paleta_izquierda.mover_abajo, "s")

    # Controles de la paleta derecha
    ventana.onkeypress(paleta_derecha.mover_arriba, "o")
    ventana.onkeypress(paleta_derecha.mover_abajo, "l")

    # Control para salir
    ventana.onkeypress(salir, "x")

    # Bucle principal del juego
    while True:
        ventana.update()

        # Mover la pelota
        pelota.mover()

        # Detectar colisiones con las paletas
        pelota.colision_paleta(paleta_izquierda)
        pelota.colision_paleta(paleta_derecha)

            
if __name__ == "__main__":
    main()
