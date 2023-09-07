# This function accepts a string variable "data_field".
def count_words(data_field):
    split_data = data_field.split()
    return len(split_data)

# Call to the function
result = count_words("Catalog item 3523: Organic raw pumpkin seeds in shell")
# Should print 9
print(result)


"""data_field.split(): La cadena data_field se divide en palabras individuales utilizando el método split(). Esto crea
una lista en la que cada elemento de la lista es una palabra de la cadena original.
len(split_data): Después de dividir la cadena y almacenar las palabras en split_data, se usa len() para obtener
la longitud de la lista split_data. En este contexto, la longitud de la lista es igual al número de palabras en la cadena original.
Por lo tanto, len(split_data) devuelve el número de palabras en la cadena data_field."""
