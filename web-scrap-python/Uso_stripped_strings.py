from bs4 import BeautifulSoup

#Uso del comando Stripped para eliminar espacios en blanco en una cadena de texto

html = """
<div>
    <p>   Hola   </p>
    <p>  Mundo  </p>
    <p>  Exterior </p>
</div>
"""

soup=BeautifulSoup(html,'html.parser')
textos_limpios=list(soup.stripped_strings)
print(textos_limpios)

