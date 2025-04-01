#Ejemplo de uso de la pseudoinversa de Moore-Penrose
#Ejemplo 3: Matriz A_p de 3x2
#La matriz A_p es una matriz de 3 filas y 2 columnas
#La matriz A_p es una matriz rectangular, por lo que no tiene inversa
#Usando Pytorch

import torch    

A_p = torch.tensor([[-1, 2], [3, -2], [5, 6.]], dtype=torch.float32)
print(f'Matriz A_p: \n{A_p}')
print(f'\nDimensiones de A_p: {A_p.shape}')

U,D,VT = torch.svd(A_p) #Descomposición en valores singulares
print(f'\nDescomposición en valores singulares de A_p:\nU:\n{U}\nD:\n{D}\nVT:\n{VT}')

D = torch.diag(D) #Matriz diagonal de valores singulares
print(f'\nMatriz diagonal de valores singulares:\n{D}')

D_inv = torch.linalg.inv(D) #Inversa de la matriz diagonal de valores singulares
print(f'\nInversa de la matriz inversa de valores singulares:\n{D_inv}')

D_plus=torch.concatenate((D_inv,torch.tensor([[0,0]]).T),axis=1) #Matriz de Dplus
print(f'\n Valor de D_plus:\n{D_plus}')

print('-'*50)
A_p_plus=torch.matmul(VT.T,torch.matmul(D_plus,U.T)) #Matriz pseudo-inversa de A_p
print(f'\nMatriz pseudo-inversa de A_p:\n{A_p_plus}')

print('-'*50)
A_p_plus = torch.linalg.pinv(A_p) #Matriz pseudo-inversa de A_p usando la función pinv  
print(f'\nMatriz pseudo-inversa de A_p usando la función pinv:\n{A_p_plus}')



