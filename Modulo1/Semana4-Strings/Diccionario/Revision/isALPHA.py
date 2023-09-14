def sales_prices(item_and_price):
    item = ""
    price = ""

    item_or_price = item_and_price.split()
    for x in item_or_price:
        if x.isalpha():
            item += x + " "
        else:
            price = x
    item = item.strip()
    return "{} are on sale for ${}".format(item, price)

# Call to the function
print(sales_prices("Winter fleece jackets 49.99"))
# Should print "Winter fleece jackets are on sale for $49.99"



"""1. Se define la función `sales_prices` con un solo parámetro, `item_and_price`.

2. Se inicializan dos variables vacías, `item` y `price`, que se utilizarán para almacenar el nombre del artículo y su precio, respectivamente.

3. Se divide la cadena `item_and_price` en palabras utilizando el método `split()`. Esto crea una lista llamada `item_or_price`
que contiene las palabras individuales de la cadena.

4. Se itera a través de las palabras en `item_or_price` utilizando un bucle `for` y una variable `x` para representar cada palabra.

5. Dentro del bucle, se verifica si `x` es una palabra que contiene solo letras (es decir, si es el nombre del artículo).
Esto se hace utilizando el método `isalpha()`. Si `x` contiene solo letras, se agrega a la variable `item`, seguido de un espacio en blanco.

6. Si `x` no es una palabra que contenga solo letras, se asume que es el precio del artículo y se asigna a la variable `price`.

7. Después de que se completa el bucle, se elimina cualquier espacio en blanco adicional alrededor de la variable `item` utilizando `strip()`.

8. Finalmente, se devuelve una cadena formateada que combina el nombre del artículo y el precio utilizando placeholders
`{}` y `.format()`. La cadena resultante indica que el artículo está en oferta y muestra su nombre y precio.

9. Se llama a la función `sales_prices` con el argumento `"Winter fleece jackets 49.99"` y se imprime el resultado.

La llamada a la función con `"Winter fleece jackets 49.99"` imprimirá: "Winter fleece jackets are on sale for $49.99", como se espera."""
