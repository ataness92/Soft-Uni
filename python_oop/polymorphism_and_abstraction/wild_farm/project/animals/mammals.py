from typing import List

from project.animals.animal import Mammal
from project.food import Vegetable, Food, Fruit, Meat


class Mouse(Mammal):

    @property
    def food_that_eats(self) -> List[Food]:
        return [Vegetable, Fruit]

    @property
    def gain_weight(self) -> float:
        return 0.1

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):

    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 0.4

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):

    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat, Vegetable]

    @property
    def gain_weight(self) -> float:
        return 0.3

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):

    @property
    def food_that_eats(self) -> List[Food]:
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 1

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
