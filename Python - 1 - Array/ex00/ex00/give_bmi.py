import numpy as np
import sys


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    calculate bmi from 2 lists of the same size, int and float only
    use numpy to be faster
    return bmi as list
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
    verify if each bmi given if above the limit specified or not
    return true or false
    """
    return [x > limit for x in bmi]
