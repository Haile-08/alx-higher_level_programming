#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a class named square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class
        args:
            size: the size of the square
            position: the position of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position
    @property
    def size(self):
        """a getter method for size"""
        return self.__size
    @size.setter
    def size(self, value):
        """a setter method for size
        args:
            value: the input value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        """a getter method for position"""
        return self.__position
    @position.setter
    def position(self, value):
        """a setter method for position
        args:
            value: the input value
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return: the area of the square"""
        return self.__size * self.__size
    
    def my_print(self):
        """Method to print #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")
    def __str__(self):
        value = []
        if self.__size == 0:
            value.append("")
        else:
            for i in range(self.__size):
                val = []
                for i in range(self.__position[0]):
                    val.append(" ")
                for i in range(self.__size):
                    val.append("#")
                value.append(val)
                val.clear()
        return ("\n".join(value))
