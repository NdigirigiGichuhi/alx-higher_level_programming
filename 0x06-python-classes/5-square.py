#!/usr/bin/python3

"""This module define a square class"""


class Square:
    """
    This class defines a square
    """
    def __init__(self, size=0):
        """
        Args:
            size: size of one side of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Returns the length of one side of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets a value to the size argument

        Args:
            value: size of one side of the square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the area of a square
        """

        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()

        for row in range(self.__size):
            print("{}".format("#") * self.__size)
