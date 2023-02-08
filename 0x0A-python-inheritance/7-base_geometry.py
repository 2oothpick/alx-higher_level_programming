#!/usr/bin/python3
"""
this module contains the based geometry class
"""


class BaseGeometry:
    """this is the based geometry class """
    def area(self):
        """this is the area method """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """this is the integer validator method """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
