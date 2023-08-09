#!/usr/bin/python3
"""
This rectangle module inherits from the base class form the previous base.py file
Rectangle inherits from Base
"""
from models.base import Base
class Rectangle(Base):
    """
    The Rectangle class inherits from the Base class and represents a rectangle
    with width, height, and position attributes.
    
    Attributes:
        id (int): An identifier assigned by the Base class constructor.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x-coordinate of the top-left corner of the rectangle
            y (int): The y-coordinate of the top-left corner of the rectangle
            id (int): A unique identifier for the instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if isinstance(value, int) and value > 0:
            self.__width = value
        else:
            raise ValueError("Width must be a positive integer")
        
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value > 0:
            self.__height = value
        else:
            raise ValueError("Height must be a positive integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self.__x = value
        else:
            raise ValueError("X must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self.__y = value
        else:
            raise ValueError("Y must be an integer")
