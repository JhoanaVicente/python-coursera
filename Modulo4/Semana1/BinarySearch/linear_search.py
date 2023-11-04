def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

""" Toma dos argumentos: list, que es la lista en la que se busca, y key, que es el valor que estás tratando de encontrar.

Itera a través de la lista utilizando un bucle for y la función enumerate. La variable i almacena el índice actual y item almacena el valor actual.

Compara cada elemento con la clave (key) y si encuentra una coincidencia, retorna el índice (i) en el que se encontró el elemento.

Si el bucle termina sin encontrar una coincidencia, lo que significa que la clave no está en la lista, la función retorna -1.

La función es válida y cumple su propósito. Puedes usarla para buscar elementos en una lista. Si deseas verificar su
funcionamiento, puedes crear una lista y llamar a la función con diferentes valores de clave para ver si devuelve los resultados esperados."""
