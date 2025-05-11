from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class for any character
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Init character with name and life state
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Mark the character as dead
        """
        pass


class Stark(Character):
    """
    Creation of an inherited class Stark
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Mark the character as dead
        """
        self.is_alive = False
