from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBERS = ["ArcticClimber", "SummitClimber"]

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self,climber_type: str, climber_name: str):
        if climber_type == "ArcticClimber":
            climber = ArcticClimber(climber_name)
        elif climber_type == "SummitClimber":
            climber = SummitClimber(climber_name)
        else:
            return f"{climber_type} doesn't exist in our register."

        try:
            find_climber = next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."
        except StopIteration:
            self.climbers.append(climber)
            return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type == "ArcticPeak":
            peak = ArcticPeak(peak_name, peak_elevation)
        elif peak_type == "SummitPeak":
            peak = SummitPeak(peak_name, peak_elevation)
        else:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}"

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        needed_gear = next(filter(lambda p: p.name == peak_name, self.peaks))
        missing_gear = [item for item in needed_gear.get_recommended_gear() if item not in gear]
        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb " \
               f"{peak_name}. Missing gear: " \
               f"{', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        try:
            climber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."
        try:
            peak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."


    def get_statistics(self):
        for c in self.climbers:
            c.conquered_peaks = sorted(c.conquered_peaks)
        first_result = [c for c in self.climbers if c.conquered_peaks]
        result = sorted(first_result, key = lambda c: (-len(c.conquered_peaks)))
        result_str = '\n'.join([str(c) for c in result])
        return f"Total climbed peaks: {len(self.peaks)}\n" \
               "**Climber's statistics:**\n" \
               f"{result_str}"
