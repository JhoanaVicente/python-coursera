import re
def compare_strings(string1, string2):
  #Convert both strings to lowercase
  #and remove leading and trailing blanks
  string1 = string1.lower().strip()
  string2 = string2.lower().strip()

  #Ignore punctuation
  punctuation = r"[.?!,:;'-]"
  string1 = re.sub(punctuation, r"", string1)
  string2 = re.sub(punctuation, r"", string2)

  #DEBUG CODE GOES HERE
  print(f"Processed string1: {string1}")
  print(f"Processed string2: {string2}")

  return string1 == string2

print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False


"""La función `compare_strings` es una función de Python que se encarga de comparar dos cadenas de texto. Lo que hace esta
función es realizar una serie de transformaciones en ambas cadenas para normalizarlas y luego las compara para determinar si son iguales o no.

Aquí está lo que hace paso a paso:

1. Convierte ambas cadenas en minúsculas utilizando el método `lower()`. Esto se hace para que la comparación no distinga
entre mayúsculas y minúsculas. Por ejemplo, "Hello" y "hello" se considerarán iguales después de esta transformación.

2. Utiliza `strip()` para eliminar cualquier espacio en blanco al principio o al final de las cadenas. Esto garantiza
que no haya espacios en blanco innecesarios que puedan afectar la comparación.

3. Luego, se define una variable llamada `punctuation` que contiene una expresión regular. Esta expresión regular busca
ciertos caracteres de puntuación, como puntos, signos de exclamación, comas, dos puntos y apóstrofes. La expresión
regular `[.?!,:;'-]` se utiliza para coincidir con cualquiera de estos caracteres.

4. Usando `re.sub()`, se reemplazan todos los caracteres de puntuación en ambas cadenas con una cadena vacía
(es decir, se eliminan). Esto asegura que la comparación no se vea afectada por la presencia o ausencia de estos caracteres de puntuación.

5. Finalmente, se realiza la comparación de las dos cadenas resultantes después de todas las transformaciones. Si son
iguales,la función devuelve `True`, de lo contrario, devuelve `False`.

El "DEBUG CODE GOES HERE" indica que el código para depuración se puede agregar en ese punto para imprimir los resultados
intermedios y ayudar a comprender cómo se están procesando las cadenas. En este caso, se utilizan dos declaraciones
`print()` para mostrar las cadenas procesadas `string1` y `string2`.

Luego, la función se prueba con varias parejas de cadenas y se imprime el resultado de la comparación. Si las cadenas
son iguales después de realizar todas las transformaciones y eliminar la puntuación, se imprime `True`, de lo contrario, se imprime `False`.

Este tipo de función es útil para comparar cadenas de texto en un escenario en el que se desea ignorar diferencias de
mayúsculas y minúsculas, así como la puntuación. En este caso, las cadenas "Have a Great Day!" y "Have a great day?" se
considerarían iguales, lo que es útil en muchas aplicaciones, como la verificación de la igualdad de cadenas de búsqueda
en un motor de búsqueda o en la corrección ortográfica."""
