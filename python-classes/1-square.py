#!/usr/bin/python
class Square:
    #assuming the size was passed as a valid integer
    def __init__(self, size):
        self.__size = size #square class with private instance attribute __size
    def area(self):
        return self.__size ** 2 #findong the area of the square
    def perimeter(self):
        return 4 * self.__size
    def get_size(self):
        return self.__size #using getters to access__size since it is private
    def set_size(self, current_size):
        self.__size = current_size #using setters to modify __size

        