class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    # Intercambia todas las manzanas entre "you" y "me" usando una variable temporal.
    temp_apples = you.apples
    you.apples = me.apples
    me.apples = temp_apples

def exchange_ideas(you, me):
    # Comparte todas las ideas entre "you" y "me" sumando sus ideas individuales.
    you.ideas += me.ideas
    me.ideas = you.ideas  # También podrías usar `me.ideas += you.ideas` aquí si se desea.

exchange_apples(johanna, martin)
print("Johanna tiene {} manzanas y Martin tiene {} manzanas".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna tiene {} ideas y Martin tiene {} ideas".format(johanna.ideas, martin.ideas))



"""En este código:
exchange_apples intercambia todas las manzanas entre "you" y "me" usando una variable temporal para evitar perder ningún valor.

exchange_ideas comparte todas las ideas entre "you" y "me" sumando sus ideas individuales.

Luego, llamamos a ambas funciones para realizar el intercambio de manzanas e ideas y finalmente imprimimos las cantidades
de manzanas e ideas de Johanna y Martin después del intercambio."""
