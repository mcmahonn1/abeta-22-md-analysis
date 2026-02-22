import numpy as np
import os

# --- Setup ---
data_dir = r"C:\BINF641\Week9\HelixFractions"  # adjust path if needed
s2_files = [f"sstructureS2T{i}.dat" for i in range(1, 6)]
helix_codes = {'H', 'G', 'I'}

def compute_helix_fraction(filepath):
    fractions = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            Nh = sum(1 for c in line if c in helix_codes)
            N = len(line)
            h = Nh / N if N > 0 else 0
            fractions.append(h)
    return np.array(fractions)

# --- Collect all raw helix fractions from all 5 trajectories ---
all_raw_H = []
for fname in s2_files:
    full_path = os.path.join(data_dir, fname)
    raw_hf = compute_helix_fraction(full_path)
    all_raw_H.extend(raw_hf)  # append all frame values to master list

# --- Calculate statistics ---
all_raw_H = np.array(all_raw_H)
H_avg = np.mean(all_raw_H)
H_std = np.std(all_raw_H)
H_se = H_std / np.sqrt(len(all_raw_H))

# --- Output ---
print(f"System 2 — Average Helix Fraction ⟨H⟩: {H_avg:.4f}")
print(f"System 2 — Standard Deviation: {H_std:.4f}")
print(f"System 2 — Standard Error: {H_se:.4f}")
