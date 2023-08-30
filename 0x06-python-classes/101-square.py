#!/usr/bin/python3
""" this module create the class Square"""


class Square:
    """ Class Square with constuctor method"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class Square
        Arg
            size: size to initializate __size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def __str__(self):
        """Create the string of the squar
        Returns:
            The string"""

        string = ""
        if self.size == 0:
            return ("")
        else:
            string += "\n" * self.__position[1]
            for j in range(self.__size):
                string += " " * self.__position[0]
                for i in range(self.__size):
                    string += "#"
                if j < self.__size - 1:
                    string += "\n"
        return string

    def area(self):
        """
        Calculate the area of a square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square checking position
        """

        if self.size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """
        getter function of position
        Returns:
            position of square
        """
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """
        getter function of size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        setter function of attribute size
        Args:
            value: value for __size
        """
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
