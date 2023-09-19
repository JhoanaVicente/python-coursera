import re

def check_sentence(text):
    result = re.search(r"^[A-Z].*[?.]$", text)
    return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

"""Ahora, el código utiliza la expresión regular `r"^[A-Z].*[?.]$"` para verificar si la cadena es una oración que comienza
con una letra mayúscula, contiene caracteres y termina con un signo de puntuación (? o .). Los ejemplos de llamadas a la
función producirán los resultados que esperas."""
