"""Concatene un valor, una cadena y la clave para cada elemento del diccionario y agréguelo al final de una nueva lista [] usando el método   list.append(x) .
Itere sobre claves con múltiples valores de un diccionario usando bucles for anidados con el método Dictionary.items() ."""

# This function receives a dictionary, which contains common employee
# last names as keys, and a list of employee first names as values.
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the
# values ["Maria", "Hugo", "Lucia"] should be converted to a list
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].

def list_full_names(employee_dictionary):
    # Creamos una lista vacía llamada 'full_names' para almacenar los nombres completos.
    full_names = []

    # Iteramos a través de los elementos (pares clave-valor) del diccionario 'employee_dictionary'.
    for last_name, first_names in employee_dictionary.items():
        # En este bucle anidado, iteramos a través de la lista de nombres 'first_names'.
        for first_name in first_names:
            # Combinamos el 'first_name' actual con el 'last_name' y lo agregamos a 'full_names'.
            full_names.append(first_name + " " + last_name)

    # Devolvemos la lista de nombres completos.
    return full_names

# Llamamos a la función con un diccionario de ejemplo y mostramos el resultado.
print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))

