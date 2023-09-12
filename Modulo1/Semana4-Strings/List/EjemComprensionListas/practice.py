def squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""En este código, estamos utilizando una comprensión de lista para generar una lista de los cuadrados de los números en
el rango desde start hasta end. Aquí está cómo funciona:
range(start, end + 1): Esto crea un rango de números desde start hasta end, incluyendo start pero excluyendo end + 1.
[x ** 2 for x in range(start, end + 1)]: Para cada número x en el rango generado, calculamos su cuadrado utilizando el
operador de exponente ** y luego agregamos ese cuadrado a la lista resultante.
Entonces, cuando llames a la función squares(start, end), te devolverá una lista de los cuadrados de los números en el
rango desde start hasta end."""




