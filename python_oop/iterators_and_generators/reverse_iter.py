class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.iterable):
            return self.iterable.pop()
        raise StopIteration


one_to_ten = reverse_iter([1, 2, 3, 4])

for num in one_to_ten:
    print(num)