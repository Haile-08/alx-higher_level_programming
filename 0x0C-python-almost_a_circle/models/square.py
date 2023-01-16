#!/usr/bin/python3
"""Define a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initilize a class
        Args:
           size: size of the square
           x: x value of the class
           y: y value of the class
           id: id of the class
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """a getter method for size
        Retrun: the size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """A setter method for size
        Args:
            value: int input
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class attribute
        Args:
            *args: is the list of arguments - no-keyworded arguments
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
        """
        if args is not None:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """A dectionary rep
        Return: the dictionary representation of a Square
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):
        """Print reprsentaion of the class
        Return: [Square] (<id>) <x>/<y> - <size>
        """
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        return '[Square] ({}) {}/{} - {}'.format(i, x, y, w)
