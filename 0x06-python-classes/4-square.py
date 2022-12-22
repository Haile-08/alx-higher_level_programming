#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize the class.

        Args:
            size: the size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter fucntion."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.size * self.size
