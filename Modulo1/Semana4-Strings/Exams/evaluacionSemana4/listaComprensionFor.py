def increments(start, end):
    return [x for x in range(start + 2, end + 2+1)] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

"""En esta función, creamos una lista de comprensión que genera números x utilizando un bucle for. El rango del bucle for
es desde start + 2 hasta end + 2 para asegurarse de que se incluyan los valores start y end en la lista final. Luego,
cada número x generado se agrega a la lista resultante. Recordar agregar (+1) para agregar el ultimo numero a imprimir"""
