#Halla la suma de los n primeros números de la serie de Fibonacci.
# La serie de Fibonacci es una secuencia de números donde cada número es la suma de los dos anteriores.
# Por ejemplo, la serie comienza así: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# La función recursiva suma_fibonacci(n) calcula la suma de los n primeros números de la serie de Fibonacci.
# La función fibonacci(n) calcula el n-ésimo número de la serie de Fibonacci.

def fibonacci(n):   
    """
    Función recursiva que calcula el n-ésimo número de la serie de Fibonacci.
    :param n: Número entero no negativo.
    :return: n-ésimo número de la serie de Fibonacci.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Salida: 55