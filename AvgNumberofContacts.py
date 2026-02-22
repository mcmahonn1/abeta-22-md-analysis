import os
import numpy as np
import matplotlib.pyplot as plt

# Directory where contact files are located
data_dir = r"C:\BINF641\Week9\ProductionC22\Ibu"

# List of all contact files
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
    path = os.path.join(data_dir, fname)
    with open(path, 'r') as f:
        for line in f:
            counts = list(map(int, line.strip().split()))
            all_contacts.append(counts)

# Convert to NumPy array: shape (frames * traj, residues)
contact_array = np.array(all_contacts)

# Compute ⟨C(i)⟩ across all timepoints and all trajectories
avg_contacts = np.mean(contact_array, axis=0)

# Plot ⟨C(i)⟩
plt.figure(figsize=(12, 5))
plt.plot(range(1, len(avg_contacts)+1), avg_contacts, marker='o', color='crimson')
plt.xlabel("Residue Index (i)")
plt.ylabel("⟨C(i)⟩ - Avg # of Contacts with Ibuprofen")
plt.title("System 2: Average Contacts Between Residues and Ibuprofen")
plt.grid(True)
plt.tight_layout()
plt.show()

# 📃 Print values
print("Residue Index\t⟨C(i)⟩")
for i, val in enumerate(avg_contacts, start=1):
    print(f"{i:>4}\t\t{val:.4f}")
