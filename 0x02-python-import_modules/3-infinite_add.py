#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lists = sys.argv
    s = 0
    for i in lists[1:]:
        s = s + int(i)
    print('{:d}'.format(s))
