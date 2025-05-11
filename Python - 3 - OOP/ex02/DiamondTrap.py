from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King class combining traits from Baratheon and Lannister.

    Allows dynamic update of eyes and hair color using setter/getter methods.
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """
        Set the eye color of the character.
        """
        self.eyes = color

    def get_eyes(self):
        """
        Return the eye color of the character.
        """
        return self.eyes

    def set_hairs(self, color):
        """
        Set the hair color of the character.
        """
        self.hairs = color

    def get_hairs(self):
        """
        Return the hair color of the character.
        """
        return self.hairs

    def die(self):
        """
        Mark the character as dead.
        """
        self.is_alive = False
