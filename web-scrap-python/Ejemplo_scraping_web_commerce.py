from bs4 import BeautifulSoup
import requests

# URL de la página a scrapear
url='https://listado.mercadolibre.com.pe/celulares-telefonos/celulares-smartphones/samsung/nuevo/#c_container_id=not_apply&c_id=%2Fsplinter%2Fcard-primary-withoutdiscount&c_element_order=1&c_campaign=samsung&c_label=%2Fsplinter%2Fcard-primary-withoutdiscount&c_uid=f4293dc7-0a6a-11f0-8b89-8f95e4da6094&c_element_id=f4293dc7-0a6a-11f0-8b89-8f95e4da6094&c_global_position=7&deal_print_id=f42dd1a0-0a6a-11f0-bfd4-3d42f269d3d9&c_tracking_id=f42dd1a0-0a6a-11f0-bfd4-3d42f269d3d9'

# Simular headers para evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Realizar la petición
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Verificar errores HTTP
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selectores actualizados (pueden cambiar, verifica en el HTML)
    productos = soup.find_all('li', class_='ui-search-layout__item shops__layout-item')  # Contenedor de cada producto
    i=0
    for producto in productos:
        i=i+1
        try:
            nombre = producto.find('h3', class_='poly-component__title-wrapper').text.strip()
            precio = producto.find('span', class_='andes-money-amount__fraction').text.strip()
            Calificacion=producto.find('span',class_='andes-visually-hidden',).text.strip()
            
            print(f"Item: {i}")
            print(f"Producto: {nombre}")
            print(f"Precio: S/. {precio}")
            print(f'{Calificacion}')
            print("-" * 50)
        except AttributeError as e:
            print(f"Error extrayendo datos de un producto: {e}")
            continue

except requests.exceptions.RequestException as e:
    print(f"Error al conectar con MercadoLibre: {e}")