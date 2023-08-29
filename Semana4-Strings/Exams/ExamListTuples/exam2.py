def pig_latin(text):
  say = ""
  words = text.split()
  for word in words:
    if word [0] in"aeiou":
      pig_word = word + "ay"
    else:
      pig_word = word[1:] + word[0] + "ay"
    say += pig_word + " "
  return say.strip()

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


"""En este código:
text.split() divide el texto en una lista de palabras.
Para cada palabra en la lista words:
Si la primera letra de la palabra está en "aeiou" (es una vocal), simplemente se agrega "ay" al final para formar la versión en Pig Latin.
Si la primera letra de la palabra es una consonante, se reorganiza la palabra colocando la primera letra al final y
luego se agrega "ay" al final para formar la versión en Pig Latin.
Las palabras convertidas en Pig Latin se concatenan en la cadena say, separadas por espacios.
say.strip() se utiliza para eliminar cualquier espacio en blanco adicional al principio o al final de la cadena.
La función pig_latin(text) finalmente devuelve la cadena en Pig Latin."""
