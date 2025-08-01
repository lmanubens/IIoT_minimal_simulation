import time

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

try:
    # Only available in notebook environments
    from IPython.display import HTML
except ImportError:  # pragma: no cover - IPython not installed
    HTML = None

from .sensor import Sensor
from .monitor import Monitor


def main(inline: bool = False):
    sensors = [
        Sensor("Water Level", "m", 0.0, 10.0),
        Sensor("Flow Rate", "m3/s", 0.0, 5.0),
        Sensor("pH", "", 6.0, 9.0),
    ]
    monitor = Monitor(sensors)

    fig, ax = plt.subplots()
    lines = {sensor.name: ax.plot([], [], label=sensor.name)[0] for sensor in sensors}
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Value")
    ax.legend()

    start_time = None

    def update(_):
        nonlocal start_time
        if start_time is None:
            start_time = time.time()
        monitor.sample()
        current_time = time.time()
        elapsed = current_time - start_time
        for name, line in lines.items():
            data = monitor.data[name]
            times = [t - start_time for t, _ in data]
            values = [v for _, v in data]
            line.set_data(times, values)
        ax.set_xlim(max(0, elapsed - 60), elapsed + 5)
        return list(lines.values())

    ani = FuncAnimation(fig, update, interval=1000, cache_frame_data=False)
    if inline and HTML is not None:
        plt.close(fig)
        return HTML(ani.to_jshtml())
    plt.show()


if __name__ == "__main__":
    main()
