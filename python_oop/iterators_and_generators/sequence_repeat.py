class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number + len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > len(self.sequence):
            self.number -= len(self.sequence)
            return self.sequence[:self.number] if self.number < len(self.sequence) else self.sequence
        raise StopIteration

class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number - 1:
            raise StopIteration

        self.idx += 1

        return self.sequence[self.idx%len(self.sequence)]


# test zero
import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        result = list(sequence_repeat('abc', 5))
        self.assertEqual(result, ['a', 'b', 'c', 'a', 'b'])

if __name__ == '__main__':
    unittest.main()