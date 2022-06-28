#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            upper = ord(i) + 32
            print("{:s}".format(chr(upper)), end='')
    print("")
