#!/usr/bin/env python3
"""Defines a Square class that inherits from Rectangle."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a validated size."""

    def __init__(self, size):
        """Initialize a square with a positive integer size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square area."""
        return self.__size * self.__size
