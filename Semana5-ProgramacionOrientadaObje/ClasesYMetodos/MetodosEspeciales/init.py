class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

jonagold = Apple("red", "sweet")
print(jonagold.color)




# EXAMPLE
class Person:
    def __init__(self, name): # INICIALIZAR EL ATRIBUTO 'NAME' / CREO INSTANCIA DE LA CLASE
        self.name = name  # Rellenamos el atributo 'name' con el valor proporcionado al crear la instancia.

    def greeting(self): # MÉTODO
        # Devolvemos una cadena que incluye el nombre de la Persona.
        return f"hi, my name is {self.name}"  # Utilizamos el atributo 'name' para construir el saludo.

# Crear una nueva instancia con un nombre de tu elección
some_person = Person("John")  # Aquí puedes reemplazar "John" con el nombre que desees.

# Llamar al método greeting
print(some_person.greeting())  # Imprimimos el saludo generado por el método greeting.

"""La letra "f" que aparece antes de una cadena de texto en Python se utiliza para crear una cadena formateada, y se conoce
como una cadena f (o cadena f-strings). Las cadenas f-strings son una característica de formateo de cadenas en Python que
permite insertar valores de variables dentro de una cadena de manera más legible y conveniente.
Cuando pones una "f" antes de una cadena (por ejemplo, `f"hi, my name is {self.name}"`), puedes incluir expresiones entre
llaves `{}` dentro de la cadena, y Python los evaluará y reemplazará con los valores reales correspondientes cuando se
ejecuta el programa. En este caso, `{self.name}` se reemplazará por el valor del atributo `name` del objeto `self`, que
es la instancia actual de la clase `Person`.
Usar f-strings es una forma eficiente y legible de construir cadenas que contienen valores de variables en Python, en
lugar de concatenar manualmente cadenas y variables con operadores `+`."""
