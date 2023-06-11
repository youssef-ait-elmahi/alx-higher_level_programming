#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if sentence == '':
        return (0, None)
    else:
        first_c = sentence[0]
        return (size, first_c)
