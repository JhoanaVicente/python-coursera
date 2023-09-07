"""Itere sobre los pares clave y valor de un diccionario usando un bucle for con el método Dictionary.items() para
calcular la suma de los valores en un diccionario. Esta funcion devuelve el tiempo
total con los minutos representados como decimales (ejemplo: 1 hora 30 minutos= 1,5)
para todo el tiempo del usuario final gastado accediendo a un servidor en un dia determinado."""

def sum_server_use_time(Server):
    total_use_time = 0.0
    for key, value in Server.items():
        total_use_time += Server[key]
    return round(total_use_time, 2)

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer)) # Should print 20.1

"""Esta función, `sum_server_use_time`, calcula la suma total del tiempo de uso del servidor a partir de un diccionario que
almacena los tiempos de uso de diferentes usuarios. Aquí está lo que hace en cada paso:
1. `def sum_server_use_time(Server):`: Esto define la función llamada `sum_server_use_time` que toma un argumento llamado
`Server`, que se espera que sea un diccionario.
2. `total_use_time = 0.0`: Inicializa una variable `total_use_time` con un valor de punto flotante (número decimal) de `0.0`.
Esta variable se utilizará para acumular la suma de los tiempos de uso.
3. `for key, value in Server.items():`: Comienza un bucle `for` que itera a través de los elementos del diccionario `Server`.
`key` representa la clave (nombre del usuario en este caso) y `value` representa el valor asociado (tiempo de uso en horas) en el diccionario.
4. `total_use_time += Server[key]`: En cada iteración del bucle, agrega el valor actual del tiempo de uso (`Server[key]`) al `total_use_time`.
5. `return round(total_use_time, 2)`: Después de completar el bucle, la función devuelve el `total_use_time` redondeado
a 2 decimales utilizando la función `round()`.

En este caso, estás pasando el diccionario `FileServer` como argumento a la función `sum_server_use_time`, que contiene
los tiempos de uso de diferentes usuarios. La función itera a través de este diccionario, suma todos los tiempos de uso y
devuelve la suma total redondeada a dos decimales. La suma total debería ser `20.1`, como se espera en la salida del último `print()`.

Espero que esta explicación te ayude a entender la función y su funcionamiento."""
