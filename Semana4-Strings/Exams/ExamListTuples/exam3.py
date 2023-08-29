def group_list(group, users):
  members = ", ".join(users)
  return "{}: {}".format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

"""En este código:
", ".join(users) une los elementos de la lista users utilizando una coma seguida de un espacio como separador.
"{}: {}".format(group, members) utiliza el método format() para formatear una cadena que incluye el nombre del grupo (group) y la lista de miembros concatenados (members)
Finalmente, la función group_list(group, users) devuelve la cadena formateada.
Este código tomará el nombre del grupo y la lista de miembros y devolverá una cadena en el formato especificado."""
