class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.suma()
print(s.n1 + s.n2)


# Metodo de construccion __init__(seft) = (iniciar)
class Ropa:
    def __init__(self):
        self.marca = 'moda'
        self.talla = 'M'
        self.color = 'rojo'
camisa = Ropa()
print(camisa.talla)
print(camisa.marca)



class Calculadora:
    def __init__(self, n1, n2): # Para que sepa que se llama a las variables)
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2
operacion = Calculadora(10,3)
print(operacion.suma)


class Birds:
    def __init__(self):
        self.color = 'blue'
        self.number = '0'
    def count(self):
        self.numberOfBirds = '1'
total = Birds()
print(total.number)
