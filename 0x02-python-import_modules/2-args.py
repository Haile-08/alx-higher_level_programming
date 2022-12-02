#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lists = sys.argv
    print('{:d} argument:'.format(len(lists) - 1))
    for i in range(1, len(lists)):
        print('{:d}: {}'.format(i, lists[i]))
