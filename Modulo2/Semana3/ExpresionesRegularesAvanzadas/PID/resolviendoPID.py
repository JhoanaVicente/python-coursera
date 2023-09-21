import re

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
            return ""
    return result.group(1)
log = "99 elephants in a [cage]"
print(extract_pid(log))

print(extract_pid("99 elephants in a [cage]")) # DEVUELVE UNA CADENA VACIA, PERO LO TUVE QUE MODIFICAR PORQUE ME SALIA ERROR, ABAJO LA DESCRIPCION

"""La corrección es reemplazar result[1] por result.group(1). La función search de la biblioteca re devuelve un objeto Match
y para obtener el valor capturado en el grupo de captura (los dígitos entre paréntesis), debes usar el método group(1) en
lugar de indexar el objeto result como si fuera una lista. Con esta corrección, tu función extract_pid debería funcionar
correctamente y extraer el PID de la línea de registro."""
