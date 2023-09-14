"""Utilice la operación diccionario[clave] = valor para asociar un valor con una clave en un diccionario.
Itere sobre claves con múltiples valores de un diccionario, usando bucles for anidados y una declaración if , y el método Dictionary.items() .
Utilice el método diccionario[clave].append(valor) para agregar la clave, una cadena y la clave para cada elemento del diccionario."""

def invert_resource_dict(resource_dictionary):
    # Creamos un nuevo diccionario vacío llamado 'new_dictionary' para almacenar el resultado invertido.
    new_dictionary = {}

    # Iteramos a través de los elementos (pares clave-valor) del diccionario 'resource_dictionary'.
    for resource_group, resources in resource_dictionary.items():
        # En este bucle anidado, iteramos a través de la lista de recursos 'resources' para cada grupo.
        for resource in resources:
            # Verificamos si el recurso ya existe en 'new_dictionary'.
            if resource in new_dictionary:
                # Si el recurso ya existe, agregamos el grupo de recursos a la lista existente.
                new_dictionary[resource].append(resource_group)
            else:
                # Si el recurso no existe, creamos una nueva entrada con el recurso y su grupo de recursos.
                new_dictionary[resource] = [resource_group]

    # Devolvemos el nuevo diccionario invertido.
    return new_dictionary

# Llamamos a la función con un diccionario de ejemplo y mostramos el resultado.
print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
