import re

def check_web_address(text):
    pattern = r"^(http://|https://|www\.)?[a-zA-Z0-9_-]+\.[a-zA-Z]{2,}$"
    result = re.search(pattern, text)
    return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

"""Con esta expresión regular, la función check_web_address verificará si la cadena proporcionada se parece a una dirección
web válida. El patrón busca lo siguiente:

^: El comienzo de la cadena.
(http://|https://|www\.)?: Un grupo opcional que puede contener "http://", "https://", o "www." al principio.
[a-zA-Z0-9_-]+: Cualquier combinación de letras, dígitos, guiones bajos (_) y guiones (-) en el dominio.
\.: Un punto literal que separa el dominio de la extensión.
[a-zA-Z]{2,}: Dos o más letras para la extensión del dominio (por ejemplo, com, org, us, etc.).
$: El final de la cadena.
Los ejemplos de llamadas a la función verificarán si las cadenas proporcionadas son direcciones web válidas según este patrón."""
