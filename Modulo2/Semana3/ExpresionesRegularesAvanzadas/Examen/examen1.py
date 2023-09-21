"""Para transformar el número de teléfono en cada registro, necesitas usar una expresión regular para buscar el número de
teléfono en el formato sin el código de país y luego reemplazarlo con el formato que incluye el código de país. Puedes
hacerlo de la siguiente manera:"""

import re

def transform_record(record):
    # Utilizamos \b para asegurarnos de que el número de teléfono sea una palabra completa
    new_record = re.sub(r'\b(\d{3}-\d{3}-\d{4})\b', r'+1-\1', record)
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer

"""La expresión regular r'\b(\d{3}-\d{3}-\d{4})\b' busca números de teléfono en el formato "###-###-####" y usa \b para
asegurarse de que sea una palabra completa. Luego, en el segundo argumento de re.sub(), usamos r'+1-\1' para reemplazar
el número de teléfono con el formato "+1-###-###-####"."""
