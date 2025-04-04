class Empleados:
    numero_empleados = 0 #atributo de clase
    #Creacion del constructor
    #nombre,cargo y salario son atributos de instancia
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleados.numero_empleados +=(
            1
            ) #incrementa el contador de empleados
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, trabajo como {self.cargo}")
    
    def aumentar_salario(self,porcentaje):
        self.salario *= (1 + porcentaje / 100)
        print(f"Mi nuevo salario de {self.nombre} es {self.salario}")
    
    @classmethod
    def desde_string(cls,datos_empleado):#metodo de una clase
        nombre,cargo,salario=datos_empleado.split(',')
        return cls(nombre,cargo,float(salario))
    
    @staticmethod
    def es_feriado(dia):
        feriados=[1,10,27]
        return dia in feriados #verifica si el dia es feriado

#instanciar una clase -- crear objetos
empleado1=Empleados("Juan Perez","Gerente",5000)
empleado2=Empleados("Maria Lopez","Analista",3000)

empleado1.presentarse()
empleado2.presentarse()
#utilizar metodo de clase
empleado3=Empleados.desde_string("Pedro Garcia,Desarrollador,4000")
empleado4=Empleados('Adamari Lopez','contadora',2500)

print('')
empleado1.aumentar_salario(10)
empleado2.aumentar_salario(5)
print(f'El dia 1 es feriado? {Empleados.es_feriado(1)}')
print(f'El dia 2 es feriado? {Empleados.es_feriado(2)}')

print(f"El numero de empleados es {Empleados.numero_empleados}")
