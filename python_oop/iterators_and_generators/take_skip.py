class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.index = -step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.count*self.step-self.step:
            self.index += self.step
            return self.index
        raise StopIteration
