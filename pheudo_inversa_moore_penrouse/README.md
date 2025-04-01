Pseudoinversa de Moore-Penrose (A⁺)

Es una generalización de la matriz inversa para matrices no cuadradas o singulares (sin inversa normal).

Propiedades clave:

1. Si 
A es invertible → A+=(A)-1
2. Resuelve sistemas Ax=b
   
   . Si no hay solución → da la mejor aproximación (mínimos cuadrados).
   . Si hay infinitas soluciones → da la de norma mínima.
   
Cálculo (vía SVD):
Si A=UΣVT (descomposición SVD), entonces:
                A+ = VΣ+ UT
(donde Σ+ invierte los valores singulares no nulos).

Usos:
. Regresión lineal.

. Sistemas sobredeterminados/subdeterminados.

. Procesamiento de señales y machine learning.

Ejemplo rápido:

Si A=[[1,0],[0,0]] → A+=[[1,0][0,0]]

Es la "inversa universal" para matrices


 




