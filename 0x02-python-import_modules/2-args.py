#!/usr/bin/python3
import sys
print("{} argument:".format(len(sys.argv)-1))
for i in range(len(sys.argv)):
    if i == 0:
        continue
    else:
        print("{}: {}".format(i, sys.argv[i]))
