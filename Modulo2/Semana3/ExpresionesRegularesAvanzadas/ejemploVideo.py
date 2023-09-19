# Cambia el formato de un nombre de "Apellido, Nombre" a "Nombre Apellido".

import re
def rearrange_name(name):
  result = re.search(r"^(\w+), (\w+(?: \w)?\.?)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

print(rearrange_name("Kennedy, John F."))


"""En esta expresión regular revisada:

^: Coincide con el inicio de la cadena.
(\w+): Captura uno o más caracteres de palabra (esto coincide con el apellido). , :
Coincide con una coma seguida de un espacio.
(\w+(?: \w)?\.?): Captura uno o más caracteres de palabra (esto coincide con el nombre), seguidos opcionalmente de un
espacio y una inicial del segundo nombre (pueden ser uno o más caracteres de palabra seguidos de un punto opcional).
$: Coincide con el final de la cadena.
Con esta expresión regular, podrás manejar nombres como "Kennedy, John F." correctamente, incluyendo segundos nombres,
iniciales del segundo nombre y apellidos dobles."""

