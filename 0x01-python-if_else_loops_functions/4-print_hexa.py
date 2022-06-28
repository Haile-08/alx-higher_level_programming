#!/usr/bin/python3
a = 0x0
b = 0x62
number = list(range(0, 98))
hexa = list(range(a, b))
for i in range(len(number)):
    print(f"{number[i]} = {hex(hexa[i])}")
