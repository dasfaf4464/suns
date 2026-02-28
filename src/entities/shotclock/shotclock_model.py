class Shotclock:
    def __init__(self):
        self.current_time: float = 24.00 #second
        self.setup_time: float = 24.0
        self.is_update: bool = False
        self.stop: bool = False
        self.time_record = []
        self.speed = 1.0

    def update(self, delta_time):
        if self.is_update and not self.stop and self.current_time <= 0:
            self.current_time -= delta_time * self.speed

    def stop_time(self):
        self.stop = True
        self.time_record.append(self.current_time)

    def restart(self):
        self.stop = False

    def reset(self, time_setup):
        self.time_setup = time_setup
        self.current_time = self.time_setup
        self.time_record.clear()

    def get_printable(self):
        return self.current_time