#Ejercicio 3
#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
#Calcular después la suma, resta, multiplicación y división. 
#Utilizar un método para cada una e imprimir los resultados obtenidos.
#Llamar a la clase Calculadora.

class Calculadora:
    #constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero no permitida."

numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
calculadora = Calculadora(numero1, numero2)
operacion = input("Ingrese la operación a realizar (suma, resta, multiplicacion, division): ").lower()
if operacion == "suma":
    resultado = calculadora.suma()  
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif operacion == "resta":      
    resultado = calculadora.resta()
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
elif operacion == "multiplicacion":
    resultado = calculadora.multiplicacion()
    print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
elif operacion == "division":
    resultado = calculadora.division()
    print(f"La división de {numero1} y {numero2} es: {resultado}")
else:
    print("Operación no válida.")
