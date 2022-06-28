#!/usr/bin/python3
def uppercase(str):
    for i in str:
        upper = ord(i) + 32
        print("{:s}".format(upper), end='')
    print("")
