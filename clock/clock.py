class Clock:
    def __init__(self, hour, minute):
        self.minutes = (60 * hour + minute) % 1440

    def __repr__(self):
        return f"{self.minutes//60:02}:{self.minutes%60:02}"

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, (self.minutes + minutes) % 1440)

    def __sub__(self, minutes):
        return Clock(0, (self.minutes - minutes) % 1440)
