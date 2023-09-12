def pig_latin(text):
  say = ""
  words = text.split()
  for word in words:
    say += word[1:] + word[0] + "ay" + " "
  return say.strip()

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
