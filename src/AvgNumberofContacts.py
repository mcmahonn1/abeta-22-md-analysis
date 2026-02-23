"""
AvgNumberofContacts.py

Compute average residue contacts with ibuprofen across trajectories.

Reads from: data/raw/
Writes to: results/figures/ and results/tables/

Author: Nicholas McMahon
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import csv

# Import shared project directories
from config import DATA_RAW, RESULTS_FIGURES, RESULTS_TABLES, ensure_dirs

# Ensure results directories exist
ensure_dirs()

# List of contact files (must be placed in data/raw/)
contact_files = [
    "S2T1ibu_contacts10.11.dat",
    "S2T2ibu_contacts10.11.dat",
    "S2T3ibu_contacts10.11.dat",
    "S2T4ibu_contacts10.11.dat",
    "S2T5ibu_contacts10.11.dat",
]

# Load and accumulate contact data
all_contacts = []

for fname in contact_files:

    path = DATA_RAW / fname

    if not path.exists():
        print(f"Warning: File not found: {path}")
        continue

    with open(path, 'r') as f:
        for line in f:
            counts = list(map(int, line.strip().split()))
            all_contacts.append(counts)

# Convert to NumPy array
contact_array = np.array(all_contacts)

# Compute average contacts per residue
avg_contacts = np.mean(contact_array, axis=0)

# Save table to CSV
csv_path = RESULTS_TABLES / "avg_contacts_ibuprofen.csv"

with open(csv_path, 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(["ResidueIndex", "AverageContacts"])

    for i, val in enumerate(avg_contacts, start=1):
        writer.writerow([i, val])

print(f"Saved table: {csv_path}")

# Save plot
plot_path = RESULTS_FIGURES / "avg_contacts_ibuprofen.png"

plt.figure(figsize=(12, 5))

plt.plot(
    range(1, len(avg_contacts)+1),
    avg_contacts,
    marker='o',
    color='crimson'
)

plt.xlabel("Residue Index (i)")
plt.ylabel("⟨C(i)⟩ - Avg # of Contacts with Ibuprofen")
plt.title("System 2: Average Contacts Between Residues and Ibuprofen")

plt.grid(True)

plt.tight_layout()

plt.savefig(plot_path, dpi=200)

plt.close()

print(f"Saved figure: {plot_path}")

