#Regresion Lineal con Pheudo-inversa de Moore Penrouse
#En los problemas de regresión, normalmente tenemos muchos más casos (n, o filas de X) 
#que características que predecir (columnas de X). Resolvamos un ejemplo en miniatura de
#tal situación de sobredeterminación.
#Tenemos ocho puntos de datos (n = 8):

import numpy as np
import matplotlib.pyplot as plt


x1 = [0, 1, 2, 3, 4, 5, 6, 7.] # E.g.: Dosage of drug for treating Alzheimer's disease
y = [1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37] # E.g.: Patient's "forgetfulness score"

#El objetivo es encontrar la mejor línea que se ajuste a estos datos.
#La forma estándar de resolver este problema es usar la pseudo-inversa de Moore-Penrose

title = 'Ensayo Clínico'
xlabel = 'Dosis del Fármaco (mL)'
ylabel = 'Olvidos del Paciente (puntos)'

fig,ax=plt.subplots()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.grid()
plt.plot(x1, y, 'bo', label='Datos de Pacientes')
plt.legend()
plt.show()

#Aunque parece que sólo hay un predictor (x1), nuestro modelo requiere un segundo (llamémoslo x0)
#para permitir una intersección y. Sin esta segunda variable, la línea que ajustamos al gráfico
#tendría que pasar por el origen (0, 0). La intersección y es constante en todos los puntos, 
#por lo que podemos establecerla igual a 1 en todos los puntos:
print('-' * 50)
x0=np.ones(8)
print(f'x0: {x0}')
#x0 es un vector de unos, que representa la intersección y.
#x1 es el vector de datos de entrada (dosis del fármaco).
#x0 y x1 son los vectores de datos de entrada que se utilizarán para crear la matriz X. 
#La matriz X contendrá los datos de entrada para el modelo de regresión lineal.

#Concatenar x0 y x1 en una matriz X
print('-' * 50)
print('Concatenando x0 y x1 en una matriz X:')
X = np.column_stack((x0, x1))
#tambien puedes usar concatenate:
#X=np.concatenate((np.matrix(x0).T,np.matrix(x1).T),axis=1)
print(f'X: {X}')

#Por las diapositivas, sabemos que podemos calcular los pesos w mediante la
#ecuación w=X+y:
print('-' * 50)
print('Calculando los pesos w mediante la ecuación w=X+y:')
w=np.dot(np.linalg.pinv(X), y)
print(f'w: {w}')
#La matriz pseudo-inversa de X se calcula utilizando la función pinv de numpy.  
print('-' * 50)

b=np.asarray(w).reshape(-1)[0]
print(f'b: {b}')
print('-' * 50)

m=np.asarray(w).reshape(-1)[1]
print(f'm: {m}')
print('-' * 50)

#Con los pesos podemos trazar la recta para confirmar que se ajusta a los puntos:
print('Trazando la recta de regresión:')

fig,ax=plt.subplots()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.grid()
#plt.plot(x1, y, 'bo', label='Datos de Pacientes')

ax.scatter(x1, y, color='red', label='Datos de Pacientes')
x_min, x_max = ax.get_xlim()
y_at_x_min = m * x_min + b
y_at_x_max = m * x_max + b

ax.set_xlim(x_min,x_max)
ax.plot([x_min,x_max],[y_at_x_min,y_at_x_max],'g-', label='Recta de Regresión')
plt.legend()
plt.show()