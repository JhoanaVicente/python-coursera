#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything is OK!")

"""Este es un script de Python que realiza dos comprobaciones: una para verificar el uso del disco y otra para verificar el
uso de la CPU. Veamos cada parte del código:

#!/usr/bin/env python3: Esta es una línea conocida como shebang. Indica al sistema operativo que debe usar Python 3 para
# ejecutar el script. Es útil cuando ejecutas el script desde la línea de comandos.

import shutil y import psutil: Estas líneas importan dos módulos de Python que se utilizan en el script. shutil se utiliza
para obtener información sobre el uso del disco, y psutil se utiliza para obtener información sobre el uso de la CPU.

def check_disk_usage(disk): Esta función toma un argumento disk que representa una ruta al disco que deseas verificar.
Utiliza la función shutil.disk_usage(disk) para obtener información sobre el uso del disco y calcula el porcentaje de
espacio libre. Luego, devuelve True si el porcentaje de espacio libre es mayor que 20, lo que significa que el disco tiene
al menos un 20% de espacio libre.
def check_cpu_usage(): Esta función no toma argumentos y utiliza la función psutil.cpu_percent(1) para obtener el uso actual
de la CPU durante 1 segundo. Luego, devuelve True si el uso de la CPU es menor que 75, lo que significa que la CPU está
funcionando por debajo del 75% de su capacidad.

La parte final del script utiliza estas dos funciones para realizar comprobaciones. Si check_disk_usage("/") devuelve False
(lo que significa que el espacio en disco es insuficiente) o check_cpu_usage() devuelve False (lo que significa que el
uso de la CPU es alto), se imprimirá "ERROR!". De lo contrario, se imprimirá "Everything is OK!".

En resumen, este script verifica si el disco tiene al menos un 20% de espacio libre y si la CPU está funcionando por debajo
del 75% de su capacidad. Si cualquiera de estas condiciones no se cumple, se muestra un mensaje de error; de lo contrario,
muestra un mensaje de "Todo está bien". Es útil para monitorear el estado del sistema y tomar medidas en caso de problemas."""
