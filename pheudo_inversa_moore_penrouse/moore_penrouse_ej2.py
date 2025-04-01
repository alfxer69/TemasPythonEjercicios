import numpy as np
#Pseudoinversa de Moore-Penrose 
#Ejemplo 2: Matriz A_p de 3x2
#La matriz A_p es una matriz de 3 filas y 2 columnas
#La matriz A_p es una matriz rectangular, por lo que no tiene inversa

A_p = np.array([[1, 2], [3, 4], [5, 6]])
print(f'Matriz A_p: \n{A_p}')

A_pinv=np.linalg.pinv(A_p) #Matriz pseudo-inversa de A_p usando la función pinv
print(f'\nMatriz pseudo-inversa de A_p usando la función pinv:\n{A_pinv}')

b=np.array([7,8,9])
print(f'\nVector b:\n{b}')

x=A_pinv @ b #Producto punto entre A_pinv y b
print(f'\nProducto punto entre A_pinv y b Vector x:\n{x}')
