"""
Computeaveragehelicalfraction.py

Compute mean, standard deviation, and standard error of helix fraction
across multiple trajectories for:

- System 1 (S1): Water + peptide
- System 2 (S2): Water + peptide + ibuprofen

Reads from: data/raw/
Writes to: results/tables/

Author: Nicholas McMahon
"""

import numpy as np
import csv

from config import DATA_RAW, RESULTS_TABLES, ensure_dirs

ensure_dirs()

helix_codes = {"H", "G", "I"}


def compute_helix_fraction(filepath):
    fractions = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            Nh = sum(1 for c in line if c in helix_codes)
            N = len(line)
            fractions.append(Nh / N if N > 0 else 0.0)
    return np.array(fractions, dtype=float)


def compute_system_stats(system_label, file_list):
    all_raw = []
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
        all_raw.extend(hf)

    if found == 0:
        print(f"\nNo files found for {system_label}.")
        return None

    if len(all_raw) == 0:
        print(f"\nFiles found for {system_label}, but no helix values read.")
        return None

    all_raw = np.array(all_raw, dtype=float)

    mean = float(np.mean(all_raw))
    std = float(np.std(all_raw))
    se = float(std / np.sqrt(len(all_raw)))
    n = int(len(all_raw))

    print(f"{system_label} — ⟨H⟩: {mean:.4f}, SD: {std:.4f}, SE: {se:.4f}, frames: {n}")

    return {"system": system_label, "mean": mean, "std": std, "se": se, "n_frames": n}


def save_stats_row(stats, outname):
    out_csv = RESULTS_TABLES / outname
    with open(out_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["system", "mean", "std", "se", "n_frames"])
        writer.writerow([stats["system"], stats["mean"], stats["std"], stats["se"], stats["n_frames"]])
    print(f"Saved table: {out_csv}")


def main():
    s1_files = [f"sstructureS1T{i}.dat" for i in range(1, 6)]
    s2_files = [f"sstructureS2T{i}.dat" for i in range(1, 6)]

    s1_stats = compute_system_stats("S1", s1_files)
    s2_stats = compute_system_stats("S2", s2_files)

    if s1_stats is not None:
        save_stats_row(s1_stats, "helix_stats_S1.csv")

    if s2_stats is not None:
        save_stats_row(s2_stats, "helix_stats_S2.csv")

    if s1_stats is None and s2_stats is None:
        raise SystemExit("No helix structure files found for either system.")


if __name__ == "__main__":
    main()
