my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    my_list.remove(myVal)
    return my_list

print(RemoveValue(27))
print(RemoveValue(27))


def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list?")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))


"""El código proporcionado contiene dos definiciones de la función `RemoveValue`, y cada una de ellas realiza una acción
diferente en función de la existencia del valor en la lista `my_list`.

1. **Primera definición de `RemoveValue`**:
   - Esta función toma un valor `myVal` como argumento y utiliza el método `remove` de la lista para eliminar la primera
   aparición de ese valor en `my_list`.
   - La primera llamada a la función `RemoveValue` pasa `27` como argumento y elimina el `27` de la lista `my_list`.
   Luego, imprime la lista resultante.
   - La segunda llamada a la función `RemoveValue` también pasa `27`, pero dado que el `27` ya se ha eliminado en la
   llamada anterior, generará un error ya que `27` no se encuentra en la lista.

2. **Segunda definición de `RemoveValue`**:
   - Esta función también toma un valor `myVal` como argumento y realiza una verificación antes de eliminar el valor de `my_list`.
   - Verifica si `myVal` está presente en `my_list`. Si no se encuentra, genera una excepción `ValueError` con el mensaje
   "Value must be in the given list?".
   - Si `myVal` está presente en `my_list`, lo elimina utilizando `my_list.remove(myVal)` y luego devuelve la lista modificada.
   - La tercera llamada a la función `RemoveValue` pasa `27` como argumento, y dado que `27` ya se ha eliminado en la
   primera llamada, generará un error porque no se encuentra en la lista.

En resumen, ambas definiciones de la función `RemoveValue` intentan eliminar un valor de la lista `my_list`, pero la
segunda definición verifica primero si el valor está presente en la lista y genera un error si no lo encuentra. Esto
significa que la segunda definición es más robusta en términos de manejo de errores y evita eliminar valores que no existen en la lista."""
