#Ejercicio que hace uso de la recursividad para invertir una cadena.
# La función invertir_cadena toma una cadena como entrada y devuelve la cadena invertida.
# La función utiliza la recursividad para invertir la cadena, tomando el primer carácter y llamando a sí misma con el resto de la cadena.
def invertir_cadena(cadena):
    """
    Función recursiva que invierte una cadena.
    :param cadena: Cadena de texto a invertir.
    :return: Cadena invertida.
    """
    if len(cadena) == 1:
        return cadena
    else:
        return invertir_cadena(cadena[1:])+ cadena[0]
    
input_cadena = input("Ingrese una cadena: ")
cadena_invertida = invertir_cadena(input_cadena)
print(f'Cadena invertida: {cadena_invertida}')
