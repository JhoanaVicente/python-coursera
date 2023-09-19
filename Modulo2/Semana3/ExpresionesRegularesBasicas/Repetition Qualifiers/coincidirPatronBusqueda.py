import re

print(re.search(r"o+l+", "goldfish"))

print(re.search(r"o+l+", "woolly"))

print(re.search(r"o+l+", "boil"))

"""El código que has proporcionado utiliza expresiones regulares para buscar un patrón en cadenas de texto. En este caso,
el patrón que se busca es "o+l+". Aquí tienes una explicación de lo que significa este patrón y cómo se aplica a las
cadenas de texto que has proporcionado:

1. `print(re.search(r"o+l+", "goldfish"))`: Esta línea busca el patrón "o+l+" en la cadena de texto "goldfish". El patrón
"o+l+" se interpreta de la siguiente manera:
   - `o+`: Busca una o más ocurrencias de la letra "o".
   - `l+`: Busca una o más ocurrencias de la letra "l".

   En "goldfish", el patrón "o+l+" coincide con "ol" en "gold". El resultado será un objeto `Match` que indica la posición
donde se encontró la coincidencia.

2. `print(re.search(r"o+l+", "woolly"))`: En este caso, se busca el mismo patrón "o+l+" en la cadena "woolly". La cadena
"woolly" contiene "oo" en el medio, lo que satisface el patrón "o+l+". Se encontrará una coincidencia.

3. `print(re.search(r"o+l+", "boil"))`: Aquí nuevamente se busca el patrón "o+l+", pero en la cadena "boil". En este caso,
el patrón no coincide en absoluto con la cadena "boil", ya que no contiene dos letras "o" o "l" consecutivas. Por lo tanto,
no se encontrará ninguna coincidencia.

En resumen, este código utiliza una expresión regular para buscar cadenas que contengan una o más ocurrencias de las letras
"o" seguidas de una o más ocurrencias de las letras "l". Dependiendo de la cadena de entrada, se encontrarán o no coincidencias
con este patrón."""
