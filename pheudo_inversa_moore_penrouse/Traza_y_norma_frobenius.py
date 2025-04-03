#Hallaremos la traza de una matriz de 2D

import numpy as np 
import torch

A=np.array([[25,2],[5,4]])
print(f'A: \n{A}')
print(f'Traza de A: {np.trace(A)}')
print('-' * 50)
#Utilizamos Pytorch con a matriz A_p
#A_p es una matriz de 2D
A_p=torch.tensor([[-1,2],[3,-2],[5,7.]])
print(f'A_p: \n{A_p}')
print(f'Traza de A_p: {torch.trace(A_p)}')
print('-' * 50)
#hallaremos la norma de Frobenius de una matriz de 2D
Norma_Frobenius=torch.norm(A_p,p='fro')
print(f'Norma de Frobenius de A_p: {Norma_Frobenius}')
print('-' * 50)
#Hallaremos la norma de Frobenius con ||A||F=√Tr(AAT)
Norma_Frobenius_2=torch.sqrt(torch.trace(torch.matmul(A_p,A_p.T)))
print(f'Norma de Frobenius de A_p: {Norma_Frobenius_2}')
print('-' * 50)



