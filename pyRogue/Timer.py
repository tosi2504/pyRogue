import time



class Timer:
    def __init__(self, FPS):
        self.FPS = FPS
        self.prev_time = time.perf_counter()
        self.current_time = self.prev_time
        self.STEP_TIME = 1./self.FPS

    def update(self):
        self.prev_time = self.current_time
        self.current_time = time.perf_counter()

    def wait_remaining_time(self):
        delta = time.perf_counter() - (self.current_time + self.STEP_TIME)
        if not delta < 0:
            print(f"Timer overloaded by {delta} s")
        while time.perf_counter() < (self.current_time + self.STEP_TIME):
            pass
