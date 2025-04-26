def buscar_cantidad_producto(inventario,codigo_producto,inicio=0,fin=None):
    """
    Función recursiva que busca la cantidad de un producto en el inventario.
    :inventario: Lista de diccionarios que representan el inventario.
    :codigo_producto: Código del producto a buscar.
    :return: Cantidad del producto encontrado o 0 si no se encuentra.
    """
    if fin is None:
        fin = len(inventario)-1
    if inicio>fin:
        return 0
    
    medio=(inicio+fin)//2
    
    if inventario[medio]['codigo'] == codigo_producto:
        return inventario[medio]['cantidad']
    
    elif inventario[medio]['codigo'] > codigo_producto:
        return buscar_cantidad_producto(inventario, codigo_producto, inicio,medio-1)
    
    else:
        return buscar_cantidad_producto(inventario, codigo_producto, medio+1,fin)
    

inventario_productos = [
    {'codigo': '101','cantidad': 10},
    {'codigo': '204','cantidad': 5},
    {'codigo': '307','cantidad': 34},
    {'codigo': '409','cantidad': 2},
    {'codigo': '512','cantidad': 8},
    {'codigo': '614','cantidad': 15},
    {'codigo': '718','cantidad': 18},
    {'codigo': '820','cantidad': 3},
   
]

print(buscar_cantidad_producto(inventario_productos, '512'))


