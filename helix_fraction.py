def compute_helix_fraction(filepath):
    # Define which secondary structure codes are helical
    helix_codes = {'H', 'G', 'I'}  # H: alpha, G: 3_10, I: pi helix

    # Initialize counters
    total_Nh = 0
    total_N = 0
    failed_frames = 0
    helix_fractions = []

    # Open and read the file
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()

            # Skip blank lines
            if not line:
                failed_frames += 1
                continue

            Nh = sum(1 for c in line if c in helix_codes)
            N = len(line)
            h = Nh / N if N > 0 else 0

            helix_fractions.append(h)
            total_Nh += Nh
            total_N += N

    # Print summary
    print(f"Total frames: {i + 1}")
    print(f"Failed frames: {failed_frames}")
    print(f"Valid frames: {i + 1 - failed_frames}")
    print(f"\nAverage helix fraction h = Nh/N: {total_Nh / total_N:.4f} ({(total_Nh / total_N) * 100:.2f}%)")

    return helix_fractions

helix_fractions=compute_helix_fraction("C:\BINF641\Week9\ProductionC22\IBU\Trajectory1\sstructure.dat")

