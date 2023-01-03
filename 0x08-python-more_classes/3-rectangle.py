#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Represent a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the class
        Args:
            width: integer input
            height: integer input
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A getter function for the width
        Returns:
            The width of the reactangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A setter function for the width
        Args:
            value: integer input
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A getter function for the height
        Returns:
            the height of the reactangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A setter fucniton for the width
        Args:
            value: integer input
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle
        Returns:
            the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the rectangle
        Returns:
            the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Define the print() representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for i in range(0, self.__height):
                [print("#", end="") for i in range(0, self.__width)]
                if i != self.__height - 1:
                    print("")
        return ("")
