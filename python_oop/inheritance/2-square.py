#!/usr/bin/env python3
"""Defines a Square class with a string representation."""


SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represent a square with a validated size."""

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
