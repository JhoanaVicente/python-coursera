usernames = {}
name = "good_user"
usernames[name] = usernames.get(name, 0) + 1
print(usernames)

usernames[name] = usernames.get(name, 0) + 1
print(usernames)

"""Este código se utiliza para contar cuántas veces aparece un nombre de usuario en el diccionario usernames. La primera
vez que se encuentra un nombre de usuario, se crea en el diccionario con un recuento de 1, y cada vez que se encuentra
nuevamente, se incrementa el recuento en 1. Las impresiones en pantalla te muestran cómo se actualiza el diccionario a
medida que se encuentran más instancias del nombre de usuario."""







"""import re
import sys

logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result.group(1)  # Corregido aquí
        usernames[name] = usernames.get(name, 0) + 1

print(usernames)"""


