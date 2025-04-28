#calcula la potencia de un numero con metodo de recursividad
def potencia_de_un_numero(a,b):
    if b==0:
        return 1
    else:
        return a*potencia_de_un_numero(a,b-1)

print(potencia_de_un_numero(2,6))
