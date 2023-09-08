class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()


# METODO QUE DEVUELVE UN VALOR
class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())


# ANOTHER EXAMPLE
class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7

fido = Dog()
fido.years = 3
print(fido.dog_years())
