#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Represent a rectangle"""

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
        """A getter method for width
        Returns:
            the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A setter method for width
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
        """A getter method for height
        Returns:
            the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A setter method for height
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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Define the print() reprsentaion of the class"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            for i in range(0, self.__height):
                [print("#", end="") for j in range(self.__width)]
                if i != self.__height - 1:
                    print("")
        return ("")

    def __repr__(self):
        """Define the return of the rectangle"""
        strw = str(self.__width)
        strh = str(self.__height)
        return "Rectangle(" + strw + ", " + strh + ")"
