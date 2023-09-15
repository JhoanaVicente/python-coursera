import os

def new_directory(directory, filename):
    # Antes de crear un nuevo directorio, verifica si ya existe
    if os.path.isdir(directory) == False:
        os.mkdir(directory)  # Crea el nuevo directorio si no existe

    # Cámbiate al nuevo directorio
    os.chdir(directory)

    # Crea el nuevo archivo dentro del nuevo directorio
    with open(filename, "w") as file:
        pass # Aquí puedes agregar contenido al archivo si lo deseas

    # Retorna la lista de archivos en el nuevo directorio
    return os.listdir()

print(new_directory("PythonPrograms", "script.py"))


"""Aquí está el desglose del código:

import os: Importa el módulo os, que proporciona funcionalidad para interactuar con el sistema operativo, incluyendo la
creación de directorios, cambio de directorio de trabajo, entre otras operaciones relacionadas con archivos y directorios.

def new_directory(directory, filename):: Define una función llamada new_directory que toma dos argumentos: directory
(nombre del directorio que deseas crear o verificar) y filename (nombre del archivo que deseas crear dentro del directorio).

if os.path.isdir(directory) == False:: Comprueba si el directorio especificado en directory ya existe utilizando os.path.isdir().
Si el directorio no existe, se ejecuta el siguiente bloque de código.

os.mkdir(directory): Crea el nuevo directorio utilizando os.mkdir(). Este comando crea el directorio con el nombre especificado
en directory.

os.chdir(directory): Cambia el directorio de trabajo actual al nuevo directorio recién creado utilizando os.chdir(). Esto
asegura que el archivo se creará en el nuevo directorio.

with open(filename, "w") as file:: Abre el archivo especificado en filename en modo de escritura ("w") utilizando un bloque
with. Esto garantiza que el archivo se cierre automáticamente después de su uso.

pass: Esta línea es un marcador de posición. Puedes agregar el contenido que desees escribir en el archivo en lugar de pass.

return os.listdir(): Retorna la lista de archivos en el directorio actual (que es el nuevo directorio "PythonPrograms"
en este caso) utilizando os.listdir(). Esto te permite verificar que el archivo "script.py" se haya creado con éxito en el nuevo directorio.

En resumen, este código crea un nuevo directorio si no existe, cambia al nuevo directorio, crea un archivo dentro de él
y luego devuelve la lista de archivos en el nuevo directorio. Puedes utilizar este código como una función para automatizar
la creación de directorios y archivos en tu sistema de archivos."""




