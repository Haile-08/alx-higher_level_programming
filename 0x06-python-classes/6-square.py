#!/usr/bin/python3
"""Define a class named square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initalize the square class
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
        """a getter method for size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """a setter method for size value
        args:
            value: input value to set
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """a getter method for position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """a setter method for positon vlaue
        args:
            value: input value to set
        """
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return: the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print the # character in stdout"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                if self.__position[1] > 0:
                    print("", end="")
                else:
                    for i in range(self.__position[0]):
                        print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")
