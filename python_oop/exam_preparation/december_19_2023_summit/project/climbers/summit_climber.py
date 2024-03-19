from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    SUMMIT_STRENGTH = 150
    REQUIRED_STRENGTH = 75

    def __init__(self, name):
        super().__init__(name, SummitClimber.SUMMIT_STRENGTH)

    def can_climb(self):
        return self.strength >= SummitClimber.REQUIRED_STRENGTH

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 30*1.3
        elif peak.difficulty_level == "Advanced":
            self.strength -= 30*2.5

        self.conquered_peaks.append(peak.name)
