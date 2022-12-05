#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuple_b = (len(sentence), )
        tuple_b = tuple_b + (sentence[0], )
        return tuple_b
