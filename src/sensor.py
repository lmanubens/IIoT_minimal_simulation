import random
import time

class Sensor:
    """Simulates a basic sensor producing measurements."""
    def __init__(self, name: str, unit: str, min_value: float, max_value: float, interval: float = 1.0):
        self.name = name
        self.unit = unit
        self.min_value = min_value
        self.max_value = max_value
        self.interval = interval
        self.value = None
        self.last_time = None

    def read(self):
        """Generate a new measurement."""
        self.value = random.uniform(self.min_value, self.max_value)
        self.last_time = time.time()
        return self.value
