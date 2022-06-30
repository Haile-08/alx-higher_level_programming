#!/usr/bin/python3
import sys
print("{:d} argument:".format(len(sys.argv)-1))
for i in range(len(sys.argv)):
    if i == 0:
        continue
    else:
        print("{:d}: {:s}".format(i, sys.argv[i]))
