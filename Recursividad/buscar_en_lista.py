#Buscar un elemento de una lista de forma recursiva
# La función buscar_en_lista toma un elemento y una lista como entrada y devuelve True si el elemento se 
# encuentra en la lista, de lo contrario devuelve False.

def buscar_en_lista(lista,elemento):
    """
    Función recursiva que busca un elemento en una lista.
    :param elemento: Elemento a buscar.
    :param lista: Lista en la que se busca el elemento.
    :return: True si el elemento se encuentra en la lista, False de lo contrario.
    """
    if not lista:
        return False
    elif lista[0] == elemento:
        return True
    return buscar_en_lista(lista[1:],elemento)

lista=[3,5,7,8,9,10]
elemento=8

if buscar_en_lista(lista,elemento):
    print(f'El elemento {elemento} se encuentra en la lista.')
else:
    print(f'El elemento {elemento} no se encuentra en la lista.')

