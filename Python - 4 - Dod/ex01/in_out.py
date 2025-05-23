def square(x: int | float) -> int | float:
    """
    Computes the square of a number.

    Args:
        x: A number to be squared.

    Returns:
        The result of x * x.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Raises a number to the power of itself.

    Args:
        x: A number to be exponentiated.

    Returns:
        The result of x ** x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a closure that applies the function to x repeatedly.

    Each time the returned function is called, it applies the function
    to the current value of x, updates x, and returns the result.

    Args:
        x: The initial value.
        function: A function that takes one argument and returns a number.

    Returns:
        A closure function that returns the next value of function(x)
        each time it is called.
    """
    def inner() -> float:
        nonlocal x
        x = function(x)
        return x
    return inner
