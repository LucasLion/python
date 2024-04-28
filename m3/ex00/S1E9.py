from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""
    def __init__(self, first_name, is_alive=True):
        """Initialize the charater with a first name and alive status"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method the change the health state of the character"""
        pass

class Stark(Character):
    """Class representing a Stark character"""
    def __init__(self, first_name, is_alive=True):
        """Initialize the Stark charater with a first name and alive status"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Child method the change the health state of the Stark character"""
        self.is_alive = False



