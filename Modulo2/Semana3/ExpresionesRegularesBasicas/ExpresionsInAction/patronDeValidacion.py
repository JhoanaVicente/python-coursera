import re

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))

print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

"""El patrón `r"^[a-zA-Z_][a-zA-Z0-9_]*$"` se utiliza para validar si una cadena es un nombre de variable válido en muchos
lenguajes de programación. Aquí está el análisis de las expresiones regulares en cada línea de código junto con los
resultados correspondientes:

1. `print(re.search(pattern, "_this_is_a_valid_variable_name"))`: Esta línea busca el patrón en la cadena "_this_is_a_valid_variable_name".
El patrón busca lo siguiente:
   - `^`: El comienzo de la cadena.
   - `[a-zA-Z_]`: Una letra mayúscula o minúscula o un guión bajo al principio.
   - `[a-zA-Z0-9_]*`: Cualquier número de letras mayúsculas o minúsculas, dígitos o guiones bajos.
   - `$`: El final de la cadena.

   En este caso, la cadena "_this_is_a_valid_variable_name" cumple con el patrón ya que comienza con un guión bajo y
luego contiene letras, dígitos y guiones bajos. La salida será un objeto `Match` que indica la posición donde se encontró
la coincidencia.

2. `print(re.search(pattern, "this isn't a valid variable"))`: Esta línea busca el mismo patrón en la cadena "this isn't a valid variable".
En este caso, la cadena no cumple con el patrón ya que comienza con una letra y contiene espacios y apóstrofes, que no
están permitidos en los nombres de variables. La salida será `None`.

3. `print(re.search(pattern, "my_variable1"))`: Esta línea busca el patrón en la cadena "my_variable1". La cadena cumple
con el patrón ya que comienza con una letra y luego contiene letras, dígitos y guiones bajos. La salida será un objeto `Match`.

4. `print(re.search(pattern, "2my_variable1"))`: En este caso, la cadena "2my_variable1" no cumple con el patrón ya que
comienza con un dígito, lo cual no es válido para un nombre de variable. La salida será `None`.

En resumen, este patrón se utiliza para validar si una cadena es un nombre de variable válido en la mayoría de los lenguajes
de programación, siguiendo las reglas típicas de nombres de variables, como comenzar con una letra o un guión bajo y permitir
letras, dígitos y guiones bajos adicionales."""
