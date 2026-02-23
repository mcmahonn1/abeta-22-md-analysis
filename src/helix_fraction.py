"""
helix_fraction.py

Compute helix fraction from STRIDE secondary structure output.

Author: Nicholas McMahon
"""

from pathlib import Path
import csv


# Define project directories relative to repo root
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_RAW = BASE_DIR / "data" / "raw"
RESULTS_TABLES = BASE_DIR / "results" / "tables"


def compute_helix_fraction(filepath):

    # Define which secondary structure codes are helical
    helix_codes = {'H', 'G', 'I'}

    total_Nh = 0
    total_N = 0
    failed_frames = 0
    helix_fractions = []

    with open(filepath, 'r') as f:

        for i, line in enumerate(f):

            line = line.strip()

            if not line:
                failed_frames += 1
                continue

            Nh = sum(1 for c in line if c in helix_codes)
            N = len(line)

            h = Nh / N if N > 0 else 0

            helix_fractions.append(h)

            total_Nh += Nh
            total_N += N

    print(f"\nFile: {filepath.name}")
    print(f"Total frames: {i + 1}")
    print(f"Failed frames: {failed_frames}")
    print(f"Valid frames: {i + 1 - failed_frames}")

    avg_h = total_Nh / total_N

    print(f"Average helix fraction: {avg_h:.4f} ({avg_h * 100:.2f}%)")

    return helix_fractions, avg_h


def save_results(filename, helix_fractions):

    RESULTS_TABLES.mkdir(parents=True, exist_ok=True)

    output_file = RESULTS_TABLES / f"{filename}_helix_fraction.csv"

    with open(output_file, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(["Frame", "HelixFraction"])

        for i, h in enumerate(helix_fractions):

            writer.writerow([i, h])

    print(f"Saved results to {output_file}")


# Example execution when script is run directly
if __name__ == "__main__":

    # Example file name — put your actual STRIDE file in data/raw/
    input_file = DATA_RAW / "sstructureS2T1.dat"

    if input_file.exists():

        helix_fractions, avg_h = compute_helix_fraction(input_file)

        save_results("sstructureS2T1", helix_fractions)

    else:

        print(f"Input file not found: {input_file}")
        print("Place your STRIDE output file inside data/raw/")


