def alphabetize_lists(list1, list2):
    new_list = []  # Inicializa una nueva lista vacía.
    combined_lists = list1 + list2  # Combina las dos listas.
    combined_lists.sort()  # Ordena las listas combinadas alfabéticamente.
    new_list = combined_lists  # Asigna las listas combinadas a "new_list".
    return new_list

Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]

print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Debería imprimir: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']


"""En el código completado:
new_list = []: Se inicializa una nueva lista vacía llamada new_list que se utilizará para almacenar el resultado.

combined_lists = list1 + list2: Se combinan las dos listas list1 y list2 utilizando el operador +. Esto crea una nueva
lista llamada combined_lists que contiene todos los elementos de ambas listas.

combined_lists.sort(): Se ordena la lista combinada combined_lists alfabéticamente utilizando el método sort().

new_list = combined_lists: Finalmente, se asigna la lista ordenada combined_lists a new_list.

La función devuelve new_list, que es la lista combinada y ordenada alfabéticamente.

Cuando se llama a alphabetize_lists(Aniyahs_list, Imanis_list), deberías obtener la salida deseada, que es la lista combinada y ordenada alfabéticamente."""
