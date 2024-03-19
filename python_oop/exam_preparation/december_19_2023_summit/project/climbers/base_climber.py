from abc import ABC, abstractmethod
from typing import List

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: List = []
        self.is_prepared: bool = True

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        return f"{self.__class__.__name__}: /// " \
               f"Climber name: {self.name} * " \
               f"Left strength: {self.strength:.1f} * " \
               f"Conquered peaks: {', '.join(self.conquered_peaks)} ///"

