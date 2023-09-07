multiples = []
for x in range (1, 11):
    multiples.append(x*7)

print(multiples)


#List Comprenhension: Crea nuevas listas basadas en secuencias o rangos
multiples = [x*7 for x in range(1, 11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0, 101) if x % 3 == 0]
print(z)


"""Example:
En este código, estamos utilizando una COMPRENSIÓN DE LISTA para generar una lista de números impares. Aquí está cómo funciona:
range(1, n + 1): Esto crea un rango de números desde 1 hasta n, incluyendo 1 pero excluyendo n + 1.
[x for x in range(1, n + 1) if x % 2 != 0]: Para cada número x en el rango generado, estamos seleccionando solo aquellos
números que son impares. Esto lo hacemos verificando si el residuo de la división de x entre 2 (x % 2) es diferente de 0.

Finalmente, la lista resultante contiene solo los números impares en el rango de 1 a n.
Así que, cuando llames a la función odd_numbers(n), te devolverá una lista de números impares desde 1 hasta n."""

def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
