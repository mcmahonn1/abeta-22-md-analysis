# Aβ16–22 Molecular Dynamics Structural Analysis

## Overview

This project analyzes molecular dynamics (MD) simulations of the Aβ16–22 peptide in two environments:

- System 1: Peptide in water
- System 2: Peptide in water with ibuprofen

The goal is to quantify how ibuprofen affects peptide structural stability to determine if results obtained are similar to current studies.
## Methods

Secondary structure data was obtained using STRIDE via VMD and analyzed using Python.

Key metrics computed:

- Helix fraction over time
- Smoothed helix fraction trajectories
- Average helix fraction across trajectories
- Structural persistence time above threshold
- Residue-level contact frequency with ibuprofen
- Potential energy stability analysis

## Tools Used

- Python
- NumPy
- Matplotlib
- Molecular Dynamics (NAMD)
- VMD / STRIDE

## Key Scripts

- `helix_fraction.py` – Computes helix fraction from secondary structure data
- `Computeaveragehelicalfraction.py` – Calculates average helix fraction statistics
- `PlottingRawvsSmooth.py` – Visualizes structural stability over time
- `AvgNumberofContacts.py` – Computes residue–ibuprofen interaction frequencies
- `Plotting potential energyvsSimSteps.py` – Analyzes simulation energy stability

## Scientific Significance

This analysis quantifies how ibuprofen influences structural stability of amyloid peptides, which is relevant to understanding peptide aggregation and drug interactions.

## Author

Nicholas McMahon  
M.S. Computational Biology and Bioinformatics