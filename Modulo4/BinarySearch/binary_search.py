def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1


"""La función tiene dos parámetros: "list," que es la lista ordenada en la que se busca, y "key,"
que es el valor que estás tratando de encontrar en la lista.

La función retorna la posición del elemento "key" si lo encuentra en la lista, y retorna -1 si el elemento no está presente en la lista.

Se utilizan punteros "left" y "right" para rastrear el rango de elementos en la lista que se están considerando. Estos
punteros se actualizan en cada iteración del bucle while, lo que es una parte esencial del algoritmo de búsqueda binaria.

El bucle while continúa ejecutándose hasta que "left" sea mayor que "right," lo que garantiza que el algoritmo termine en algún momento.

En general, el código es correcto y representa una implementación funcional de la búsqueda binaria. Puedes usar esta función
para buscar elementos en una lista ordenada de manera eficiente. Ten en cuenta que la lista debe estar ordenada para que
la búsqueda binaria funcione correctamente."""
