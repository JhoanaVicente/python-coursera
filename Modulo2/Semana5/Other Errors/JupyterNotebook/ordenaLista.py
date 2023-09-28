my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list))

my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))

def OrganizeList(myList):
    for item in myList:
        assert type(myList) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list))

"""El código proporcionado tiene dos definiciones de la función `OrganizeList`, y cada una realiza una acción diferente
en función del tipo de elementos en la lista que recibe como argumento.

1. **Primera definición de `OrganizeList`**:
   - Esta función toma una lista `myList` como argumento.
   - Si `myList` es una lista de cadenas de texto (strings), la función la ordena alfabéticamente utilizando el método `sort()`
   y luego devuelve la lista ordenada.
   - La primera llamada a la función `OrganizeList` toma la lista `my_word_list`, que es una lista de cadenas, y la ordena
   alfabéticamente. Luego, imprime la lista ordenada.
   - La segunda llamada a la función `OrganizeList` toma la lista `my_new_list`, que contiene números y una cadena, y
   también la ordena alfabéticamente. Luego, imprime la lista ordenada.

2. **Segunda definición de `OrganizeList`**:
   - Esta función también toma una lista `myList` como argumento.
   - Sin embargo, antes de ordenar la lista, realiza una verificación para asegurarse de que todos los elementos en `myList`
   sean de tipo cadena (str). Si encuentra algún elemento que no es una cadena, generará una excepción `AssertionError`
   con el mensaje "Word list must be a list of strings".
   - Luego, si todos los elementos son cadenas, ordena la lista alfabéticamente con `sort()` y la devuelve.
   - La tercera llamada a la función `OrganizeList` toma la lista `my_new_list`, que contiene números y una cadena.
   Debido a la verificación de tipo que realiza antes de ordenar, generará un error ya que `my_new_list` no cumple con
   el requisito de ser una lista de cadenas.

Resumen:
- La primera versión de la función `OrganizeList` ordena cualquier lista que se le pase.
- La segunda versión de la función `OrganizeList` ordena una lista solo si todos sus elementos son cadenas, de lo
contrario, genera un error."""
