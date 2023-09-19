import re
print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Pyn"))

"""Este ejercicio de Python que utiliza el módulo `re` (expresiones regulares) para buscar
patrones en cadenas de texto. Aquí tienes una explicación línea por línea:

1. `import re`: Esta línea importa el módulo `re`, que es necesario para trabajar con expresiones regulares en Python.

2. `print(re.search(r"Py.*n", "Pygmalion"))`: Este código busca el patrón "Py.*n" en la cadena de texto "Pygmalion".
La expresión regular "Py.*n" significa lo siguiente:
   - `Py`: Busca la letra "P" seguida de "y".
   - `.*`: Esto coincide con cualquier número de caracteres (cualquier carácter y cualquier cantidad de ellos).
   - `n`: Finalmente, busca la letra "n".

   En este caso, la cadena "Pygmalion" coincide con el patrón ya que comienza con "Py" y termina con "n". El resultado
será un objeto `Match` que indica la posición donde se encontró la coincidencia.

3. `print(re.search(r"Py.*n", "Python Programming"))`: Este código busca el mismo patrón "Py.*n" en la cadena de texto
"Python Programming". Aquí también encontrarás una coincidencia ya que "Python" satisface el patrón, comenzando con "Py"
y terminando con "n".

4. `print(re.search(r"Py[a-z]*n", "Python Programming"))`: En este caso, la expresión regular es "Py[a-z]*n", lo que
significa lo siguiente:
   - `Py`: Busca la letra "P" seguida de "y".
   - `[a-z]*`: Esto coincide con cero o más letras minúsculas entre "a" y "z".
   - `n`: Finalmente, busca la letra "n".

   En la cadena "Python Programming", "Python" cumple con el patrón, ya que comienza con "Py" y termina con "n". La
expresión `[a-z]*` coincide con "thon" porque todas las letras están en minúsculas.

5. `print(re.search(r"Py[a-z]*n", "Pyn"))`: En este último caso, la cadena es "Pyn". El patrón "Py[a-z]*n" buscará "Pyn"
y lo encontrará como una coincidencia válida, ya que "Pyn" comienza con "Py" y termina con "n", y no contiene letras mayúsculas.

En resumen, el código utiliza expresiones regulares para buscar patrones en las cadenas de texto y devuelve las
coincidencias encontradas."""
