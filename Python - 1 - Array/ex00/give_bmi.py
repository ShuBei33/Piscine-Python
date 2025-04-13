import numpy as np
import sys


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculates BMI values from two lists: height and weight.

    Uses NumPy for efficient array operations and returns the result
    as a list of BMI values. Both input lists must be of the same size
    and contain only integers or floats.

    Args:
        height (list[int | float]): List of heights.
        weight (list[int | float]): List of weights.

    Returns:
        list[float]: List of calculated BMI values.
    """

    try:
        if len(height) != len(weight):
            raise ValueError("ValueError: the lists are not the same size")
        if not all(isinstance(h, (int, float)) for h in height):
            raise TypeError("TypeError: height must be int or float")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError("TypeError: weight must be int or float")

        height_array = np.array(height)
        weight_array = np.array(weight)
        bmi = weight_array / (height_array ** 2)

        return bmi.tolist()  # retransforme en liste

    except Exception as e:
        print(e)
        sys.exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks which BMI values are above a given limit.

    Returns a list of booleans indicating whether each BMI is
    greater than the specified threshold.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Threshold to compare against.

    Returns:
        list[bool]: List of booleans, True if BMI is above the limit.
    """

    return [x > limit for x in bmi]
