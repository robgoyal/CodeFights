# Name: vectorClass.py
# Author: Robin Goyal
# Last-Modified: June 12, 2018
# Purpose: Implement a Vector Class

from math import sqrt


class Vector:
    """Vector Class"""

    def __init__(self, coords):
        self.coords = coords

    def add(self, other):
        """add

        Returns a new vector with the coordinates summed.

        Examples:
        >>> a = Vector([1, 2, 3])
        >>> b = Vector([3, 4, 5])
        >>> a.add(b)
        Vector([4, 6, 8])
        """

        Vector._check_lengths(self, other)
        new_coords = [i + j for i, j in zip(self.coords, other.coords)]
        return Vector(new_coords)

    def subtract(self, other):
        """subtract

        Returns a new vector with the coordinates subtracted.

        Examples:
        >>> a = Vector([1, 2, 3])
        >>> b = Vector([3, 4, 5])
        >>> a.subtract(b)
        Vector([-2, -2, -2])
        """

        Vector._check_lengths(self, other)
        new_coords = [i - j for i, j in zip(self.coords, other.coords)]
        return Vector(new_coords)

    def dot(self, other):
        """dot

        Returns the dot product of two vectors

        Examples:
        >>> a = Vector([1, 2, 3])
        >>> b = Vector([3, 4, 5])
        >>> a.dot(b)
        26
        """

        Vector._check_lengths(self, other)
        product = sum(i * j for i, j in zip(self.coords, other.coords))
        return product

    def norm(self):
        """norm

        Return the normalized value of the vector.

        Examples:
        >>> a = Vector([1, 2, 3])
        >>> a.norm()
        sqrt(14)
        """

        return sqrt(sum(pow(coord, 2) for coord in self.coords))

    def equals(self, other):
        """equals

        Returns True if the coordinates of the vectors
        are the same, False otherwise.

        Examples:
        >>> a = Vector([1, 2, 3])
        >>> b = Vector([1, 2, 3])
        >>> c = Vector([5, 6, 7, 8])
        >>> a.equals(b)
        True
        >>> a.equals(c)
        False
        """

        if len(self.coords) != len(other.coords):
            return False

        for i, j in zip(self.coords, other.coords):
            if i != j:
                return False

        return True

    def __str__(self):
        """
        Examples:
        >>> a = Vector([1, 2, 3])
        >>> print(a)
        (1,2,3)
        """

        return "({})".format(",".join([str(coord) for coord in self.coords]))

    @staticmethod
    def _check_lengths(v1, v2):
        """_check_lengths

        Raise an exception if v1 and v2 are of
        different lengths.

        Examples:
        >>> a = Vector([1, 2, 3])
        >>> b = Vector([3, 4, 5])
        >>> c = Vector([5, 6, 7, 8])
        >>> _check_lengths(b, c)
        Exception Raised
        """

        if len(v1.coords) != len(v2.coords):
            raise Exception("Vectors are of different sizes")
