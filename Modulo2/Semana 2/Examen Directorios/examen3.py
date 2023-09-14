import os
import datetime

def file_date(filename):
    # Crear el archivo en el directorio actual
    with open(filename, "w") as file:
        pass  # Puedes agregar contenido al archivo si lo deseas

    # Obtener la marca de tiempo de creación del archivo
    timestamp = os.path.getctime(filename)

    # Convertir la marca de tiempo en una fecha legible
    date = datetime.datetime.fromtimestamp(timestamp).date()

    # Convertir la fecha en una cadena con el formato "yyyy-mm-dd"
    date_str = date.strftime("%Y-%m-%d")

    # Retornar la fecha en el formato deseado
    return "{:s}".format(date_str)

print(file_date("PythonPrograms/newfile.txt"))

"""Este código tiene como objetivo crear un archivo con un nombre especificado, obtener la fecha de creación de ese archivo
y luego formatear esa fecha en un formato específico ("yyyy-mm-dd"). A continuación, te explico el código paso a paso:

1. `import os`: Esta línea importa el módulo `os`, que proporciona funciones para interactuar con el sistema operativo,
incluyendo operaciones relacionadas con archivos y directorios.

2. `import datetime`: Aquí se importa el módulo `datetime`, que proporciona clases y funciones para trabajar con fechas
y horas en Python.

3. `def file_date(filename):`: Se define una función llamada `file_date` que toma un argumento `filename`, que es el nombre
del archivo que se va a crear y del cual se desea obtener la fecha de creación.

4. `with open(filename, "w") as file:`: Se utiliza un bloque `with` para abrir el archivo especificado en `filename` en
modo de escritura (`"w"`). Esto crea el archivo o lo sobrescribe si ya existe. El archivo se abre dentro de un contexto,
lo que asegura que se cierre adecuadamente después de su uso.

5. `pass`: Esta línea es un marcador de posición. Puedes agregar contenido al archivo dentro del bloque `with` si lo deseas,
pero en el código proporcionado, el archivo se crea vacío.

6. `timestamp = os.path.getctime(filename)`: Después de crear el archivo, se utiliza la función `os.path.getctime()` para
obtener la marca de tiempo de creación del archivo en segundos desde la época.

7. `date = datetime.datetime.fromtimestamp(timestamp).date()`: Se convierte la marca de tiempo en un objeto de fecha
legible utilizando `datetime.datetime.fromtimestamp(timestamp).date()`.

8. `date_str = date.strftime("%Y-%m-%d")`: Luego, se formatea la fecha en una cadena con el formato deseado ("yyyy-mm-dd")
utilizando el método `strftime()`.

9. `return "{:s}".format(date_str)`: La función retorna la fecha formateada como una cadena de caracteres.

10. `print(file_date("newfile.txt"))`: Finalmente, la función `file_date` se llama con el argumento "newfile.txt" para
crear el archivo y obtener la fecha de creación, que se imprime en la consola.

En resumen, este código crea un archivo llamado "newfile.txt" (aunque inicialmente está vacío), obtiene la fecha de
creación de ese archivo y la retorna en el formato "yyyy-mm-dd"."""
