"""re.sub() es una función útil para realizar sustituciones en cadenas utilizando expresiones regulares, lo que te permite
buscar patrones específicos y reemplazarlos por otro texto."""
import re

result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
print(result)

"""En esta línea de código, estás utilizando re.sub() para buscar y reemplazar cualquier dirección de correo electrónico
en la cadena de entrada por "[REDACTED]". La expresión regular r"[\w.%+-]+@[\w.-]+" se utiliza para encontrar las
direcciones de correo electrónico en la cadena. Aquí está desglosada: [\w.%+-]+ busca uno o más caracteres de palabra,
puntos, porcentaje, signos más o menos, y el carácter de punto. @ coincide con el carácter "@" literal.
[\w.-]+ busca uno o más caracteres de palabra, puntos o guiones antes del dominio del correo electrónico.
El resultado será que cualquier dirección de correo electrónico encontrada en la cadena se reemplazará por "[REDACTED]".
El resultado se guarda en la variable result."""



result2 = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(result2)

"""En esta línea de código, estás utilizando re.sub() para reorganizar el formato de un nombre en la cadena de entrada. La
expresión regular r"^([\w .-]*), ([\w .-]*)$" busca nombres en formato "Apellido, Nombre". Aquí está desglosada:

^ coincide con el inicio de la cadena.
([\w .-]*) captura un grupo de caracteres que pueden ser letras, espacios, puntos o guiones, que representa el apellido.
, coincide con una coma literal seguida de un espacio.
([\w .-]*) captura otro grupo de caracteres que pueden ser letras, espacios, puntos o guiones, que representa el nombre.
$ coincide con el final de la cadena.
La expresión r"\2 \1" en el segundo argumento de re.sub() se utiliza para reorganizar el apellido y el nombre en el
formato "Nombre Apellido". \2 se refiere al segundo grupo de captura (nombre), y \1 se refiere al primer grupo de captura (apellido).

El resultado será que "Lovelace, Ada" se reemplazará por "Ada Lovelace". El resultado se guarda en la variable result2."""
