import matplotlib.pyplot as plt
import numpy as np
import os

def extract_temp_potential(filepath):
    times = []
    temps = []
    potentials = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith("ENERGY:"):
                parts = line.strip().split()
                if len(parts) > 15:
                    ts = int(parts[1])
                    temp = float(parts[15])
                    potential = float(parts[16])
                    times.append(ts)
                    temps.append(temp)
                    potentials.append(potential)
    return times, temps, potentials

# Directory for output files
trajectory_dir = r"C:\BINF641\Week9\ProductionC22\Water\Trajectory5"
dt_ps = 1.0  # picoseconds per frame

out_files = [f for f in os.listdir(trajectory_dir) if f.endswith(".out")]

# Collect aligned data
all_temps = []
all_potentials = []
common_times = None

for file in out_files:
    full_path = os.path.join(trajectory_dir, file)
    times, temps, potentials = extract_temp_potential(full_path)

    if common_times is None:
        common_times = times
    elif times != common_times:
        continue  # skip files that don't match in length/timing

    all_temps.append(temps)
    all_potentials.append(potentials)

# Convert to NumPy for averaging
temps_array = np.array(all_temps)
potentials_array = np.array(all_potentials)
average_temps = np.mean(temps_array, axis=0)
average_potentials = np.mean(potentials_array, axis=0)
times_ns = np.array(common_times) * dt_ps / 1000

# Plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(times_ns, average_temps, color="tab:blue")
plt.title("S1T5 Average Temperature vs Time")
plt.xlabel("Time (ns)")
plt.ylabel("Temperature (K)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(times_ns, average_potentials, color="tab:red")
plt.title("S1T5 Average Potential Energy vs Time")
plt.xlabel("Time (ns)")
plt.ylabel("Potential Energy (kcal/mol)")
plt.grid(True)

plt.tight_layout()
plt.show()


