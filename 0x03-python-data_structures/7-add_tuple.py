#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        zero = (0,)
        for i in range(3):
            tuple_a = tuple_a + zero
            tuple_b = tuple_b + zero
        new_tuple = ()
        for j in range(2):
            s = tuple_a[j] + tuple_b[j]
            new_tuple = new_tuple + (s,)
        return new_tuple
