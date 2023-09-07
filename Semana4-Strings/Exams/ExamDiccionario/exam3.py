"""LO HICE SOLITA CON AYUDA DE GUIAESTUDIO2 ...QUE ALEGRIA:"""

def add_prices(basket):
    total = 0
    for key, value in basket.items():
        total += value
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffe": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))



"""La función update_wardrobe toma el diccionario wardrobe y el diccionario new_items y utiliza el método update para agregar
los elementos de new_items a wardrobe. Después de llamar a la función, puedes imprimir wardrobe para ver el resultado actualizado.
def update_wardrobe(wardrobe, new_items):"""

def update_wardrobe(wardrobe, new_items):
    wardrobe.update(new_items)

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}

update_wardrobe(wardrobe, new_items)

print(wardrobe)

