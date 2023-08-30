#!/usr/bin/python3
""" defines a square by: (based on 2-square.py)"""


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """stimulates square
        Args:
           size: size  of square"""

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """finds area of square returns: the area of the square """

        return self.__size ** 2
