#!/usr/bin/python3
"""
This program checks whether the base class has methods.
The Base: is the main class with other methods
There is an init method which executes regardless
"""
class Base:
    """
    The Base provides basic 'id' to manage the  attribute  in the subclasses
    It assigns unique identifiers to the instances of the number of objects created

    Attributes
        __nb_objects(int):
            This is a private class to keep track of the total number of objects created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base

        Args:
        id(int):
            An integer that shows the desired the identifier for the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
