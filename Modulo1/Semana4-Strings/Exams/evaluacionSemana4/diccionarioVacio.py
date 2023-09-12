def setup_guests(guest_list):
    result = {}  # Inicializa un nuevo diccionario vacío.
    for guest in guest_list:  # Itera sobre los elementos en la lista de invitados.
        result[guest] = 0  # Agrega cada elemento de la lista al diccionario con valor inicial de 0.
    return result

guests = ["Adam", "Camila", "David", "Jamal", "Charley", "Titus", "Raj", "Noemi", "Sakira", "Chidi"]

print(setup_guests(guests))
# Debería imprimir {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}


"""En este código:
Se inicia un diccionario vacío llamado result.

Luego, se utiliza un bucle for para iterar a través de los elementos en la lista guest_list. En cada iteración, guest
representa el nombre de un invitado.

Dentro del bucle for, se agrega cada elemento guest al diccionario result como una clave con un valor inicial de 0.

Finalmente, la función setup_guests devuelve el diccionario result, que contiene los nombres de los invitados como claves
y un valor inicial de 0 para cada uno."""
