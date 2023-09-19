import re

def check_zip_code(text):
    # La expresión regular busca un código postal de EE. UU. con el formato deseado.
    pattern = r"(?<!^)\b\d{5}(?:-\d{4})?\b"

    # Busca si el patrón se encuentra en el texto proporcionado.
    result = re.search(pattern, text)

    # Devuelve True si se encuentra un código postal válido, de lo contrario, devuelve False.
    return result is not None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
