class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.dictionary[key]
            self.index += 1
            return key, value
        else:
            raise StopIteration


class dictionary_iter2:

    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dictionary)-1:
            raise StopIteration

        self.index += 1

        return self.items[self.index]

class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.items = dictionary.items()

    def __iter__(self):
        return iter(self.items)



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)