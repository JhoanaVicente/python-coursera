"""La función crea una etiqueta de nombre formateada utilizando el primer nombre y la primera letra del apellido:
return("{} {}.".format(first_name, last_name[0])): Esta línea crea la etiqueta de nombre utilizando el método format para
incorporar los valores de first_name (primer nombre) y la primera letra de last_name (primer carácter del apellido) en la
cadena. La cadena resultante es la etiqueta de nombre formateada como se desea.

Los ejemplos print(nametag(...)) al final llaman a la función con diferentes nombres y apellidos y muestran las etiquetas
de nombre resultantes según lo descrito anteriormente."""

def nametag(first_name, last_name):
    return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."
