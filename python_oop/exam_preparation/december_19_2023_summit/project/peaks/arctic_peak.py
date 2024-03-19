from typing import List

from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)
        self.difficulty_level = self.calculate_difficulty_level()

    def get_recommended_gear(self) -> List:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return "Extreme"
        if self.elevation >= 2000:
            return "Advanced"


