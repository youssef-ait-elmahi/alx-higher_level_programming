#!/usr/bin/python3
"""this class defines rectangle"""


class Rectangle:
    """
    A class representing a rectangle.
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    Methods:
        No additional methods defined.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        Raises:
            ValueError: If width or height is less than 0.
            TypeError: If width or height is not an integer.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.
        Args:
            value (int): The width value to set.
        Raises:
            ValueError: If width is less than 0.
            TypeError: If width is not an integer.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        Get the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.
        Args:
            value (int): The height value to set.
        Raises:
            ValueError: If height is less than 0.
            TypeError: If height is not an integer.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            int: The calculated area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Returns:
            int: The calculated perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
