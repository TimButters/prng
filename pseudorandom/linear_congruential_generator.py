from .base import RandomBase


class LinConGen(RandomBase):
    def __init__(self, seed=56):
        super().__init__(seed)
        self._a = 48271
        self._c = 74
        self._m = 2 ** 32

    def random(self):
        self.current_number = (self._a*self.current_number + self._c) % self._m
        return self.current_number