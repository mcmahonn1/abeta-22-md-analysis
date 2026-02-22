import matplotlib.pyplot as plt
import numpy as np

# Path to your sstructure.dat file
filepath = r"C:\BINF641\Week9\ProductionC22\Water\Trajectory5\sstructure.dat"

# Define which secondary structure codes are helical
helix_codes = {'H', 'G', 'I'}

# Frame time (adjust if needed)
frame_interval_ps = 1.0  # 1 ps per frame
window_size = 100        # Smoothing window (100 ps = 0.1 ns)

# Compute helix fraction (raw)
helix_fractions = []
with open(filepath, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            helix_fractions.append(0.0)
            continue
        Nh = sum(1 for c in line if c in helix_codes)
        N = len(line)
        h = Nh / N if N > 0 else 0
        helix_fractions.append(h)

# Convert to NumPy array
hf = np.array(helix_fractions)

# Smoothed helix fraction using moving average
smoothed_hf = np.convolve(hf, np.ones(window_size)/window_size, mode='valid')

# Time axes
times_raw = np.arange(len(hf)) * frame_interval_ps / 1000  # ns
times_smooth = np.arange(len(smoothed_hf)) * frame_interval_ps / 1000  # ns

# Plot both raw and smoothed
plt.figure(figsize=(12, 6))
plt.plot(times_raw, hf, label="Raw Helix Fraction", alpha=0.4, color="gray")
plt.plot(times_smooth, smoothed_hf, label=f"Smoothed ({window_size} frame avg)", color="green")
plt.xlabel("Time (ns)")
plt.ylabel("Helix Fraction (Nh/N)")
plt.title("Helix Fraction vs Time — Trajectory 5")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
