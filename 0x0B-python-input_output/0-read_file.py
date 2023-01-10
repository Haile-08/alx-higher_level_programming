#!/usr/bin/python3
"""Define a function that read file"""


def read_file(filename=""):
    """Read file
    Args:
        filename: string input
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
