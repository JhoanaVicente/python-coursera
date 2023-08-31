# Se utilizan para organizar elementos en colecciones, puedes usar diferentes
# tipos de datos: cadenas, enteros, flotadores, tuplas, etc
# Al almacenar valores en un diccionario, la clave se especifica primero, seguida del valor correspondiente, separado por dos puntos.
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

# Averiguamos cuantos archivos de texto hay en el diccionario (txt)
file_counts["txt"]

# Para saber si una palabra esta contenida en el dicionario (in)
"jpg" in file_counts
"html" in file_counts

# Añadir un recuento
file_counts["cfg"] = 8
print(file_counts)

# Agregar una clave que ya existe, se reemplaza
file_counts["csv"] = 17
print(file_counts)

# Eliminar
del file_counts["cfg"]
print(file_counts)
