from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the Monster King"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    @property
    def get_eyes(self):
        return self.eyes

    @eyes.setter
    def set_eyes(self, eyes):
        self.eyes = eyes

    @property
    def get_hairs(self):
        return self.hairs

    @hairs.setter
    def set_hairs(self, hairs):
        self.hairs = hairs




