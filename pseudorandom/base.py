class RandomBase:
    def __init__(self, seed):
        self.current_number = seed

    def __iter__(self):
        return RandomIterator(self)


class RandomIterator:
    def __init__(self, random):
        self._random = random

    def __next__(self):
        return self._random.random()
