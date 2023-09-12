"""Utilice una lista de comprensión para devolver valores"""

def squares(start, end):
    return [n*n for n in range(start, end+1)]
print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


"""Utilice el método string.split() para separar una cadena en una lista de palabras individuales.
Itere sobre la nueva lista usando un bucle for .
Modifique cada elemento de la lista dividiendo la cadena del elemento en una posición de índice [1:] determinada
y agregando la subcadena al final del elemento.
Convierte una lista nuevamente en una cadena."""

def change_string(given_string):
    new_string = ""
    new_list = given_string.split()

    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "
    return new_string

print(change_string("1one 2two 3three 4four 5five"))
# Should print "one-1 two-2 three-3 four-4 five-5"



"""Utilice el método string.join() para concatenar una cadena que proporciona un nombre de lista y sus elementos"""

def list_elements(list_name, elements):
    return "The " + list_name + " list includes: " + ", ".join(elements)

print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))
# Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"
