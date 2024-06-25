class CustomList():

    def __init__(self):
        self.__values = []

    def append(self, value):
        self.__values[len(self.__values):] = [value]
        return self.__values