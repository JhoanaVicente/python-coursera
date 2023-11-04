def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False

  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list?
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]
list_of_names.sort()

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False
print(find_item(list_of_names, "Jamie")) # True

"""Esta función se utiliza para buscar un elemento en una lista ordenada mediante una búsqueda binaria. Ayuda a determinar
eficientemente si un elemento dado se encuentra en la lista o no. Los parámetros son la lista ordenada en la que se va a buscar y el elemento que se desea encontrar. La función devuelve True si encuentra el elemento en la lista y False en caso contrario.

El código que sigue a la función realiza algunas pruebas para verificar su funcionamiento, comprobando si ciertos elementos
están en la lista y si devuelve los resultados esperados."""
