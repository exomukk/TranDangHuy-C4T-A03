class Timer:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1

    def reset(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
