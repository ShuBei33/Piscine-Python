from S1E9 import Character


class Baratheon(Character):
    """
    Class representing the Baratheon family
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Baratheon character with family-specific traits.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): Whether the character is alive (default True).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def die(self):
        """
        Mark the Baratheon character as dead.
        """
        self.is_alive = False


class Lannister(Character):
    """
    Class representing the Lannister family
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Lannister character with family-specific traits.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): Whether the character is alive (default True).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def die(self):
        """
        Mark the Lannister character as dead.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Create a new instance of the Lannister class.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): Whether the character is alive (default True).

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        return cls(first_name, is_alive)
