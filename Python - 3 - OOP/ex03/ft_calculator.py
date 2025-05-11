class calculator:
    """
    A simple vector calculator using operator overloading.

    Supports addition, subtraction, multiplication, and division
    between a vector (list of floats) and a scalar.
    """
    def __init__(self, vector):
        """
        Initialize the calculator with a vector of floats.

        Args:
            value (list of float): The vector to operate on.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Add a scalar to each element of the vector and print the result.

        Args:
            object (int | float): The scalar to add.
        """
        res = [v + object for v in self.vector]
        print(res)

    def __mul__(self, object) -> None:
        """
        Multiply each element of the vector by a scalar and print the result.

        Args:
            object (int | float): The scalar to multiply.
        """
        res = [v * object for v in self.vector]
        print(res)

    def __sub__(self, object) -> None:
        """
        Subtract a scalar from each element of the vector and print the result.

        Args:
            object (int | float): The scalar to subtract.
        """
        res = [v - object for v in self.vector]
        print(res)

    def __truediv__(self, object) -> None:
        """
        Divide each element of the vector by a scalar and print the result.
        Handle division by zero.

        Args:
            object (int | float): The scalar to divide by.
        """
        try:
            res = [v / object for v in self.vector]
            print(res)
        except ZeroDivisionError:
            print("Division by zero is impossible")
