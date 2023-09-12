def endangered_animals(animal_dict):
    result = ""

    # Completar el bucle for para iterar a través de los elementos clave y valor en el diccionario.
    for animal, population in animal_dict.items():

        # Utilizar un método de cadena para formatear la cadena requerida.
        result += animal + "\n"
    return result

print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Debería imprimir:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger


"""El bucle for itera a través de los elementos clave y valor en el diccionario animal_dict utilizando el método items().
En cada iteración, animal representa el nombre del animal y population representa la población de ese animal.

Usamos la operación de concatenación (+) para agregar el nombre del animal (animal) a la cadena result, seguido por "\n"
para agregar un salto de línea después de cada nombre de animal. Esto asegura que cada nombre de animal se imprima en una
línea separada.

La función endangered_animals devuelve la cadena result, que contiene los nombres de los animales en líneas separadas,
como se muestra en los comentarios."""
