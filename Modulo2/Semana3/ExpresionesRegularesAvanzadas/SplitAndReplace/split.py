"""La función re.split() se utiliza para dividir una cadena en una lista de subcadenas en función de un patrón regular. El
patrón regular se utiliza para encontrar los lugares donde se debe realizar la división."""

import re

"""Estás utilizando el patrón [.?!] que coincide con cualquier punto, signo de interrogación o signo de exclamación en la
cadena. Como resultado, la cadena se divide en partes cada vez que se encuentra uno de estos caracteres de puntuación,
y obtienes una lista de las partes divididas:Obtienes una lista que contiene las partes divididas de la cadena original."""
result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(result)



"""Estás utilizando el mismo patrón [.?!], pero esta vez has colocado el patrón entre paréntesis ( ), lo que crea un grupo
de captura. Esto significa que el patrón también se incluirá en los resultados, pero como parte de elementos separados
en la lista. Como resultado, obtienes una lista que contiene tanto las partes divididas como los caracteres de puntuación:
En este caso, obtienes una lista donde los caracteres de puntuación también se incluyen como elementos separados en la lista.
Puedes utilizar esta funcionalidad para dividir una cadena y mantener los delimitadores si es necesario para tu aplicación específica."""
result2 = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(result2)
