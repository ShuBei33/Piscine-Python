import numpy as np
import sys


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D array between the given start and end indices.

    Prints the original and new shapes, and returns the sliced array
    as a list. The slicing is done using standard Python slicing
    and NumPy is used for shape handling.

    Args:
        family (list): A two-dimensional list to be sliced.
        start (int): Starting index (included).
        end (int): Ending index (excluded).

    Returns:
        list: A sliced version of the input list.
    """

    try:
        if not isinstance(family, list):
            raise TypeError("data sent must be a two-dimensional list")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("data inside 2d array must be lists")
        if len(family) == 0:
            raise ValueError("input list must not be empty")
        size = len(family[0])
        if not all(len(row) == size for row in family):
            raise ValueError("all rows must have the same number of elements")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end positions must be integers")

        family = np.array(family)
        print(f"My shape is : {np.shape(family)}")
        sliced = family[start:end]
        if sliced.size == 0:
            print("My new shape is : (0, 0)")
            return []
        print(f"My new shape is : {np.shape(sliced)}")
        return sliced.tolist()

    except Exception as e:
        print(e)
        sys.exit(1)
