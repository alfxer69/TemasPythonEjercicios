#suma de numeros enteros con recursividad
#serie de numeros como 1+2+3+4+5+6+7+8+9+10....
def suma_numero_naturales(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+suma_numero_naturales(n-1)

print(f'Suma de numeros naturales {suma_numero_naturales(10)}')