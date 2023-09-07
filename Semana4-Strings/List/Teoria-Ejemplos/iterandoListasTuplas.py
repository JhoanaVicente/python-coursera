animals = ["Lion", "Zebra", "Dolphin", "Monkey"] #Iteramos sobre una lista de cadenas
chars = 0 #Los caracteres comienzan con 0
for animal in animals: #Comenzamos un bucle
    chars += len(animal)
    print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))


#Funcion de enumerar
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


#Definimos una funcion para que reciba una lista de personas
def full_emails(people): #'People' es una lista de tuplas
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"),
                   ("shay@example.com", "Shay Brandt")]))



"""Example:
En este código, utilizamos la función enumerate() para obtener tanto el índice como el valor de cada elemento en la lista
elements. Luego, utilizamos una comprensión de lista para crear una nueva lista que contenga solo los elementos en las
posiciones impares (índices pares) dentro de la lista original."""

def skip_elements(elements):
    return [element for index, element in enumerate(elements) if index % 2 == 0]

"""Aquí, estamos usando una comprensión de lista para iterar sobre las tuplas generadas por enumerate(elements).
Para cada tupla, estamos seleccionando solo el element (el valor en la lista original) si el index (el índice en la
lista original) es par, es decir, si index % 2 == 0."""

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


"""Iterando sobre listas usando ENUMERAR:
Cuando cubrimos los bucles for , mostramos el ejemplo de iteración sobre una lista. Esto le permite iterar sobre cada
elemento de la lista, exponiendo el elemento al bucle for como una variable. Pero ¿qué pasa si quieres acceder a los
elementos de una lista, junto con el índice del elemento en cuestión? Puedes hacer esto usando la función enumerar().
La función enumerate() toma una lista como parámetro y devuelve una tupla para cada elemento de la lista. El primer
valor de la tupla es el índice y el segundo valor es el elemento mismo."""
