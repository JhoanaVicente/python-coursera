"""En la programación orientada a objetos, el concepto de herencia le permite construir relaciones entre objetos, agrupando
conceptos similares y reduciendo la duplicación de código."""

class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.color)


"""En Python, usamos paréntesis en la declaración de clase para que la clase herede de la clase Fruit. Entonces, en este ejemplo,
le estamos indicando a nuestra computadora que tanto la clase Apple como la clase Grape heredan de la clase Fruit. Esto
significa que ambos tienen el mismo método constructor que establece los atributos de color y sabor."""
