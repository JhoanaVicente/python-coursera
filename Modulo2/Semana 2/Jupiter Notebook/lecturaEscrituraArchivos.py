guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line.strip()) # Le agregué STRIP

"""Claro, puedo explicarte el código que proporcionaste:

1. `guests = open("guests.txt", "w")`: En esta línea, se abre el archivo llamado "guests.txt" en modo de escritura (`"w"`).
Esto significa que si el archivo ya existe, se eliminará su contenido anterior y se creará uno nuevo. Si el archivo no existe,
se creará uno nuevo. La variable `guests` se utiliza para hacer referencia al archivo abierto.

2. `initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]`: Aquí, se crea una lista llamada `initial_guests` que
contiene los nombres de los invitados iniciales que se desean agregar al archivo.

3. El bucle `for i in initial_guests:` recorre la lista de invitados iniciales.

4. `guests.write(i + "\n")`: Dentro del bucle, se utiliza el método `write` para escribir cada nombre de invitado seguido
de un carácter de nueva línea (`"\n"`) en el archivo "guests.txt". Esto coloca cada nombre en una línea separada en el archivo.

5. `guests.close()`: Después de agregar todos los invitados iniciales al archivo, se cierra el archivo utilizando el método
`close()`. Esto es importante para asegurarse de que los cambios se guarden y el archivo se cierre adecuadamente.

6. Luego, el código utiliza un bloque `with` para abrir el archivo "guests.txt" en modo de lectura (`"r"`) en un contexto.
Dentro del bloque `with`, se recorre el archivo línea por línea utilizando un bucle `for line in guests:`.

7. `print(line.strip())`: Dentro del bucle, se utiliza `print()` para mostrar cada línea del archivo. `line.strip()` se
utiliza para eliminar los caracteres de nueva línea (`"\n"`) que están al final de cada línea del archivo, lo que hace que
la salida sea más limpia.

En resumen, este código crea un archivo llamado "guests.txt", agrega una lista de invitados iniciales a ese archivo, luego
lo cierra y, finalmente, lo vuelve a abrir para leerlo línea por línea e imprimir cada nombre de invitado en la consola."""




# Now suppose we want to update our file as guests check in and out.
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

"""El código que has proporcionado agrega nuevos invitados a un archivo llamado "guests.txt" y luego muestra la lista completa
de invitados en la consola. Aquí está el desglose del código:

1. `new_guests = ["Sam", "Danielle", "Jacob"]`: En esta línea, se crea una lista llamada `new_guests` que contiene los
nombres de los nuevos invitados que se desean agregar al archivo.

2. El código utiliza un bloque `with` para abrir el archivo "guests.txt" en modo de apendizaje (`"a"`) en un contexto.
El modo "a" permite agregar contenido al final del archivo sin sobrescribir su contenido existente.

3. `for i in new_guests:`: Este bucle `for` itera a través de la lista de nuevos invitados (`new_guests`).

4. `guests.write(i + "\n")`: Dentro del bucle, se utiliza el método `write` para agregar cada nombre de nuevo invitado
al final del archivo "guests.txt", cada uno en una nueva línea (`"\n"`).

5. `guests.close()`: Una vez que se han agregado todos los nuevos invitados al archivo, se cierra el archivo utilizando
`close()`. Sin embargo, en realidad, no necesitas cerrar el archivo manualmente cuando lo abres con un bloque `with`, ya
    que se cerrará automáticamente al salir del bloque `with`.

6. Luego, el código utiliza otro bloque `with` para abrir el archivo "guests.txt" en modo de lectura (`"r"`) y leer su contenido línea por línea.

7. `for line in guests:`: Este bucle `for` itera a través de cada línea del archivo.

8. `print(line)`: Dentro del bucle, se utiliza `print()` para mostrar cada línea del archivo en la consola.

El resultado de este código será mostrar la lista completa de invitados, incluyendo los invitados iniciales y los nuevos
invitados, en la consola. La lista se mostrará línea por línea."""




