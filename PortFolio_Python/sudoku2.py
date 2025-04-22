import json
import random

# Cargar el archivo JSON que contiene los tableros de Sudoku
def cargar_tableros():
    with open(r'E:\PythonAvanzado\Pandas\nltk\portfolio\tablero_sudoku.json', 'r') as file:
        data = json.load(file)
    return data["tableros"]

# Seleccionar un tablero aleatorio
def mostrar_tablero_aleatorio():
    tableros = cargar_tableros()
    
    # Seleccionar un tablero aleatorio de la lista de tableros
    tablero_aleatorio = random.choice(tableros)
    
    # Mostrar el tablero seleccionado
    print("Tablero de Sudoku Aleatorio:")
    for fila in tablero_aleatorio:
        print(fila)

# Llamar a la función para mostrar un tablero aleatorio
mostrar_tablero_aleatorio()