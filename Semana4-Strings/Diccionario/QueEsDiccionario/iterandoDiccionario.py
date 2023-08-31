#Entonces, si usa un diccionario en un bucle for, la variable de iteración irá a través de las claves en el diccionario.
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)

# Devuelve una tupla
for ext, amount in file_counts.items(): # Podemos usar elementos para obtener pares de valores clave
    print("There are {} files with the .{} extension".format(amount, ext))

# Estos métodos devuelven tipos de datos especiales relacionados con el diccionario
file_counts.keys()# Claves para obtener las claves
file_counts.values()#Valores para obtener solo los valores

for value in file_counts.values():
    print(value)

for keys in file_counts.keys():
    print(keys)

#Example
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for ext, char in cool_beasts.items():
    print("{} have {}".format(ext, char))



# Cuantas veces aparece la misma letra:
def count_letters(text):
    result = {} # Inicializamos con un diccionario vacio
    for letter in text: # Luego revisamos cada letra en la cadena dada
        if letter not in result: # Para cada letra, comprobamos si no esta ya en el dicionario
            result[letter] = 0 # En ese caso, inicializamos una entrada en el diccionario con un valor de cero
        result[letter] += 1 # Finalmente, incrementamos el recuento de esa letra en el diccionario
    return result
#En resumen, hemos creado un diccionario donde las claves son cada una de las letras
#presentes en la cadena y los valores son cuantas veces esta presente cada letra

count_letters("aaaaa")
count_letters("tenant")
