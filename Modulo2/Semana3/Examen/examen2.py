import re

def check_time(text):
    pattern = r"^(1[0-2]|[1-9]):[0-5][0-9] ?[APap][Mm]$"
    result = re.search(pattern, text)
    return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

"""^: Coincide con el inicio de la cadena.
(1[0-2]|[1-9]): Este grupo captura la hora. Puede ser "1" seguido de un dígito de 0 a 2, lo que representa las horas de
10 a 12, o puede ser un solo dígito de 1 a 9 para las horas de 1 a 9.
:: Coincide con dos puntos literalmente.
[0-5][0-9]: Representa los minutos. Coincide con un dígito de 0 a 5 seguido de otro dígito de 0 a 9, lo que representa
los minutos de 00 a 59.
?: Un espacio opcional después de los minutos.
[APap][Mm]: Representa "AM" o "PM" en mayúsculas o minúsculas.
$: Coincide con el final de la cadena.

Al usar [APap], la expresión regular coincide con cualquiera de estas combinaciones de letras, lo que hace que el código
sea más flexible y funcione independientemente de si las letras están en mayúsculas o minúsculas en el texto de entrada.
Esto mejora la robustez del código y lo hace más versátil para manejar diferentes formatos de entrada."""
