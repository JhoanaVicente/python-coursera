"""Sólo diccionarios:
son conjuntos desordenados;
tener claves que pueden ser una variedad de tipos de datos, incluidas cadenas, números enteros, flotantes, tuplas;
puede acceder a los valores del diccionario mediante claves;
utilice corchetes dentro de llaves { [ ] };
utilice dos puntos entre la clave y los valores;
utilice comas para separar cada grupo de claves y cada valor dentro de un grupo de claves;
haga que sea más rápido y fácil para un intérprete de Python encontrar elementos específicos, en comparación con una lista."""

# Ejemplos de diccionario
pet_dictionary = {"dogs": ["Yorkie", "Collie", "Bulldog"], "cats": ["Persian", "Scottish Fold", "Siberian"], "rabbits": ["Angora", "Holland Lop", "Harlequin"]}
print(pet_dictionary.get("dogs", 0))
# Should print ['Yorkie', 'Collie', 'Bulldog']

"""La razón por la que se usa `0` como argumento predeterminado en `pet_dictionary.get("dogs", 0)` es para manejar el caso
en el que la clave "dogs" no existe en el diccionario. El método `.get()` se utiliza para obtener el valor correspondiente
a una clave en un diccionario. Si la clave no existe en el diccionario, el método `.get()` devuelve el valor predeterminado
que se proporciona como segundo argumento. En este caso, si el diccionario `pet_dictionary` no contiene la clave "dogs",
en lugar de devolver un error, se devuelve el valor `0` como resultado. Es una forma de manejar la falta de una clave en
un diccionario sin causar un error. Sin embargo, también podrías usar cualquier otro valor que tenga sentido en el contexto
de tu programa en lugar de `0`, según lo que quieras lograr."""


"""Sólo listas:
son conjuntos ordenados;
elementos de la lista de acceso por posiciones de índice;
requerir que estos índices sean números enteros;
utilice corchetes [ ];
utilice comas para separar cada elemento de la lista."""

pet_list  = ["Yorkie", "Collie", "Bulldog", "Persian", "Scottish Fold", "Siberian", "Angora", "Holland Lop", "Harlequin"]
print(pet_list[0:6])
# Should print ['Yorkie', 'Collie', 'Bulldog']
