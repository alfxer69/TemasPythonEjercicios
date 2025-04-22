'''Tienes a tu disposición un conjunto de discos numerados del 1 al N y tres torres
etiquetadas como A, B y C. La torre A contiene inicialmente todos los discos
apilados en orden descendente, desde el disco N en la parte inferior hasta el
disco 1 en la parte superior.
Tu tarea es implementar una solución recursiva para mover todos los discos
desde la torre A hasta la torre C, siguiendo las reglas clásicas de las Torres de
Hanoi:
1. Puedes mover un disco a una torre adyacente.
2. Solo puedes mover un disco a la cima de otra pila si esa pila está vacía o si
el disco superior es más grande que el disco que estás colocando.
Debes definir una función llamada torres_de_hanoi(n, origen, destino, auxiliar)
que, dado el número total de discos n y las torres de origen, destino y auxiliar,
imprima los pasos necesarios para lograr el movimiento de todos los discos
desde la torre A hasta la torre C.'''

def imprimir(n,origen,destino):
    print(f'el disco {n} va del origen {origen} a {destino}')

def h(n,origen,destino,auxiliar):
    if n==1:
        imprimir(n,origen,destino)
        return
    h((n-1),origen,auxiliar,destino)
    imprimir(n,origen,destino)
    h((n-1),auxiliar,destino,origen)
   
    
h(5,'origen','destino','auxiliar')
        
def factorial_numero(numero):
    if numero>1:
        numero=numero*factorial_numero(numero-1)
        
    return numero
print(factorial_numero(5))

def cuenta_atras(numero):
    numero-=1
    if numero>0:
        print(numero)
        cuenta_atras(numero)
        
cuenta_atras(10)