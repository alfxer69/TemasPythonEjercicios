class Impresoras:
    def velocidad_de_impresion(self):
        pass

class ImpresorasLaser(Impresoras):
    def velocidad_de_impresion(self):
        pass

class ImpresorasInyeccionTinta(Impresoras):
    def velocidad_de_impresion(self):
        pass

class ImpresorasTermicas(Impresoras):
    def velocidad_de_impresion(self):
        pass

class ImpresorasMatriciales(Impresoras):
    def velocidad_de_impresion(self):
        pass

#impresoras laser
class ImpresorasHP(ImpresorasLaser):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora HP {self.modelo} imprime a {paginas_por_minuto} ppm')

class ImpresorasCanon(ImpresorasLaser):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Canon {self.modelo} imprime a {paginas_por_minuto} ppm')

class ImpresorasBrother(ImpresorasLaser):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Brother {self.modelo} imprime a {paginas_por_minuto} ppm')

class ImpresorasXerox(ImpresorasLaser):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Xerox {self.modelo} imprime a {paginas_por_minuto} ppm')

class ImpresorasLexmark(ImpresorasLaser):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Lexmark {self.modelo} imprime a {paginas_por_minuto} ppm')

class ImpresorasRicoh(ImpresorasLaser):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Ricoh {self.modelo} imprime a {paginas_por_minuto} ppm')

#impresoras de inyeccion de tinta
class ImpresorasEpson(ImpresorasInyeccionTinta):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Epson {self.modelo} imprime a {paginas_por_minuto} ppm')

class ImpresorasCanon(ImpresorasInyeccionTinta):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Canon {self.modelo} imprime a {paginas_por_minuto} ppm')

class impresorasHP(ImpresorasInyeccionTinta):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora HP {self.modelo} imprime a {paginas_por_minuto} ppm')

#impresoras termicas
class ImpresorasZebra(ImpresorasTermicas):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Zebra {self.modelo} imprime a {paginas_por_minuto} lpm')

class ImpresorasEpson(ImpresorasTermicas):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Epson {self.modelo} imprime a {paginas_por_minuto} lpm')

class ImpresorasBixolon(ImpresorasTermicas):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Bixolon {self.modelo} imprime a {paginas_por_minuto} lpm')

#impresoras matriciales
class ImpresorasEpson(ImpresorasMatriciales):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Epson {self.modelo} imprime a {paginas_por_minuto} pps')

class ImpresorasOkidata(ImpresorasMatriciales):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Okidata {self.modelo} imprime a {paginas_por_minuto} pps')

class ImpresorasPanasonic(ImpresorasMatriciales):
    def __init__(self, modelo):
        self.modelo = modelo

    def velocidad_de_impresion(self, paginas_por_minuto):
        print(f'La impresora Panasonic {self.modelo} imprime a {paginas_por_minuto} pps')
        
def velocidad_impresion_laser(laser: ImpresorasLaser, paginas_por_minuto):
    laser.velocidad_de_impresion(paginas_por_minuto)

def velocidad_impresion_inyeccion(inyeccion: ImpresorasInyeccionTinta, paginas_por_minuto):
    inyeccion.velocidad_de_impresion(paginas_por_minuto)

def velocidad_impresion_termica(termica: ImpresorasTermicas, paginas_por_minuto):
    termica.velocidad_de_impresion(paginas_por_minuto)

def velocidad_impresion_matricial(matricial: ImpresorasMatriciales, paginas_por_minuto):
    matricial.velocidad_de_impresion(paginas_por_minuto)

#Ejemplo de uso
impresora_hp = ImpresorasHP('LaserJet Pro')
velocidad_impresion_laser(impresora_hp, 30)

impresora_canon = ImpresorasCanon('PIXMA')
velocidad_impresion_inyeccion(impresora_canon, 15)

impresora_bixolon = ImpresorasBixolon('SRP-350III')
velocidad_impresion_termica(impresora_bixolon, 50)

impresora_okidata = ImpresorasOkidata('Microline 320 Turbo')
velocidad_impresion_matricial(impresora_okidata, 10)


