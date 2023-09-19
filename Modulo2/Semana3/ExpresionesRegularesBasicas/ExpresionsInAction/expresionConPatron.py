import re

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"A.*a$", "Azerbaijan"))
print(re.search(r"A.*a$", "Australia"))

"""Aquí tienes el análisis de las expresiones regulares utilizadas en cada una de las líneas de código junto con los
resultados correspondientes:

1. `print(re.search(r"A.*a", "Argentina"))`: Esta expresión regular busca el patrón que comienza con la letra "A",
seguida de cualquier número de caracteres (representados por `.*`), y luego termina con la letra "a". En la cadena
"Argentina", esto coincide con "Argentina" ya que comienza con "A" y termina con "a". La salida será un objeto `Match`
que indica la posición donde se encontró la coincidencia.

2. `print(re.search(r"A.*a", "Azerbaijan"))`: Similar al caso anterior, esta expresión regular busca el patrón que
comienza con "A", seguido de cualquier número de caracteres, y luego termina con "a". En "Azerbaijan", coincidirá con
"Azerbaija" ya que es la secuencia que satisface el patrón. La salida será un objeto `Match`.

3. `print(re.search(r"A.*a$", "Azerbaijan"))`: Esta expresión regular es similar a la anterior, pero agrega el símbolo
"$" al final del patrón, lo que significa que la coincidencia debe terminar con "a" al final de la cadena. En "Azerbaijan",
no habrá coincidencia ya que la cadena termina con "n". La salida será `None`.

4. `print(re.search(r"A.*a$", "Australia"))`: En este caso, la expresión regular busca el patrón que comienza con "A",
seguido de cualquier número de caracteres, y luego termina con "a" al final de la cadena. En "Australia", coincidirá con
"Australia" ya que comienza con "A" y termina con "a". La salida será un objeto `Match`.

En resumen, estas expresiones regulares se utilizan para buscar patrones específicos en cadenas de texto y los resultados
dependen de si la cadena cumple con el patrón especificado."""
