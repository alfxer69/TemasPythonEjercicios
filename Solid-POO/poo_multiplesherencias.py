class A:
    def metodo_a(self):
        return 'Metodo A'

class B:
    def metodo_b(self):
        return 'Metodo B'

class C(A,B):
    def metodo_c(self):
        return 'Metodo C'
    
objeto_c=C()

print(objeto_c.metodo_a())
print(objeto_c.metodo_b())
print(objeto_c.metodo_c())
    