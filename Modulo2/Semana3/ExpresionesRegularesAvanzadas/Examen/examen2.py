import re

def multi_vowel_words(text):
    pattern = r'\b\w*[aeiouAEIOU]{3,}\w*\b'
    result = re.findall(pattern, text)
    return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []

"""En esta expresión regular:

\b coincide con el límite de palabra para asegurarse de que coincida con palabras completas.
\w* coincide con cero o más caracteres alfanuméricos antes de las vocales.
[aeiouAEIOU]{3,} coincide con tres o más vocales (mayúsculas o minúsculas).
\w* coincide con cero o más caracteres alfanuméricos después de las vocales.
\b coincide con el límite de palabra al final para asegurarse de que coincida con palabras completas.
De esta manera, la función multi_vowel_words encuentra palabras que contienen al menos tres vocales y devuelve una lista
con esas palabras."""
