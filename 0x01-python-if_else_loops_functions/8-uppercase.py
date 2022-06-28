#!/usr/bin/python3
def uppercase(str):
    out = range(len(str))
    for i in str:
        upper = ord(i) + 32
        out.append(chr(upper))
    return out
