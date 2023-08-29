"""Si tenemos una variable de cadena llamada WEATHER = "RAINFALL", para imprimir la subcadena "RAIN" o todos los caracteres
antes de la "f", puedes utilizar la técnica de "slicing" (rebanado). Aquí tienes cómo lograrlo:

WEATHER = "RAINFALL"

# Imprimir la subcadena "RAIN"
print(WEATHER[:4])  # Esto imprimirá "RAIN"

# Imprimir todos los caracteres antes de la "f"
print(WEATHER[:WEATHER.index("f")])  # Esto imprimirá "RAIN"



Ambas opciones lograrán el resultado deseado:
WEATHER[:4] cortará la cadena para incluir caracteres desde el inicio (índice 0) hasta, pero sin incluir, el índice 4. Esto extraerá la subcadena "RAIN".

WEATHER.index("f") encuentra el índice de la primera aparición del carácter "f" en la cadena. Usar este índice en el corte
(WEATHER[:WEATHER.index("f")]) incluirá caracteres desde el inicio de la cadena hasta, pero sin incluir, el índice de "f",
efectivamente dándote todos los caracteres antes de "f", que en este caso es "RAIN"."""
