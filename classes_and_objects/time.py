class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours:int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def set_time(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds = (self.seconds + 1) % (self.max_seconds + 1)
        if self.seconds == 0:
            self.minutes = (self.minutes + 1) % (self.max_minutes + 1)
            if self.minutes == 0:
                self.hours = (self.hours + 1) % (self.max_hours + 1)
        return self.get_time()

    # def next_second(self):
    #     if self.seconds == Time.max_seconds:
    #         self.seconds = 0
    #         self.minutes += 1
    #
    #         if self.minutes == Time.max_minutes+1:
    #             self.minutes = 0
    #             self.hours += 1
    #
    #             if self.hours == Time.max_hours+1:
    #                 self.hours = 0
    #                 self.seconds = 0
    #
    #
    #     else:
    #         self.seconds += 1

        return self.get_time()

time = Time(23, 59, 59)

print(time.next_second())


def next_second(self):
    self.seconds = (self.seconds + 1) % (self.max_seconds + 1)
    self.minutes = (self.minutes + self.seconds // (self.max_seconds + 1)) % (self.max_minutes + 1)
    self.hours = (self.hours + self.minutes // (self.max_minutes + 1)) % (self.max_hours + 1)
    return self.get_time()
