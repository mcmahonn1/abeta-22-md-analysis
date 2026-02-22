"""
run_analysis.py

Master pipeline for Aβ16–22 molecular dynamics structural analysis.

Runs:

- Helix fraction computation
- Average helix fraction statistics
- Raw vs smoothed trajectory analysis
- Threshold persistence time analysis
- Contact analysis
- Energy stability analysis

Author: Nicholas McMahon
"""

import subprocess
import os

SRC_DIR = "src"

scripts = [
    "helix_fraction.py",
    "Computeaveragehelicalfraction.py",
    "PlottingRawvsSmooth.py",
    "Timeexceeds0.4basedonaverage.py",
    "AvgNumberofContacts.py",
]

for script in scripts:
    script_path = os.path.join(SRC_DIR, script)
    print(f"\nRunning {script}...\n")
    subprocess.run(["python", script_path])

print("\nAnalysis pipeline complete.")
