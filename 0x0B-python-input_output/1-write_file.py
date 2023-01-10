#!/usr/bin/python3
"""Define a function that write to a file"""


def write_file(filename="", text=""):
    """Write to a file
    Args:
        filename: string input
        text: string input
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return f.tell()
