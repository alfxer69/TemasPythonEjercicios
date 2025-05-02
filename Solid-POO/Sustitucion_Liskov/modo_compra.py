class CompraLibro:
    def proceso_compra(self):
        pass

class CompraLibroenLinea(CompraLibro):
    def proceso_compra(self):
        pass 

class CompraLibroFisico(CompraLibro):
    def proceso_compra(self):
        pass

#Compra libro en linea

class CompraEbook(CompraLibroenLinea):
    def __init__(self,autor):
        self.autor=autor
    
    def proceso_compra(self,libro):
        print(f'El libro {libro} del autor {self.autor} es un ebook')

class CompraAudiolibro(CompraLibroenLinea):
    def __init__(self,autor):
        self.autor=autor
    
    def proceso_compra(self,libro):
        print(f'El libro {libro} del autor {self.autor} es un audiolibro')

class CompraLibroDigital(CompraLibroenLinea):
    def __init__(self,autor):
        self.autor=autor
    
    def proceso_compra(self,libro):
        print(f'El libro {libro} del autor {self.autor} es un libro digital')

#Compra libro fisico

class CompraLibroTapaDura(CompraLibroFisico):
    def __init__(self,autor):
        self.autor=autor
    
    def proceso_compra(self,libro):
        print(f'El libro {libro} del autor {self.autor} es un libro de tapa dura')

def proceso_compra_en_linea(linea:CompraLibroenLinea, libro):
    linea.proceso_compra(libro)

def proceso_compra_fisico(fisico:CompraLibroFisico, libro):
    fisico.proceso_compra(libro)

#Ejemplo de uso
ebook=CompraEbook('Gabriel Garcia Marquez')
proceso_compra_en_linea(ebook,'Cien años de soledad')

librotapadura=CompraLibroTapaDura('Mario Vargas Llosa')
proceso_compra_fisico(librotapadura,'La ciudad y los perros')





