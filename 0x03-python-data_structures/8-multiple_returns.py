#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_a = (0, )
        tuple_a = tuple_a + (None, )
        return tupe_a
    else:
        tuple_b = (len(sentence), )
        tuple_b = tuple_b + (sentence[0], )
        return tuple_b
