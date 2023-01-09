#!/usr/bin/python3
"""Define a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reprsent a class Rectangle"""

    def __init__(self, width, height):
        """Initialize a class
        Args:
            width: integer input
            height: integer input
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Print represntation of the class"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
