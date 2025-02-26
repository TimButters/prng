"""Pseudo-Random Number Generation"""
from .base import RandomBase


class MiddleSquare(RandomBase):
    """Von-Neuman Middle Square Method"""

    def __init__(self, seed=675248, digits=6):
        """Class initialisation.

        Parameters
        ----------
        seed: int (default 675248)
            The initial value to use for number generation.
        digits: int (default 6)
            The number of digits to generate for
            a random number.
        """
        super().__init__(seed)
        self.digits = digits

    def random(self):
        """Generate the next random number"""
        square = str(self.current_number**2)
        skip = (len(square) - self.digits) // 2
        self.current_number = int(square[skip : skip + self.digits])
        return self.current_number
