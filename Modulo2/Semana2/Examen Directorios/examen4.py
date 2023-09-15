import os

def parent_directory():
    # Crea una ruta relativa para el directorio padre
    relative_parent = os.path.join(os.getcwd(), "..")

    # Retorna la ruta absoluta del directorio padre
    return os.path.abspath(relative_parent)

print(parent_directory())

"""Por supuesto, aquí está la explicación del código que has proporcionado:

1. `import os`: Esta línea importa el módulo `os`, que proporciona funciones para interactuar con el sistema operativo,
incluyendo operaciones relacionadas con archivos y directorios.

2. `def parent_directory():`: Se define una función llamada `parent_directory` que no toma ningún argumento.

3. `relative_parent = os.path.join(os.getcwd(), "..")`: En esta línea, se crea una ruta relativa para el directorio padre.
`os.getcwd()` se utiliza para obtener el directorio de trabajo actual, que es el directorio desde el cual se está ejecutando
el script. Luego, `os.path.join()` se utiliza para combinar el directorio de trabajo actual con "..", que se refiere al
directorio padre. Esto crea una ruta relativa que apunta al directorio padre del directorio actual.

4. `return os.path.abspath(relative_parent)`: La función retorna la ruta absoluta del directorio padre. `os.path.abspath()`
se utiliza para convertir la ruta relativa en una ruta absoluta, lo que garantiza que obtengas la ruta completa y no solo
una ruta relativa.

5. `print(parent_directory())`: Finalmente, la función `parent_directory` se llama y su resultado (la ruta absoluta del
directorio padre) se imprime en la consola.

En resumen, este código crea una función que devuelve la ruta absoluta del directorio padre del directorio de trabajo
actual. Esto puede ser útil cuando necesitas referenciar el directorio padre en tu programa para acceder a archivos o
directorios en un nivel superior."""