# Remove the guests that have checked out already.
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line.split())

"""El código que proporcionaste parece ser una extensión del código anterior. En este caso, el código lee el archivo "guests.txt",
elimina los nombres que están en la lista "checked_out" y luego muestra la lista resultante en la consola. Aquí está el desglose del código:

1. `checked_out = ["Andrea", "Manuel", "Khalid"]`: Se define una lista llamada "checked_out" que contiene los nombres de
los invitados que se han retirado o salido del lugar.

2. `temp_list = []`: Se crea una lista vacía llamada "temp_list" que se utilizará para almacenar temporalmente los nombres
de los invitados del archivo.

3. El código utiliza un bloque `with` para abrir el archivo "guests.txt" en modo de lectura (`"r"`) y lee su contenido
línea por línea. Cada línea se agrega a "temp_list" después de eliminar los caracteres de nueva línea (`"\n"`) utilizando `strip()`.

4. Luego, se abre nuevamente el archivo "guests.txt", pero esta vez en modo de escritura (`"w"`) en un bloque `with` diferente.

5. `for name in temp_list:`: Se recorre la lista "temp_list", que contiene los nombres de los invitados del archivo original.

6. `if name not in checked_out:`: Se verifica si el nombre actual (`name`) no está en la lista "checked_out", lo que significa
que el invitado no se ha retirado.

7. `guests.write(name + "\n")`: Si el nombre no está en la lista "checked_out", se escribe en el archivo "guests.txt" seguido
de un carácter de nueva línea (`"\n"`), lo que agrega el nombre nuevamente al archivo.

8. Finalmente, se abre el archivo "guests.txt" una vez más en modo de lectura y se muestra cada línea en la consola utilizando
`print(line.split())`. La llamada a `split()` divide cada línea en palabras (separadas por espacios) y las muestra como una lista.

El resultado de este código será mostrar la lista actualizada de invitados en la consola, después de haber eliminado los nombres
que están en la lista "checked_out". Los nombres se mostrarán como listas de palabras divididas por espacios."""




# Run the following code to check whether Bob and Andrea are still checked in.
guests_to_check = ['Bob', 'Andrea', 'Sam']
checked_in = []

with open("guests.txt", "r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

"""El código que proporcionaste parece ser un programa para verificar si ciertos invitados están registrados (han realizad
check-in) en el archivo "guests.txt". Aquí está el desglose del código:

1. `guests_to_check = ['Bob', 'Andrea']`: Se define una lista llamada "guests_to_check" que contiene los nombres de los
invitados que se desean verificar si están registrados (han realizado check-in).

2. `checked_in = []`: Se crea una lista vacía llamada "checked_in" que se utilizará para almacenar temporalmente los
nombres de los invitados del archivo "guests.txt".

3. El código utiliza un bloque `with` para abrir el archivo "guests.txt" en modo de lectura (`"r"`) y lee su contenido
línea por línea. Cada línea se agrega a la lista "checked_in" después de eliminar los caracteres de nueva línea (`"\n"`) utilizando `strip()`.

4. Luego, el código recorre la lista "guests_to_check" en un bucle `for check in guests_to_check:`.

5. `if check in checked_in:`: Para cada nombre en "guests_to_check", se verifica si ese nombre está presente en la lista
"checked_in" (lo que significa que el invitado ha realizado check-in y está en el archivo "guests.txt").

6. Dependiendo del resultado de la verificación, se muestra un mensaje en la consola indicando si el invitado está registrado
("checked in") o no está registrado ("not checked in").

El resultado de este código será una serie de mensajes en la consola que indicarán si los invitados en la lista
"guests_to_check" han realizado check-in o no, en función de los nombres encontrados en el archivo "guests.txt". Esto es
útil para verificar la asistencia de invitados específicos."""


import os
os.path.getsize("guests.txt")

import datetime
timestamp = os.path.getmtime("guests.txt")
datetime.datetime.fromtimestamp(timestamp)
