import re

def change_letter(sentence:str) ->str:
    new_sentence = ""
    for i, letter in enumerate(sentence):

        if i == 0:
            new_sentence += letter.upper()
            continue
        if not re.match("[a-zA-Z]",letter):
            new_sentence += letter
            continue
        if new_sentence[-1].isupper() or not re.match("[a-zA-Z]",new_sentence[-1]):
            new_sentence += letter.lower()
        elif new_sentence[-1].islower() or not re.match("[a-zA-Z]",new_sentence[-1]):
            new_sentence += letter.upper()


    return new_sentence
