#!/usr/bin/env python3

import random

def greeting():
    name = input("Hello!, What's your name?")
    number = random.randint(1,101)
    print("Hello " + name + ", your random number is " + str(number))

greeting()


"""1. `#!/usr/bin/env python3`: Esta línea es una convención llamada "shebang". Indica que el programa debe ser ejecutado
# utilizando Python 3. Cuando ejecutas este archivo, el sistema operativo utiliza Python 3 para interpretar el código que sigue.

2. `import random`: Importa el módulo `random`, que proporciona funciones para generar números aleatorios.

3. `def greeting()`: Define una función llamada `greeting()`. Las funciones son bloques de código reutilizables que se
ejecutan cuando son llamados.

4. `name = input("Hello!, What's your name?")`: Esta línea solicita al usuario que introduzca su nombre a través de la
entrada estándar (teclado) y almacena la entrada en la variable `name`.

5. `number = random.randint(1,101)`: Genera un número entero aleatorio entre 1 y 100 (inclusive) y lo almacena en la
variable `number`.

6. `print("Hello " + name + ", your random number is " + str(number))`: Imprime un mensaje de saludo que incluye el
nombre del usuario y el número aleatorio. Para imprimir todo como una cadena, se concatenan las partes del mensaje
usando el operador `+`. La función `str(number)` se utiliza para convertir el número aleatorio en una cadena para que
pueda concatenarse con las cadenas.

7. `greeting()`: Llama a la función `greeting()`, lo que inicia la ejecución del código dentro de esa función.

Cuando ejecutas el programa, te pedirá que ingreses tu nombre, generará un número aleatorio y luego imprimirá un mensaje
de saludo que incluye tu nombre y el número aleatorio. La función `str()` se usa para convertir el número en una cadena
para que se pueda concatenar con las otras cadenas en el mensaje. Esto es necesario porque solo se pueden concatenar
cadenas con cadenas en Python."""
