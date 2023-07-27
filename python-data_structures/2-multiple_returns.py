#!/usr/bin/pyhton3
#tuples
def multiple_returns(sentence):
    len_of_string = len(sentence)
    if len_of_string > 0:
        firstCharacter = sentence[0]
    else:
        firstCharacter = None
    return len_of_string, firstCharacter
"""
sentence = "At Holberton school, I learnt C!"
len_of_string, firstCharacter = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(len_of_string, firstCharacter))
"""