#!/usr/bin/python
"""defines a square by: (based on 1-square.py)"""

class Square:
    """Square with private instance attribute size"""
    def __init(self, size=0);
    """Args:
           size: size of square"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__ = size
        else:
            raise TypeError("size must be an integer")
