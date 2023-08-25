#Bucles for con la funcion range() con el valor de fin de rango incluido
"""def count_by_10(end):
    count = ""
    for number in range(0,end+1,10):
        count += str(number) + " "
    return count.strip()

print(count_by_10(100))
# Should print 0 10 20 30 40 50 60 70 80 90 100"""

#Bucles for anidados con la funcion range() para crear una matriz de numeros
"""def matrix(initial_number, end_of_first_row):
    n1 = initial_number
    n2 = end_of_first_row+1
    for column in range(n1, n2): #bucle for creara las columnas
        for row in range(n1, n2): #Bucle for anidado creara las filas
              print(column*row, end=" ")
        print()
matrix(1, 4)
# Should print:
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16"""

# Predice el valor final de un bucle for anidado con funciones range()
for outer_loop in range(10): #Se utiliza un indice de fin de rango de 10
    for inner_loop in range(outer_loop):
        print(inner_loop)


#Bucle while para imprimir una secuencia de numeros
"""starting_number = 18 #Cuenta regresiva de 3 en 3 comenzando desde 18 y terminando en 0
while starting_number >= 0:
    print(starting_number, end=" ") #Para facilitar la lectura, se incluye espacio
    starting_number -= 3
# Should print 18 15 12 9 6 3 0"""


#Bucle while para contar el numero de digitos en un valor numerico
"""def X_figure(salary): #"El salario del CEO es de 6 cifras"
    tally = 0 #Inicializa con un numero entero
    if salary == 0: #La sentencia comprueba si la variable salario es igual a 0
        tally += 1 #Si es verdadero, incrementa el contador.
    while salary >= 1: #El bucle no se ejecuta si el salrio es 0.
        salary = salary/10 #El salario se puede dividir por 10.
        tally += 1 #Suma 1 al contador para contar el numero de veces que se ejecuta el bucle
    return tally

#Llame a la funcion X_figure con 1 parámetro, convertida en una cadena, dentro de una
#función de impresion con cadenas adicionales.
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")
# Should print"The CEO has a 7-figure salary."""""



#Utilice sentencias if-else anidadas y bucles while para contar hacia arriba o hacia atrás desde la primera variable hasta la segunda variable.
"""def elevator_floor(enter, exit):
    floor = enter
    elevator_direction = ""
    if enter > exit:
        elevator_direction = "Going down: "
        while floor >= exit:
            elevator_direction += str(floor)
            if floor > exit:
                elevator_direction += " | "
            floor -= 1
    else:
        elevator_direction = "Going up: "
        while floor <= exit:
            elevator_direction += str(floor)
            if floor < exit:
                elevator_direction += " | "
            floor += 1
    return elevator_direction

print(elevator_floor(1,4)) # Should print Going up: 1 | 2 | 3 | 4
print(elevator_floor(6,2)) # Should print Going down: 6 | 5 | 4 | 3 | 2"""
