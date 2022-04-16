class RandomBase:
    def __init__(self, seed):
        self.current_number = seed

    def random(self):
        pass

    def random_list(self, N=10):
        """Return a list of random numbers"""
        return [self.random() for i in range(N)]

    def __iter__(self):
        return RandomIterator(self)


class RandomIterator:
    def __init__(self, random):
        self._random = random

    def __next__(self):
        return self._random.random()
