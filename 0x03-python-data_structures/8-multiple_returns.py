#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length < 1:
        return None
    tuple_return = (length, sentence[0])
    return tuple_return
