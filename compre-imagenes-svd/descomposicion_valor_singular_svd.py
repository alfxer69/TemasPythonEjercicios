import numpy as np 

#Generar una matriz de 2x2
A = np.array([[3,0],[4,5.]])
print(f'Matriz A: \n{A}')

U,sigma,V=np.linalg.svd(A)
print(f'U: \n{U}\n')
print(f'sigma: \n{sigma}\n') #Los valores singulares
print(f'V: \n{V}\n')  #La matriz V es la matriz de rotación   Vt=V^T

#hallar la diagonal de sigma
D=np.diag(sigma)
print(f'Diagonal de sigma: \n{D}\n')

#Descomposición de la matriz A
#A=U*D*V^T
A=np.dot(U,np.dot(D,V))
print(f'A: \n{A}\n')