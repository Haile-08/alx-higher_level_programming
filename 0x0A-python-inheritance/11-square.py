#!/usr/bin/python3
"""Define a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprsent a Square"""

    def __init__(self, size):
        """Initilize a class
        Args:
            size: integer input
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

