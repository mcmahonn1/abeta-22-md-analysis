import numpy as np
import matplotlib.pyplot as plt
import os

# Configuration
data_dir = r"C:\BINF641\Week9\HelixFractions"  # Update if needed
window_size = 20
frame_interval_ps = 1.0  # 1 ps per frame

helix_codes = {'H', 'G', 'I'}

def compute_helix_fraction(filepath):
    fractions = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                fractions.append(0.0)
                continue
            Nh = sum(1 for c in line if c in helix_codes)
            N = len(line)
            h = Nh / N if N > 0 else 0
            fractions.append(h)
    return np.array(fractions)

def compute_average_smoothed(file_list):
    all_smoothed = []
    for fname in file_list:
        full_path = os.path.join(data_dir, fname)
        hf = compute_helix_fraction(full_path)
        smoothed = np.convolve(hf, np.ones(window_size)/window_size, mode='valid')
        all_smoothed.append(smoothed)
    average = np.mean(all_smoothed, axis=0)
    times_ns = np.arange(len(average)) * frame_interval_ps / 1000
    return times_ns, average

# File names
s1_files = [f"sstructureS1T{i}.dat" for i in range(1, 6)]
s2_files = [f"sstructureS2T{i}.dat" for i in range(1, 6)]

# Compute averages
s1_times, s1_avg = compute_average_smoothed(s1_files)
s2_times, s2_avg = compute_average_smoothed(s2_files)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(s1_times, s1_avg, label="System 1 (Water + Peptide)", color="blue")
plt.plot(s2_times, s2_avg, label="System 2 (Water + Peptide + IBU)", color="orange")
plt.xlabel("Time (ns)")
plt.ylabel("Average Helix Fraction ⟨H(t)⟩")
plt.title("Average Smoothed Helix Fraction vs. Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
