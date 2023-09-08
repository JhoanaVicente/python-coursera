class Birds:
    def __init__(self):
        self.color = ""
        self.number = 4

    def count(self):
        self.number += 1

def count_and_print_birds(bird_object):
    bird_object.count()
    print(f"Number of birds: {bird_object.number}")

# Crear una instancia de la clase Birds
bluejay = Birds()
bluejay.number = 8
# Llamar a la función para contar y mostrar el número de aves
count_and_print_birds(bluejay)


# INSTANCIA Y VARIABLE
