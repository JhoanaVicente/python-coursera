import re
def long_words(text):
  pattern = r"\w{7,10}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

"""La función `long_words` toma un texto como entrada y devuelve una lista de palabras que tienen entre 7 y 10 caracteres de
longitud. Aquí está el desglose de la función:

1. `import re`: Esto importa el módulo de expresiones regulares de Python.

2. `def long_words(text):`: Define la función `long_words` que toma un argumento `text`, que es el texto en el que queremos
buscar palabras largas.

3. `pattern = r"\w{7,10}"`: Esto define una expresión regular llamada `pattern`. La expresión regular `"\w{7,10}"` busca
palabras que consisten en caracteres de palabra (letras y números) y que tienen una longitud de 7 a 10 caracteres.

4. `result = re.findall(pattern, text)`: Utiliza la función `re.findall` para buscar todas las coincidencias de la expresión
regular `pattern` en el texto de entrada `text`. Esto devuelve una lista de todas las palabras que cumplen con el patrón.

5. `return result`: La función devuelve la lista de palabras encontradas.

Luego, se muestra cómo usar la función con tres ejemplos diferentes:

- `print(long_words("I like to drink coffee in the morning."))`: Busca palabras largas en la frase "I like to drink coffee in the morning."
y devuelve `['morning']`, que es la única palabra que cumple con el patrón.

- `print(long_words("I also have a taste for hot chocolate in the afternoon."))`: Busca palabras largas en la frase
"I also have a taste for hot chocolate in the afternoon." y devuelve `['chocolate', 'afternoon']`, que son las dos palabras
que cumplen con el patrón.

- `print(long_words("I never drink tea late at night."))`: Busca palabras largas en la frase "I never drink tea late at night."
pero no encuentra ninguna palabra que cumpla con el patrón, por lo que devuelve una lista vacía `[]`.

La función es útil para filtrar palabras largas de un texto según el criterio de longitud definido en el patrón de la
expresión regular."""
