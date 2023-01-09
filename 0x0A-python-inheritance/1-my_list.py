#!/usr/bin/python3
"""Define our own mylist"""


class MyList(list):
    """Represent a custom list"""

    def __init__(self, a=[]):
        if not isinstance(a, list):
            raise TypeError("Input should be a list")
        for i in a:
            if type(i) not in [int, float]:
                raise ValueError("Element should be int or float")
        for i in a:
            self.append(i)

    def print_sorted(self):
        """Print the sorted list"""
        print(sorted(self))
