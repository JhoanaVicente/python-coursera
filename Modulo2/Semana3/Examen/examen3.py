import re

def contains_acronym(text):
    # La expresión regular busca un paréntesis de apertura seguido por al menos un carácter en mayúscula o dígito,
    # seguido opcionalmente por caracteres en minúscula o dígitos, y luego un paréntesis de cierre.
    pattern = r"\([A-Z0-9][A-Za-z0-9]*\)"

    # Busca si el patrón se encuentra en el texto proporcionado.
    result = re.search(pattern, text)

    # Devuelve True si se encuentra un acrónimo que cumple con las condiciones, de lo contrario, devuelve False.
    return result is not None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


"""La función `contains_acronym` se encarga de verificar si una cadena de texto contiene un acrónimo. Un acrónimo es una
abreviatura formada por las letras iniciales de una frase o nombre, y en este caso, estamos buscando acrónimos que estén
entre paréntesis en el texto.

Aquí está cómo funciona la función paso a paso:

1. Se define una expresión regular en la variable `pattern`. La expresión regular `r"\([A-Z0-9][A-Za-z0-9]*\)"` tiene
los siguientes componentes:
   - `\(`: Coincide con un paréntesis de apertura "(".
   - `[A-Z0-9]`: Coincide con un solo carácter que sea una letra mayúscula o un dígito.
   - `[A-Za-z0-9]*`: Coincide con cero o más caracteres que pueden ser letras mayúsculas, letras minúsculas o dígitos.
   - `\)`: Coincide con un paréntesis de cierre ")".

2. La función busca si el patrón definido en `pattern` se encuentra en el texto proporcionado usando `re.search(pattern, text)`.

3. Si se encuentra una coincidencia que cumple con el patrón, la función devuelve `True`, indicando que se ha encontrado
un acrónimo válido. En caso contrario, devuelve `False`, lo que significa que no se encontró ningún acrónimo válido en el texto.

En resumen, la función `contains_acronym` utiliza una expresión regular para buscar acrónimos que estén entre paréntesis
en el texto. Si encuentra al menos un acrónimo que cumple con las condiciones (al menos una letra mayúscula o un dígito
entre paréntesis), devuelve `True`; de lo contrario, devuelve `False`. Esto te permite verificar si una cadena contien
acrónimos en ese formato específico."""




("""No es necesario utilizar ^ y $ porque estamos buscando acrónimos dentro del texto en lugar de hacer coincidir toda la cadena.
En este escenario, queremos encontrar acrónimos que estén en cualquier parte del texto, no necesariamente al principio o
al final. Por lo tanto, no utilizamos ^ para el inicio y $ para el final. En cambio, usamos paréntesis \( y \) para denotar
el inicio y el final de un acrónimo dentro del texto.""")
