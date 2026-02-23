"""
Plotting AVGoverTrajectories.py

Compute and plot the average smoothed helix fraction across trajectories
for System 1 vs System 2.

Reads from: data/raw/
Writes to: results/figures/ and results/tables/

Author: Nicholas McMahon
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

from config import DATA_RAW, RESULTS_FIGURES, RESULTS_TABLES, ensure_dirs

ensure_dirs()

# Configuration
window_size = 20
frame_interval_ps = 1.0  # 1 ps per frame
helix_codes = {"H", "G", "I"}


def compute_helix_fraction(filepath):
    fractions = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                fractions.append(0.0)
                continue
            Nh = sum(1 for c in line if c in helix_codes)
            N = len(line)
            fractions.append(Nh / N if N > 0 else 0.0)
    return np.array(fractions, dtype=float)


def smooth(hf):
    if len(hf) < window_size:
        return np.array([], dtype=float)
    kernel = np.ones(window_size, dtype=float) / window_size
    return np.convolve(hf, kernel, mode="valid")


def compute_average_smoothed(file_list, system_label):
    all_smoothed = []
    found = 0

    print(f"\n--- {system_label}: reading from {DATA_RAW} ---")

    for fname in file_list:
        path = DATA_RAW / fname

        if not path.exists():
            print(f"NOT FOUND: {fname}")
            continue

        print(f"FOUND: {fname}")
        found += 1

        hf = compute_helix_fraction(path)
        sm = smooth(hf)

        if len(sm) == 0:
            print(f"Warning: {fname} shorter than window_size={window_size}, skipping.")
            continue

        all_smoothed.append(sm)

    if found == 0 or len(all_smoothed) == 0:
        return None, None

    # Make sure equal lengths (trim to shortest)
    minlen = min(len(x) for x in all_smoothed)
    all_smoothed = [x[:minlen] for x in all_smoothed]

    average = np.mean(all_smoothed, axis=0)

    times_ns = np.arange(len(average), dtype=float) * frame_interval_ps / 1000.0

    return times_ns, average


def save_series_csv(times_ns, avg_series, outname):
    out_csv = RESULTS_TABLES / outname
    with open(out_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time_ns", "avg_smoothed_helix"])
        for t, h in zip(times_ns, avg_series):
            writer.writerow([float(t), float(h)])
    print(f"Saved table: {out_csv}")


def main():
    # File names expected in data/raw/
    s1_files = [f"sstructureS1T{i}.dat" for i in range(1, 6)]
    s2_files = [f"sstructureS2T{i}.dat" for i in range(1, 6)]

    s1_times, s1_avg = compute_average_smoothed(s1_files, "S1")
    s2_times, s2_avg = compute_average_smoothed(s2_files, "S2")

    if s1_times is None or s2_times is None:
        raise SystemExit("Missing S1 or S2 files in data/raw/. Copy sstructureS1T*.dat and sstructureS2T*.dat into data/raw/.")

    # Align lengths/time axis just in case
    minlen = min(len(s1_avg), len(s2_avg))
    s1_times, s1_avg = s1_times[:minlen], s1_avg[:minlen]
    s2_times, s2_avg = s2_times[:minlen], s2_avg[:minlen]

    # Save averaged series to CSV
    save_series_csv(s1_times, s1_avg, "avg_smoothed_helix_S1.csv")
    save_series_csv(s2_times, s2_avg, "avg_smoothed_helix_S2.csv")

    # Plot and save
    out_fig = RESULTS_FIGURES / "avg_smoothed_helix_S1_vs_S2.png"

    plt.figure(figsize=(10, 5))
    plt.plot(s1_times, s1_avg, label="System 1 (Water + Peptide)")
    plt.plot(s2_times, s2_avg, label="System 2 (Water + Peptide + IBU)")
    plt.xlabel("Time (ns)")
    plt.ylabel("Average Helix Fraction ⟨H(t)⟩")
    plt.title("Average Smoothed Helix Fraction vs. Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_fig, dpi=200)
    plt.close()

    print(f"Saved figure: {out_fig}")


if __name__ == "__main__":
    main()
