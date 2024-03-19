from typing import List

from project.animals.animal import Bird
from project.food import Food, Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def gain_weight(self) -> float:
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"
