"""Desglose de la función:
new_string = "" y reverse_string = "": Inicializan dos cadenas vacías para almacenar la versión sin espacios y en minúsculas
de la cadena original, y la versión invertida de esa cadena.

El bucle for letter in input_string: itera sobre cada letra en la cadena input_string.

if letter != " ":: Esta condición verifica si la letra no es un espacio.

Si no es un espacio, agrega la letra en minúsculas a la cadena new_string y agrega la letra invertida a la cadena reverse_string.
Después de recorrer todas las letras de la cadena, la función compara las cadenas new_string y reverse_string. Si son
iguales, esto significa que la cadena original es un palíndromo y devuelve True. De lo contrario, devuelve False.

Los ejemplos print(is_palindrome(...)) al final llaman a la función con diferentes cadenas y muestran si son palíndromos o no, según lo esperado."""

def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for letter in input_string:
        if letter != " ":
            new_string += letter.lower()
            reverse_string = letter.lower() + reverse_string
    if new_string == reverse_string:
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
