#El presente ejetmplo muestra como se puede descomponer una matriz en sus valores singulares
# y como se puede reconstruir la matriz original a partir de estos valores.

import numpy as np

#generamos la siguiente matriz
A = np.array([[-1,2],[3,-2],[5,7]])
print(f'Matriz A: \n{A}\n')

U,sigma,V=np.linalg.svd(A)
print(f'U: \n{U}\n')
print(f'sigma: \n{sigma}\n') #Los valores singulares
print(f'V: \n{V}\n')  #La matriz V es la matriz de rotación   Vt=V^T

#hallar la diagonal de sigma
D=np.diag(sigma)
print(f'Diagonal de sigma: \n{D}\n')
D=np.concatenate((D,[[0,0]]),axis=0)
print(f'Diagonal de sigma: \n{D}\n')

#Descomposición de la matriz A
#A=U*D*V^T
A=np.dot(U,np.dot(D,V))
print(f'A: \n{A}\n')
