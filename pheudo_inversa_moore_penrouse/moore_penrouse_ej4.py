
import tensorflow as tf

# Definir la matriz A_p (3x2)
A_p = tf.Variable([[-1., 2.], [3., -2.], [5., 6.]], dtype=tf.float32)
print("Matriz A_p:")


# Paso 1: Descomposición SVD con TensorFlow
D,U,VT = tf.linalg.svd(A_p)
# Nota: tf.linalg.svd devuelve s (valores singales), U y V (V^T ya está transpuesta)
print("\nValores singulares (D):")
print(D)
print("\nMatriz U:")
print(U)
print("\nMatriz V (V^T en la fórmula clásica):")
print(VT)

D = tf.linalg.diag(D)  # Sigma^+ es una matriz diagonal k x k (2x2 en este caso)
print(f'Matriz D \n{D}')

D_inv=tf.linalg.inv(D)  # Inversa de la matriz diagonal de valores singulares 
print(f'\nInversa de la matriz inversa de valores singulares:\n{D_inv}')

tensor = tf.Variable([[0, 0.]])
D_inv_plus=tf.concat((D_inv, tf.transpose(tensor)), axis=1)  # Matriz de D_plus (2x3)
print(f'\n Valor de D_plus:\n{D_inv_plus}')

print('-'*50)
A_p_plus = tf.matmul(VT,tf.matmul(D_inv_plus, tf.transpose(U)))  # Matriz pseudo-inversa de A_p
print(f'\nMatriz pseudo-inversa de A_p:\n{A_p_plus}')

print('-'*50)
A_p_plus = tf.linalg.pinv(A_p)  # Matriz pseudo-inversa de A_p usando la función pinv
print(f'\nMatriz pseudo-inversa de A_p usando la función pinv:\n{A_p_plus}')




#