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
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height
