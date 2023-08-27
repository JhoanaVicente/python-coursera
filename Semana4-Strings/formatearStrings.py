"""Para formatear la cadena de acuerdo a tus requerimientos, puedes usar el método format de la cadena en Python.
Aquí tienes la función student_grade:

def student_grade(name, grade):
    return "{} recibió un {}% en el examen.".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))"""



"""Ejemplo:

def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))"""



"""El método de formato devuelve una copia de la cadena donde los marcadores de posición {} han sido reemplazados por los
valores de las variables. Estas variables se convierten en cadenas si aún no lo eran. Los marcadores de posición vacíos
se reemplazan por las variables pasadas al formato en el mismo orden.

example = "format() method"
formatted_string = "this is an example of using the {} on a string".format(example)
print(formatted_string)"""



"""Si los marcadores de posición indican un número, se reemplazan por la variable correspondiente a ese orden (comenzando en cero):

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)"""





print(formatted_string)
