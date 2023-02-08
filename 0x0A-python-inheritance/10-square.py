#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ subclass of Rectangle"""
    def __init__(self, size):
        """instance of a square"""
        super().__init__(size, size)
        self.__size = size
        BaseGeometry.integer_validator(self, "size", self.__size)

    def area(self):
        """returns the area of the square """
        return self.__size ** 2
