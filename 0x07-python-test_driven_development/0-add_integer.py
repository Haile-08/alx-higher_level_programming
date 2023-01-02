#!/usr/bin/python3
"""
    Add two number
"""
def add_integer(a, b=98):
    """Add two numbers
    args:
        a: an integer or float
        b: an integer or float
    Returns:
        the sum of two integer arguments
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
