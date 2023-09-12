"""Por ejemplo, [ x*2 for x in range(1,11) ] es una lista de comprensión simple. Esta única línea de código itera en un rango
de 1 a 10, multiplica cada elemento en el rango por 2 y crea una nueva lista a partir de todos los múltiplos de 2 de 2 a 20."""

### Simple List Comprehension
print("List comprehension result:")
print([x*2 for x in range(1, 11)])

### Long form for loop
print("Long form code result:")
my_list = []
for x in range(1,11):
   my_list.append(x*2)
print(my_list)

# Click Run to compare the two results.
