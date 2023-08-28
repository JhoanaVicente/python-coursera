"""Utilice el método .replace() para reemplazar parte de una cadena.
Utilice la función len() para obtener el número de posiciones de índice en una cadena.
Corta una cadena en una posición de índice específica.


Esta función llamada `replace_date` reemplaza una fecha específica en una cadena `schedule` con otra fecha proporcionada.
Aquí tienes el desglose de la función y los ejemplos:

1. `def replace_date(schedule, old_date, new_date):`: Define la función `replace_date` que toma tres argumentos:
`schedule` (cadena de programación), `old_date` (fecha antigua a reemplazar) y `new_date` (nueva fecha que se usará para reemplazar la antigua).

2. `if schedule.endswith(old_date):`: Esta condición verifica si la cadena `schedule` termina con la fecha antigua `old_date`.

3. Si la condición es verdadera, se ejecutan los siguientes pasos:
   - `p = len(old_date)`: Calcula la longitud de la fecha antigua.
   - `new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)`: Crea una nueva cadena llamada `new_schedule`
      al tomar la porción de `schedule` que excluye la fecha antigua y luego agrega la porción final de `schedule` que contiene la fecha antigua reemplazada por la nueva fecha.

4. Finalmente, la función devuelve la cadena `new_schedule` si la condición es verdadera (la fecha antigua estaba al final
de la cadena). Si la condición no se cumple, la función simplemente devuelve la cadena original.

5. Los ejemplos `print(replace_date(...))` al final llaman a la función con diferentes cadenas de programación y fechas,
y muestran los resultados después de aplicar el reemplazo si es aplicable.

En resumen, la función reemplaza una fecha antigua específica al final de una cadena de programación con una nueva fecha,
si la fecha antigua coincide con el final de la cadena."""

def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):
        p = len(old_date)
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule
    return schedule

print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May"))
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June"))
# Should display "The convention is scheduled for June"
