from .base import RandomBase


class LinConGen(RandomBase):
    def __init__(self, *, seed=56, a=48271, c=74, m=2**32):
        super().__init__(seed)
        self._a = a
        self._c = c
        self._m = m

    def random(self):
        self.current_number = (self._a * self.current_number + self._c) % self._m
        return self.current_number / self._m
