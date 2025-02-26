class RandomBase:
    """Base class for PRNG derivative classes

    This implements basic helper methods, the
    `random()` method must be overriden in each
    child class.
    """
    def __init__(self, seed):
        self.current_number = seed

    def random(self):
        """Must be provided by each child class"""
        pass

    def random_list(self, N=10):
        """Return a list of random numbers"""
        return [self.random() for i in range(N)]

    def __iter__(self):
        return RandomIterator(self)


class RandomIterator:
    """Helper class for `__iter__` definitions"""
    def __init__(self, random):
        self._random = random

    def __next__(self):
        return self._random.random()
