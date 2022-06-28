#!/usr/bin/python3
for i in range(ord("a"), ord("z")):
    if chr(i) == 'q':
        continue
    elif chr(i) == 'e':
        continue
    else:
        print("{:c}".format(i), end='')
