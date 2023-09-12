"""La función factorial calcula el factorial de un número dado n. Comienza con un valor inicial result igual a n,
y luego multiplica este resultado por los números decrecientes desde n-1 hasta 1 utilizando un ciclo while. Finalmente, devuelve
el resultado del factorial calculado."""

"""def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1"""



"""En este código, el bucle externo controla el número de filas que se imprimirán, y el bucle interno controla el número de asteriscos
que se imprimirán en cada fila. La variable x en el bucle externo representa el número de la fila actual (comenzando desde 0), y el bucle
interno itera desde 0 hasta x para imprimir los asteriscos correspondientes a esa fila."""

"""def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(rows):
        # Complete the inner loop range to control the number of
        # asterisks per row
        for y in range(x + 1):
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()

rows_asterisks(5) # Should print the asterisk rows shown above"""



""""#Esta funcion debe realizar una cuenta regresiva
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:# Complete the while loop
            return_string += str(start) # En cada iteración del bucle, el número actual start se agrega al string de retorno utilizando return_string += str(start).
            if start > stop:
                return_string += "," #Luego, se verifica si start es mayor que stop y se agrega una coma al string de retorno si no es el último número. Esto evita que se coloque una coma después del último número.
            start -= 1
    else:
        return_string = "Counting up: "
        while start <= stop: # Complete the while loop
            return_string += str(start)# Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            start += 1 # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5" """



"""#El bucle for se utiliza para iterar a través de un rango de números que va desde minimum hasta maximum + 1 (inclusive). 
def all_numbers(minimum, maximum):
    return_string = ""  # Inicializa la variable como una cadena vacía
    for num in range(minimum, maximum + 1): # Se incluye el ultimo numero
        return_string += str(num) + " "
    return return_string.strip()  # Este comando .strip eliminará el espacio final " " al final de "return_string".

print(all_numbers(2, 6))   # Debería ser 2 3 4 5 6
print(all_numbers(3, 10))  # Debería ser 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # Debería ser -1 0 1
print(all_numbers(0, 5))   # Debería ser 0 1 2 3 4 5
print(all_numbers(0, 0))   # Debería ser 0"""



"""for sum in range(5):
    sum += sum
    print(sum)"""


"""#Bucle anidado
for x in range(10):
    for y in range(x):
        print(y)"""




"""El bucle que has escrito actualmente será infinito porque estás estableciendo x en 1 en cada iteración dentro del bucle.
Esto hace que x siempre sea 1 y nunca se incrementa, lo que significa que la condición x <= 10 siempre se cumple. Para solucionarlo,
necesitas incrementar x en cada iteración. Aquí tienes el código corregido:"""
def count_to_ten():
  x = 1
  while x <= 10:
    print(x)
    x += 1
"""En este código, he agregado x += 1 dentro del bucle para incrementar el valor de x en 1 en cada iteración. De esta manera,
x pasará por los números del 1 al 10 y luego el bucle terminará."""

count_to_ten()
