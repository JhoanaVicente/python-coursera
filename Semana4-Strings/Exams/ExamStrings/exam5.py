# Super feliz porque este lo hize 100% sola y viendo la carpeta formatearString4

def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = len(old)
        new_sentence = sentence[:-i] + sentence[-i:].replace(old, new)
        return new_sentence
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
