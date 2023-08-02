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
        __int__(self, size=0):Initializes a Square instance with a given a size(defualt is 0)
        my_print(self):Print the square pattern using '#'
    """
    def __init__(self, size):
        """
        Constructor for Square class
        Args:
            __size(int):The size of the (default is 0)
        """
        self.__size = size
    def area(self):
        return self.__size ** 2 #finding the area of the square
    def perimeter(self):
        return 4 * self.__size
    def get_size(self):
        return self.__size #using getters to access__size since it is private
    def set_size(self, current_size):
        self.__size = current_size #using setters to modify __size

        