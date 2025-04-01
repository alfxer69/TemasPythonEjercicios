import requests

#enviar solicitud get
url='https://repositorio.ues.edu.sv/items/012f5eb8-59b5-4006-a138-5652d03baa58'
try:
    response=requests.get(url)
except:
    print('Error al abrir la pagina')
else:
    if response.status_code==200:
        print('Contenido de la solicitud get: ')
        print(response.content)
    else:
        print('error en la solicitud',response.status_code)
        
