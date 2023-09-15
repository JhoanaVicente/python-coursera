import os

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return filesize

print(create_python_script("PythonPrograms/program.py"))

"""Claro, estaré encantado de explicarte el código paso a paso:

1. `import os`: Esta línea importa el módulo `os`, que es un módulo estándar de Python que proporciona funciones para
interactuar con el sistema operativo, como trabajar con archivos y directorios.

2. `def create_python_script(filename):`: Aquí se define una función llamada `create_python_script` que toma un argumento
`filename`, que es el nombre del archivo que se va a crear.

3. `comments = "# Start of a new Python program"`: En esta línea, se crea una cadena de texto llamada `comments` que
contiene un comentario inicial que se desea agregar al archivo Python.

4. `with open(filename, "w") as file:`: Se utiliza un bloque `with` para abrir el archivo especificado en `filename` en
modo de escritura (`"w"`). Esto crea el archivo o lo sobrescribe si ya existe. El archivo se abre dentro de un contexto,
lo que asegura que se cierre adecuadamente después de su uso.

5. `file.write(comments)`: Dentro del bloque `with`, se utiliza el método `write` para escribir el contenido de la cadena
`comments` en el archivo recién creado. Esto agrega el comentario al principio del archivo.

6. `filesize = os.path.getsize(filename)`: Después de escribir el comentario en el archivo, se utiliza la función
`os.path.getsize()` para obtener el tamaño del archivo en bytes. La variable `filesize` guarda ese valor.

7. `return filesize`: La función retorna el tamaño del archivo en bytes como resultado.

8. `print(create_python_script("program.py"))`: Finalmente, la función `create_python_script` se llama con el argumento
`"program.py"` para crear un archivo llamado "program.py" y agregar el comentario. Luego, el tamaño del archivo se imprime en la consola.

En resumen, este código crea un nuevo archivo Python llamado "program.py", agrega un comentario inicial al archivo y
luego devuelve el tamaño del archivo en bytes. Puedes utilizar este código como un punto de partida para generar archivos
Python con contenido inicial desde tu programa."""
