class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Computes the dot product of two vectors and prints the result.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise and prints the resulting vector.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first one element-wise and
        prints the resulting vector.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sub Vector is: {result}")
