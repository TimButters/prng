from .base import RandomBase


class LinConGen(RandomBase):
    """Linear Congruential Generator"""
    def __init__(self, *, seed=56, a=48271, c=74, m=2**32):
        """LCG Initialisation

        Parameters
        ----------
        seed: int (default 56)
            The initial value to use for generation.
        a: int (default 48271)
            Multiplier.
        c: int (default 74)
            Addiditive value.
        m: int (default 2^32)
            Modulo value.
        """
        super().__init__(seed)
        self._a = a
        self._c = c
        self._m = m

    def random(self):
        """Generate the next random number"""
        self.current_number = (self._a * self.current_number + self._c) % self._m
        return self.current_number / self._m
