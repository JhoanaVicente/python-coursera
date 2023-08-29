def guest_list(guests):
	for guest in guests:
		name, age, occupation = guest
		print("{} is {} years old and works as {}".format(name, age, occupation))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""


"""En este código:
El bucle for guest in guests: itera a través de cada elemento en la lista guests, que contiene tuplas con la información de cada invitado.
En cada iteración, desempaquetamos la tupla utilizando name, age, occupation = guest, lo que nos permite acceder a los valores individuales de nombre, edad y ocupación.
Luego, utilizamos .format() para formatear una cadena que muestra la información del invitado de la manera deseada.
Finalmente, la función guest_list(guests) imprimirá la información de cada invitado en el formato especificado.
El resultado impreso coincidirá con la salida esperada que proporcionaste."""
