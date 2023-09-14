"""Desglose de la función:
words = sentence.split(): Esta línea divide la cadena sentence en una lista de palabras utilizando el método split(),
que divide la cadena en cada espacio en blanco.

Luego, la condición if n <= len(words): verifica si el valor de n no es más grande que el número de palabras en la lista words.

Si ambas condiciones son verdaderas, la función devuelve la palabra en la posición n - 1 de la lista words, ya que las
listas en Python se indexan desde 0.

Los ejemplos print(get_word(...)) al final llaman a la función con diferentes oraciones y valores de n, y muestran las
palabras resultantes según lo descrito anteriormente.

En resumen, la función toma una oración y un número n, divide la oración en palabras y devuelve la palabra en la posición
n - 1 si se cumplen ciertas condiciones, como se muestra en los ejemplos proporcionados."""

def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()  # Split the sentence into a list of words
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]  # Return the word at index n - 1
    return ""

print(get_word("This is a lesson about lists", 4)) # Debería imprimir: lesson
print(get_word("This is a lesson about lists", -4)) # Nada
print(get_word("Now we are cooking!", 1)) # Debería imprimir: Now
print(get_word("Now we are cooking!", 5)) # Nada


