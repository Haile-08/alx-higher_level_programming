#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    lists = sys.argv
    arg = len(lists)
    if arg != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(lists[1])
        b = int(lists[3])
        op = lists[2]
        if op == '+':
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
            sys.exit(0)
        elif op == '-':
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
            sys.exit(0)
        elif op == '*':
            print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
            sys.exit(0)
        elif op == '/':
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
            sys.exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
