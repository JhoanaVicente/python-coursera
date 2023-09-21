import re
def convert_phone_number(phone):
  result = re.sub(r'\b(\d{3})-(\d{3})-(\d{4})\b', r'(\1) \2-\3', phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

"""En este código, hemos utilizado la función re.sub() para buscar números de teléfono en el formato "###-###-####" y
reemplazarlos con el formato "(###) ###-####". La expresión regular r'\b(\d{3})-(\d{3})-(\d{4})\b' busca números de
teléfono que consisten en tres grupos de tres dígitos separados por guiones. Luego, en el segundo argumento de re.sub(),
utilizamos \1, \2, y \3 para referirnos a los grupos capturados en la expresión regular y formatear el número de teléfono
correctamente."""
