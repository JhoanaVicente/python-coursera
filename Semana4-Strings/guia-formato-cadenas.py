"""Verifica si una cadena dada es un "espejo" en el sentido de que se lee igual hacia adelante y hacia atrás, ignorando
los espacios y la puntuación, y considerando las letras en minúsculas y mayúsculas como equivalentes. Aquí te explico cómo funciona la función:

1. `forwards = ""` y `backwards = ""`: Estas variables se utilizan para almacenar los caracteres de la cadena original (`my_string`)
en orden directo y en orden inverso respectivamente.

2. El bucle `for character in my_string:` itera sobre cada carácter en la cadena `my_string`.

3. `if character.isalpha():`: Esta condición verifica si el carácter es una letra (alfabético).
   - Si es una letra, se agrega al final de la cadena `forwards`.
   - Se agrega al principio de la cadena `backwards`.

4. Después de recorrer todos los caracteres de `my_string`, la función compara las cadenas `forwards` y `backwards` en
minúsculas usando `.lower()`. Si son iguales, esto significa que la cadena original es un espejo y se devuelve `True`.
De lo contrario, se devuelve `False`.

5. Finalmente, se imprimen los resultados para tres ejemplos diferentes utilizando la función `mirrored_string`.

En resumen, la función busca caracteres alfabéticos en la cadena, los organiza en el orden directo e inverso, y luego verifica
si estos dos ordenamientos son iguales al considerar solo las letras y sin importar mayúsculas y minúsculas."""

def mirrored_string(my_string):
    forwards = ""
    backwards = ""

    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards = character + backwards
    if forwards.lower() == backwards.lower():
        return True
    return False

print(mirrored_string("12 Noon")) # Should be True
print(mirrored_string("Was it a car or cat I saw")) # Should be False
print(mirrored_string("'eve, Madam Eve")) # Should be True
