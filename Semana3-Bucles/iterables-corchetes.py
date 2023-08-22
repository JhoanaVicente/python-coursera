#Si queremos ir de cero a 25 usamos la funcion rango
for x in range (5):
    print(x)

#Pero si quiero iterar, debe ser una lista y escribirla en corchetes
for x in [5]:
   print(x)

#Recibe una loista por parámetros e iter sobre la lista
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends(['Taylor', 'Luisa', 'Jaamal', 'Eli'])

#Las cadenas son iterables no las comillas
greet_friends("Barry")
