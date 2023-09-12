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
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results.
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables,
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK.
    temp_apples = you.apples
    you.apples = me.apples
    me.apples =  temp_apples
    return you.apples, me.apples
"""ME AYUDO PAMELA Y ME DIJO QUE: ESTA BIEN LA VARIABLE Y QUE LO QUE SI TENIAMOS QUE HACER
ES LLAMARLA EN LA LINEA 23 QUE ERS POR ESO QUE NO ME SALIA BIEN"""

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
