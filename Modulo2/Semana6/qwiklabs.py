#!/bin/bash

>oldFiles.txt

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3);

for file in $files; do
    if test -e "..${file}"; then echo "..${file}" >> oldFiles.txt; fi
done



#!/usr/bin/env python3
import sys
import subprocess
string.replace(old_substring, new_substring)
mv source destination
f.close()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import subprocess

# Obtén el nombre del archivo oldFiles.txt desde los argumentos de línea de comandos
old_files_filename = sys.argv[1]

# Abre el archivo oldFiles.txt y lee sus contenidos
with open(old_files_filename, 'r') as file:
    old_file_lines = file.readlines()

# Itera a través de las líneas y obtén los nombres antiguos de los archivos
old_names = []
for line in old_file_lines:
    old_name = line.strip()
    old_names.append(old_name)

# Reemplaza "jane" por "jdoe" en los nombres antiguos y obtén los nuevos nombres
new_names = [old_name.replace(" jane ", " jdoe ") for old_name in old_names]

# Renombra los archivos usando el comando 'mv'
for old_name, new_name in zip(old_names, new_names):
    subprocess.call(['mv', old_name, new_name])


"""Por supuesto, aquí tienes una explicación detallada del código:

1. `#!/usr/bin/env python3`: Esta línea indica que el script debe ser ejecutado usando el intérprete de Python 3.

2. `import sys`: Importa el módulo `sys`, que proporciona acceso a variables y funciones relacionadas con el sistema.

3. `import subprocess`: Importa el módulo `subprocess`, que permite ejecutar comandos del sistema desde Python.

4. `old_files_filename = sys.argv[1]`: Obtiene el nombre del archivo `oldFiles.txt` como un argumento de línea de comandos.
El programa espera que se le proporcione este nombre de archivo cuando se ejecuta.

5. `with open(old_files_filename, 'r') as file:`: Abre el archivo `oldFiles.txt` en modo lectura (`'r'`) usando un
bloque `with`, lo que asegura que el archivo se cierre correctamente después de su uso.

6. `old_file_lines = file.readlines()`: Lee todas las líneas del archivo `oldFiles.txt` y las almacena en la lista `old_file_lines`.

7. `old_names = []`: Crea una lista vacía llamada `old_names` para almacenar los nombres de archivo antiguos.

8. `for line in old_file_lines:`: Itera a través de las líneas leídas del archivo.

9. `old_name = line.strip()`: Elimina cualquier espacio en blanco o salto de línea alrededor del nombre de archivo
en cada línea y lo almacena en la variable `old_name`.

10. `old_names.append(old_name)`: Agrega el nombre de archivo antiguo a la lista `old_names`.

11. `new_names = [old_name.replace(" jane ", " jdoe ") for old_name in old_names]`: Crea una nueva lista llamada `new_names`
donde se reemplaza la cadena "jane" por "jdoe" en cada nombre de archivo antiguo. Esto crea los nuevos nombres de archivo.

12. `for old_name, new_name in zip(old_names, new_names):`: Itera a través de las listas `old_names` y `new_names` al mismo tiempo.

13. `subprocess.call(['mv', old_name, new_name])`: Utiliza el comando `mv` para renombrar los archivos. `mv` toma dos
argumentos: el nombre antiguo del archivo (`old_name`) y el nuevo nombre del archivo (`new_name`).

En resumen, este script renombra archivos según las instrucciones proporcionadas en el archivo `oldFiles.txt`. Cada línea
en `oldFiles.txt` contiene un nombre de archivo antiguo, y el script reemplaza "jane" por "jdoe" en esos nombres para
obtener los nuevos nombres de archivo. Luego, utiliza el comando `mv` para realizar el cambio de nombre en el sistema de archivos."""
