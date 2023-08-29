filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []

for filename in filenames:
    if filename.endswith(".hpp"):
        newfilenames.append(filename[:-4] + ".h")
    else:
        newfilenames.append(filename)

print(newfilenames)

"""En este código:
Creamos una lista vacía llamada newfilenames que usaremos para almacenar los nuevos nombres de archivo.
Utilizamos un bucle for para iterar a través de cada filename en la lista filenames.
Dentro del bucle, verificamos si el nombre de archivo termina con ".hpp" utilizando filename.endswith(".hpp").
Si el nombre de archivo termina con ".hpp", eliminamos los últimos cuatro caracteres (la extensión ".hpp")
y luego agregamos ".h" al final para obtener el nuevo nombre de archivo.
Si el nombre de archivo no termina con ".hpp", simplemente lo agregamos a la lista newfilenames sin cambios.
Finalmente, después del bucle, imprimimos la lista newfilenames."""
