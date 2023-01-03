#!/usr/bin/python3
"""A Rectangle class"""


class Rectangle:
    """Represent a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize the class Rectangle

        Args:
            width: width integer input
            height: height integer input
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter function for width
        args:
            value: integer input
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter funciton for height
        args:
            value: integer input
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
