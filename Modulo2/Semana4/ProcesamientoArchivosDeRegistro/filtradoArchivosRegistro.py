import re

def show_time_of_pid(line):
  pattern = r"(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*\[(\d+)\]"
  result = re.search(pattern, line)
  return f"{result.group(1)} pid:{result.group(2)}"

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


"""1. Importamos el módulo `re` que nos permite trabajar con expresiones regulares en Python.

2. Definimos una función llamada `show_time_of_pid` que toma una línea como entrada.

3. Creamos una variable `pattern` que contiene la expresión regular. La expresión regular tiene dos grupos de captura:
   - `(\w{3} \d{1,2} \d{2}:\d{2}:\d{2})`: Este grupo captura la fecha y hora en el formato "Jul 6 14:01:23".
   - `(\d+)`: Este grupo captura el número de proceso (PID) entre corchetes.

4. Usamos `re.search(pattern, line)` para buscar coincidencias de la expresión regular en la línea dada. Esto nos
devolverá un objeto "match" si se encuentra una coincidencia.

5. Luego, utilizamos `result.group(1)` para obtener el primer grupo de captura, que es la fecha y hora, y `result.group(2)`
para obtener el segundo grupo de captura, que es el PID.

6. Finalmente, retornamos una cadena formateada que combina la fecha y hora con "pid:" y el PID. Esto crea la salida
en el formato deseado.

El código completo se utiliza para procesar líneas de registro que contienen información de fecha, hora y PID y formatearlas
en el estilo "Jul 6 14:01:23 pid:29440". Las llamadas de ejemplo a la función demuestran cómo funciona para diferentes
líneas de registro."""

