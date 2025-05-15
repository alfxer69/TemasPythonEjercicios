from abc import ABC,abstractmethod

class ReportGenerator(ABC):
    
    @abstractmethod
    def generate(self,data):
        pass
    
class PDFGenerator(ReportGenerator):
    def generate(self, data):
        print(f'Generando Reporte PDF con los datos: {data}')
        return 'reporte.pdf'

class WordGenerador(ReportGenerator):
    def generate(self,data):
        print(f'Generando Reporte Word con los datos {data}')
        return 'reporte.doc'

class CSVGenerador(ReportGenerator):
    def generate(self,data):
        print(f'Generando reporte CSV {data}')
        return 'reporte.csv'

class HTMLGenerador(ReportGenerator):
    def generate(self,data):
        print(f'Generando Reporte HTML {data}')
        return 'reporte.html'

class GestorReporte:
    def __init__(self,reportegenerador:ReportGenerator):
        self.reportegenerador=reportegenerador
    
    def generate(self,data):
        return self.reportegenerador.generate(data)

#Ejemplos de Uso

pdf=PDFGenerator()
gestorpdf=GestorReporte(pdf)
gestorpdf.generate('Datos de PDF')

html=HTMLGenerador()
gestorhtml=GestorReporte(html)
gestorhtml.generate('datos html')


        