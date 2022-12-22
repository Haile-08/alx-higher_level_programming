#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """initalize the class.

        args:
            size: the size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """A getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        """A setter method.
        args:
            vlaue: the value to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """print a #."""
        if self.__size > 0:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")
        elif self.__size == 0:
            print("")
