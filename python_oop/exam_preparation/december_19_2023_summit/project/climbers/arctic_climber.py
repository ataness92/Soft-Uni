from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    ARCTIC_STRENGTH = 200
    REQUIRED_STRENGTH = 100

    def __init__(self, name):
        super().__init__(name, ArcticClimber.ARCTIC_STRENGTH)

    def can_climb(self):
        return self.strength >= ArcticClimber.REQUIRED_STRENGTH

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 40
        elif peak.difficulty_level == "Advanced":
            self.strength -= 30

        self.conquered_peaks.append(peak.name)
