import time
from collections import defaultdict
from typing import List, Tuple

from .sensor import Sensor

class Monitor:
    """Collects data from sensors at fixed intervals."""
    def __init__(self, sensors: List[Sensor]):
        self.sensors = sensors
        self.data = defaultdict(list)  # sensor name -> list of (timestamp, value)

    def sample(self):
        """Collect a sample from each sensor."""
        for sensor in self.sensors:
            value = sensor.read()
            self.data[sensor.name].append((sensor.last_time, value))

    def run(self, duration: float, interval: float = 1.0):
        """Run sampling for a duration in seconds."""
        end_time = time.time() + duration
        while time.time() < end_time:
            self.sample()
            time.sleep(interval)
        return self.data
