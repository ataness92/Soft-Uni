from project.next_id_mixin import NextIdMixin


class ExercisePlan(NextIdMixin):
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours):
        return cls(trainer_id, equipment_id, hours*60)

