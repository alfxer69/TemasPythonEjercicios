class Paginas:
    
    def getPaginas(self):
        return 'mas de 500 hojas'

class Libro:
    
    def __init__(self,nombre,autor,paginaslib):
        self._nombre=nombre
        self._autor=autor
        self._paginaslib=paginaslib
    
    def getNombre(self):
        return self._nombre
    
    def getAutor(self):
        return self._autor
    
    def getPaginasLibro(self):
        return self._paginaslib.getPaginas()

class LibrosPrinter:
    def __init__(self,libros):
        self._libros=libros
     
    def printInfo(self):
        print(
            f'Libro: {self._libros.getNombre()} Autor: {self._libros.getAutor()} Paginas: {self._libros.getPaginasLibro()}'
            )

if __name__=='__main__':
    paginas=Paginas()
    libro=Libro(nombre='Los Perros',autor='MVLL',paginaslib=paginas)  
    impresion=LibrosPrinter(libros=libro)
    impresion.printInfo()


        