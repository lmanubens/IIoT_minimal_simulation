# IIoT Minimal Simulation

This repository demonstrates a minimal example of simulating an industrial IoT (IIoT) environment for a water management network. A few mock sensors generate data that is collected and visualized in real time.

## Requirements

- Python 3.8+
- `matplotlib`

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Simulation

Execute the visualization script which also runs the sensor simulation:

```bash
python -m src.visualization
```

A window will open showing a live graph of each sensor's output.

When running in a Jupyter environment such as Google Colab, use:

```python
from src.visualization import main
main(inline=True)
```

This returns an HTML animation that displays directly in the notebook.

## Directory Structure

- `src/sensor.py` – definition of a simple sensor model
- `src/monitor.py` – monitoring/aggregation of sensor data
- `src/visualization.py` – real-time plotting of sensor values

Feel free to extend the code with additional sensors or storage backends for a more realistic setup.
