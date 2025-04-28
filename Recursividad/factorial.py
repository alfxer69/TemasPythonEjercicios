#Hallar el factorial de un número n de forma recursiva.
# El factorial de n (n!) es el producto de todos los números enteros positivos desde 1 hasta n.
# Por ejemplo, el factorial de 5 es 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    """
    Función recursiva que calcula el factorial de un número n.
    :param n: Número entero no negativo.
    :return: Factorial de n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f'El factorial es {factorial(5)}')  # Salida: 120
