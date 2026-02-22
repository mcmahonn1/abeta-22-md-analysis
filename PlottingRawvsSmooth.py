import matplotlib.pyplot as plt
import numpy as np

# Parameters
frame_interval_ps = 1.0
window_size = 20  # adjust as needed

# Compute helix fractions from your file
helix_fractions = compute_helix_fraction("C:/BINF641/Week9/ProductionC22/IBU/Trajectory5/sstructure.dat")
hf = np.array(helix_fractions)

# Raw time points (in ns)
times_raw = np.arange(len(hf)) * frame_interval_ps / 1000

# Smoothed helix fraction
smoothed_hf = np.convolve(hf, np.ones(window_size)/window_size, mode='valid')
times_smooth = np.arange(len(smoothed_hf)) * frame_interval_ps / 1000

# Plot both
plt.figure(figsize=(12, 4))
plt.plot(times_raw, hf, label="Raw Helix Fraction", color="skyblue", alpha=0.6)
plt.plot(times_smooth, smoothed_hf, label="Smoothed Helix Fraction", color="darkblue", linewidth=2)
plt.xlabel("Time (ns)")
plt.ylabel("Helix Fraction (Nh/N)")
plt.title("System 2 Trajectory 5 — Raw vs. Smoothed Helix Fraction")
plt.ylim(0, 1)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


