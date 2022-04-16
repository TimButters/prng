"""Pseudo-Random Number Generation"""
from base import RandomBase, RandomIterator


class MiddleSquare(RandomBase):
    """Von-Neuman Middle Square Method"""
    def __init__(self, digits=6, seed=675248):
        super().__init__(seed)
        self.digits = digits

    def random(self):
        """Return a single random number"""
        square = str(self.current_number ** 2)
        skip = (len(square) - self.digits) // 2
        self.current_number = int(square[skip: skip + self.digits])
        return self.current_number

    def random_list(self, N=10):
        """Return a list of random numbers"""
        return [self.random() for i in range(N)]
