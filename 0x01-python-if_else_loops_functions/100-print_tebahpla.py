#!/usr/bin/python3
ul = 0
for i in range(90, 64, -1):
    if ul == 0:
        i = i + 32
        ul = 1
    else:
        ul = 0
    print("{:c}".format(i), end="")
