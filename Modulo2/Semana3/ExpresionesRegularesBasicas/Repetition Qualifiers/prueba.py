import re

def check_punctuation(text):
  result = re.search(r"\.$|!$|\?$|,$", text)
  return result is not None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

"""En este código, la expresión regular r"\.$|!$|\?$|,$" busca si la cadena de texto termina con ".", "!", "?", o ",". Cada
uno de estos elementos se separa con el operador "|" que actúa como un OR lógico. Si se encuentra alguno de estos signos
de puntuación al final de la cadena, la función check_punctuation devolverá True, de lo contrario, devolverá False."""
