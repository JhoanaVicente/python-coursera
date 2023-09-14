"""También puede utilizar condicionales con listas por comprensión para crear declaraciones aún más complejas y poderosas.
Puede hacer esto agregando una declaración if al final de la lista de comprensión. Por ejemplo, [ x for x in range(1,101)
if x % 10 == 0 ] genera una nueva lista que contiene todos los números enteros divisibles por 10 de 1 a 100. La declaración
if evalúa cada valor en el rango de 1 a 100 a compruebe si es divisible por 10. Si lo es, el número se agrega a una nueva lista."""

### List Comprehension with Conditional Statement
print("List comprehension result:")
print([x for x in range(1, 101) if x % 10 == 0])

### Long form for loop with nested if-statement
print("Long form code result:")
my_list = []
for x in range(1, 101):
  if x % 10 == 0:
    my_list.append(x)
print(my_list)

# Click Run to observe the two results.

"""Las listas por comprensión pueden ser realmente poderosas, pero también pueden ser complejas, lo que resulta en un código
difícil de leer. Tenga cuidado al usarlos, ya que podría dificultar que otra persona que mire su código comprenda fácilmente
lo que está haciendo. Es una buena práctica agregar comentarios descriptivos sobre cualquier lista por comprensión utilizada
en su código. Esto ayuda a comunicar el propósito de la lista por comprensión a otros codificadores. Los comentarios también
le ayudarán a recordar el objetivo del código cuando realice futuras adiciones y mantenimiento de código."""
