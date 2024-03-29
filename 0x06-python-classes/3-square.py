#!/usr/bin/python3
"""Difine a class Square."""


class Square:
    """A class named Square"""

    def __init__(self, size=0):
        """ __init__ method

        args:
            size: the size of the square
        Return:
            none
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """ Return the current area of the square"""
        return (self.__size * self.__size)
