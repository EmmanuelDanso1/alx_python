#!/usr/bin/python3
"""
This Square class module inherits its attributes from the Rectangle class
"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class and represents a square
    with equal width and height attributes.

    Attributes (inherited from Rectangle):
        id (int): An identifier assigned by the Base class constructor.
        width (int): The width of the square.
        height (int): The height of the square (same as width).
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance of the Rectangle class.

        Args:
            x (int): The x-coordinate of the top-left corner of the rectangle
            y (int): The y-coordinate of the top-left corner of the rectangle
            id (int): A unique identifier for the instance
            size(int):size of the square
        """
        super().__init__(size, size, x, y, id)

    #def __str__(self):
        #return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    @property
    def size(self):
        """int: The size of the square (same as width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (also updates width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A formatted string containing square information.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    