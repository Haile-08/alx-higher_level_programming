#!/usr/bin/python3
"""Define the class rectangle"""


class Rectangle:
    """Represent the rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Iinitialize the class
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
        type(self).number_of_instances += 1

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
         """A setter method for the height
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
        """Define the print() of class"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            strv = self.number_of_instances
            for i in range(self.__height):
                [print(strv, end="") for i in range(self.__width)]
                if i != self.__height - 1:
                    print("")
        return ("")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger rectangle based on area
        Args:
            rect_1: object of the class
            rect_2: object of the class
        Returns:
            the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """New Rectangle instance
        Returns:
            a new Rectangle instance
        """
        return (cls(size, size))

    def __repr__(self):
        """Return the class instance"""
        strw = str(self.__width)
        strh = str(self.__hight)
        return "Rectangle(" + strw + ", " + strh + ")"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
