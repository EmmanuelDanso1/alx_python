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
        """Setting the width of the rectangle."""
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

    #def display(self):
        """
        Print a visual representation of the rectangle using the character '#'.
        """
        #for _ in range(self.height):
            #print('#' * self.width)
    def display(self):
        """
        Print a visual representation of the rectangle using the character '#'.
        Takes into account the x and y coordinates.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A formatted string containing rectangle information.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    def update(self, *args):
        """
        Update the attributes of the rectangle based on the provided arguments.

        Args:
            *args: A variable number of arguments:
                   1st argument: id attribute
                   2nd argument: width attribute
                   3rd argument: height attribute
                   4th argument: x attribute
                   5th argument: y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle based on the provided arguments.

        Args:
            *args: A variable number of arguments:
                   1st argument: id attribute
                   2nd argument: width attribute
                   3rd argument: height attribute
                   4th argument: x attribute
                   5th argument: y attribute
            **kwargs: Key-value pairs where each key represents an attribute
                      of the instance.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value