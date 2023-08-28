""" Dentro de los parámetros de formato() , seleccione caracteres en posiciones de índice específicas [ ] de una cadena variable.
Utilice el método format() , con {} marcadores de posición para datos variables, para crear una nueva cadena.


Esta función llamada `username` toma el apellido y el año de nacimiento como argumentos y crea un nombre de usuario
combinando las primeras tres letras del apellido con el año de nacimiento. Aquí tienes el desglose de la función y los ejemplos:

1. `def username(last_name, birth_year):`: Define la función `username` que toma dos argumentos: `last_name` (apellido)
y `birth_year` (año de nacimiento).

2. `return("{}{}".format(last_name[0:3],birth_year))`: Esta línea crea el nombre de usuario combinando las primeras tres
letras del apellido y el año de nacimiento.
   - `last_name[0:3]` toma los primeros tres caracteres del apellido.
   - `birth_year` es simplemente el año de nacimiento.
   - El método `format` combina ambos valores en una cadena.

3. Los ejemplos `print(username(...))` al final llaman a la función con diferentes apellidos y años de nacimiento y
muestran los nombres de usuario resultantes.

En resumen, la función crea un nombre de usuario combinando las primeras tres letras del apellido con el año de nacimiento,
como se muestra en los ejemplos que proporcionaste."""

def username(last_name, birth_year):
    return("{}{}".format(last_name[0:3],birth_year))

print(username("Ivanov", "1985"))
# Should display "Iva1985"
print(username("Rodríguez", "2000"))
# Should display "Rod2000"
print(username("Deng", "1991"))
# Should display "Den1991"
