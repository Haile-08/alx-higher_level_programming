#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            n = ord(i) - 32
        else:
            n = ord(i)
        print('{:c}'.format(n), end='')
    print('')
