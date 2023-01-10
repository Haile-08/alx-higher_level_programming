#!/usr/bin/python3
"""Define a funciton that appends a string to file"""


def append_write(filename="", text=""):
    """Append to file
    Args:
        filename: string input
        text: string input
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
