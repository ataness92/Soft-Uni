from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME = 180

    def __init__(self, name, points):
        super().__init__(name, points, self.TIME)

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"

