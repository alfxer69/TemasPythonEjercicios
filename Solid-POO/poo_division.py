class Division:
    def dividir(self,numerador,denominador):
        try:
            return numerador/denominador
        except ZeroDivisionError:
            return 'Error no se puede divir por cero'

dividir1=Division()
print(dividir1.dividir(10,2))
print('\n')
dividir2=Division()
print(dividir2.dividir(15,0))
