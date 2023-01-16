#!/usr/bin/python3
"""Define a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Reprsent a Recatangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x axis
            y: y axis
            id: id of the class
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """A width getter method
        Return: the width of the class
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A setter method
        Args:
            value: integer input
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """A height getter method
        Return: the height of the class
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A height setter method
        Args:
            value: integer input
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """A x getter method
        Return: the x value of the class
        """
        return self.__x

    @x.setter
    def x(self, value):
        """A x setter method
        Args:
            value: interger input
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """A y getter method
        Return: the x value of the class
        """
        return self.__y

    @y.setter
    def y(self, value):
        """A y setter method
        Args:
            value: integer input
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Area of the rectangle
        Return: area value
        """
        return self.__width * self.__height

    def display(self):
        """Print to stdout"""
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Print repsentaion of the class"""
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h)
