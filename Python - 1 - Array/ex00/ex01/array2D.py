import numpy as np
import sys

def slice_me(family: list, start: int, end: int) -> list:
    """
    bkbkbkb
    """
    try:
        if not isinstance(family, list):
            raise TypeError("TypeError: data sent must be a list of lists")
        if not all(isinstance(row, list) for row in family):
            raise TypeError("TypeError: data inside 2d array must be lists")
        size = len(family[0])
        if not all(len(row) == size for row in family):
            raise ValueError("ValueError: all rows must have the same size")


    except Exception as e:
        print(e)
        sys.exit(1)
