class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    def __init__(self, name):
        super(). __init__(name)
        self.set_category("reptile")

my_turtle = Turtle("Turtle")
print(f"Name: {my_turtle.name}")
print(f"Category: {my_turtle.category}")


class Snake(Animal):
    def __init__(self, name):
        super().set_category("reptile")

my_snake = Snake ("Snake")
print(f"Name: {my_snake.name}")
print(f"Name: {my_snake.category}")

class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal_category in self.current_animals.values():
            if animal_category == category:
                result += 1
        return result
zoo = Zoo()
turtle = Turtle("Turtle")
snake = Snake("Snake")

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile"))

"""Primero, se define una clase base llamada `Animal`. Esta clase tiene dos atributos de clase, `name` (nombre) y `category`
(categoría), que inicialmente se establecen en cadenas vacías. Luego, la clase `Animal` tiene un constructor `__init__` que
toma un parámetro `name` y establece el atributo de instancia `self.name` con el valor proporcionado. También tiene un
método llamado `set_category` que establece el atributo `self.category` con la categoría que se pasa como argumento.

A continuación, se define la clase `Turtle` que hereda de la clase `Animal`. En su constructor, llama al constructor de
la clase base usando `super().__init__(name)` para configurar el nombre del animal y luego llama al método `set_category`
para establecer la categoría como "reptile". Luego, crea una instancia de `Turtle` llamada `my_turtle` y muestra su nombre y categoría.

Luego, se define la clase `Snake`, que también hereda de la clase `Animal`. En su constructor, llama al método `set_category`
para establecer la categoría como "reptile". Nuevamente, crea una instancia de `Snake` llamada `my_snake` y muestra su nombre y categoría.

Finalmente, se define la clase `Zoo`. Esta clase tiene un diccionario llamado `current_animals` que se utiliza para mantener
un seguimiento de los animales en el zoológico. Tiene dos métodos: `add_animal` para agregar un animal al zoológico y
`total_of_category` para contar cuántos animales de una categoría específica hay en el zoológico.

En el código final, se crea una instancia de `Zoo` llamada `zoo`, luego se crean instancias de `Turtle` y `Snake` llamadas
`turtle` y `snake`, respectivamente. Se agregan estos animales al zoológico usando el método `add_animal`, y finalmente
se imprime la cantidad de animales en la categoría "reptile" utilizando el método `total_of_category`."""


# Sobre SUPER:

"""Cuando se llama al constructor de la clase base utilizando super().__init__(name), estás llamando al constructor de la clase
padre (Animal en este caso) para asegurarte de que se realicen las inicializaciones necesarias definidas en la clase base
antes de realizar cualquier inicialización específica de la clase derivada (Turtle o Snake).

En el contexto de la herencia, es importante asegurarse de que la inicialización de la clase base se realice antes de realizar
cualquier operación específica de la clase derivada. Esto es especialmente importante cuando la clase base tiene un constructor
que establece atributos o realiza otras acciones importantes durante la inicialización."""


