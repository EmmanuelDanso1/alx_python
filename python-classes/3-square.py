#!/usr/bin/python3
"""
This module defines Square class, which represents a square shape
Square:
    A class to create and manipulate square objects

"""
class Square:
    """
    This represent a Square root
    __size(int): The size of the Square

    Methods:
        __init__(self, size=0):Initializes a Square instance with a given a size(default is 0)
        my_print(self):Print the square pattern using '#'
    """
    def __init__(self, size=0):
        """
        Constructor for Square class
        Args:
            __size(int):The size of the (default is 0)
        """
        self.size = size

    @property #decorator allows us access the size attribute
    def size(self):
        return self.__size

    @size.setter #decorator allows us to set the value of the size about
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
