#Pseudoinversa de Moore-Penrose
#Ejemplo 1: Matriz A_p de 3x2
#La matriz A_p es una matriz de 3 filas y 2 columnas
#La matriz A_p es una matriz rectangular, por lo que no tiene inversa
   
import numpy as np

A_p=np.array([[-1,2],[3,-2],[5,7.]])
print(f'Matriz A_p: \n{A_p}')

U,D,VT=np.linalg.svd(A_p) #Descomposición en valores singulares
print(f'\nDescomposición en valores singulares de A_p:\nU:\n{U}\nD:\n{D}\nVT:\n{VT}')

D=np.diag(D) #Matriz diagonal de valores singulares
print(f'\nMatriz diagonal de valores singulares:\n{D}')

Dinv    =np.linalg.inv(D) #Inversa de la matriz diagonal de valores singulares
print(f'\nInversa de la matriz inversa de valores singulares:\n{Dinv}')

Dplus=np.concatenate((Dinv,np.array([[0,0]]).T),axis=1) #Matriz de Dplus
print(f'\n Valor de D:\n{Dplus}')

print('-'*50)
A_p_plus=VT.T@Dplus@U.T #Matriz pseudo-inversa de A_p
print(f'\nMatriz pseudo-inversa de A_p:\n{A_p_plus}')

print('-'*50)
A_p_plus=np.linalg.pinv(A_p) #Matriz pseudo-inversa de A_p usando la función pinv
print(f'\nMatriz pseudo-inversa de A_p usando la función pinv:\n{A_p_plus}')    