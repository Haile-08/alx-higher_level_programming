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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
