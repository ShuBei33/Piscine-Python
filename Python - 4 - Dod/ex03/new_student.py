import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generates a random 15-character lowercase ID.

    Returns:
        A string composed of 15 random lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Data class representing a student.

    Attributes:
        name: First name of the student.
        surname: Surname of the student.
        active: Indicates if the student is active (default is True).
        login: Auto-generated login based on name and surname.
        id: Randomly generated 15-character lowercase ID.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
        Builds the login and ID after initialization.
        Login = first letter of name (uppercase) + surname (lowercase).
        ID = 15-letter random lowercase string.
        """
        self.login = self.name[0].upper() + self.surname.lower()
        self.id = generate_id()
