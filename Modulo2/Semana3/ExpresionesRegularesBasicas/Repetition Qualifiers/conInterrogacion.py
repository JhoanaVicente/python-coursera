import re

print(re.search(r"p?each", "To each their own"))

print(re.search(r"p?each", "I like peaches"))

"""El código que has proporcionado utiliza expresiones regulares para buscar el patrón "p?each" en cadenas de texto. Aquí
tienes una explicación de lo que significa este patrón y cómo se aplica a las cadenas de texto que has proporcionado:

1. `print(re.search(r"p?each", "To each their own"))`: En esta línea, se busca el patrón "p?each" en la cadena "To each their own".
El patrón "p?each" se interpreta de la siguiente manera:
   - `p?`: Significa que la letra "p" es opcional, es decir, puede aparecer cero o una vez.
   - `each`: Busca la cadena "each" literalmente.

   En "To each their own", el patrón "p?each" coincide con la palabra "each", ya que la "p" es opcional y no está presente
en la cadena. El resultado será un objeto `Match` que indica la posición donde se encontró la coincidencia.

2. `print(re.search(r"p?each", "I like peaches"))`: En este caso, se busca el mismo patrón "p?each" en la cadena
"I like peaches". Aquí, el patrón coincide con la palabra "peach" porque la "p" está presente en la cadena, pero es opcional
según la expresión regular. El resultado será un objeto `Match` que indica la posición donde se encontró la coincidencia.

En resumen, este código utiliza una expresión regular que busca la cadena "each" con la letra "p" opcional antes de ella
en las cadenas de texto proporcionadas. Dependiendo de la cadena de entrada, se encontrarán o no coincidencias con este patrón."""
