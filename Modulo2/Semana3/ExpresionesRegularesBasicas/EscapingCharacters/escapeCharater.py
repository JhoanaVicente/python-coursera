import re

print(re.search(r".com", "welcome")) #Coincidimos con una cadena con otra cosa en ella, para hacer coincidir queremos un caracter ESCAPE

print(re.search(r"\.com", "welcome"))

print(re.search(r"\.com", "mydomain.com"))

print(re.search(r"\w*", "This is an example"))

print(re.search(r"\w*", "And_this_is_another"))

"""print(re.search(r"\.com", "welcome")): En esta línea, se busca el patrón ".com" en la cadena "welcome". La expresión
regular "\.com" busca específicamente ".com". Dado que "welcome" no contiene ".com", no se encontrará ninguna coincidencia.
La salida también será None.

print(re.search(r"\.com", "mydomain.com")): En esta línea, se busca el patrón ".com" en la cadena "mydomain.com".
La expresión regular "\.com" busca ".com". Como "mydomain.com" contiene ".com", se encontrará una coincidencia. La salida
será un objeto Match que indica la posición donde se encontró la coincidencia.

print(re.search(r"\w*", "This is an example")): En esta línea, se busca el patrón "\w*" en la cadena "This is an example".
La expresión regular "\w*" busca cero o más caracteres de palabra (letras, dígitos o guiones bajos). En "This is an example",
coincidirá con "This" ya que es la primera secuencia de caracteres que satisface el patrón. La salida será un objeto Match que
indica la posición donde se encontró la coincidencia.

print(re.search(r"\w*", "And_this_is_another")): En esta línea, se busca el patrón "\w*" en la cadena "And_this_is_another".
La expresión regular "\w*" buscará caracteres de palabra (letras, dígitos o guiones bajos) y coincide con la cadena completa
"And_this_is_another". La salida será un objeto Match que indica la posición donde se encontró la coincidencia.

En resumen, estas líneas de código muestran cómo las expresiones regulares pueden utilizarse para buscar patrones específicos
en cadenas de texto. La salida dependerá de si el patrón especificado coincide o no con la cadena de entrada."""





