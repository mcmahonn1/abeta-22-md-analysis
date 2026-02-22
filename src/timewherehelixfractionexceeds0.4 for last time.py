def compute_last_above_threshold(smoothed_list, threshold=0.4):
    th_ms = []
    for smoothed in smoothed_list:
        indices = np.where(smoothed > threshold)[0]
        if len(indices) > 0:
            last_idx = indices[-1]
            th_ns = last_idx * frame_interval_ps / 1000
            th_ms.append(th_ns)
        else:
            th_ms.append(None)  # If it never crosses 0.4
    return th_ms

# Recalculate smoothed helix fractions for each trajectory
s1_smoothed = []
for fname in s1_files:
    full_path = os.path.join(data_dir, fname)
    hf = compute_helix_fraction(full_path)
    smoothed = np.convolve(hf, np.ones(window_size)/window_size, mode='valid')
    s1_smoothed.append(smoothed)

# Compute th,m and th for System 1
s1_thms = compute_last_above_threshold(s1_smoothed)
s1_valid_thms = [t for t in s1_thms if t is not None]
s1_th_avg = np.mean(s1_valid_thms)

print("System 1 t_h,m values (ns):", s1_thms)
print(f"System 1 average t_h (ns): {s1_th_avg:.2f}")


# Step 1: Recompute smoothed helix fractions for each trajectory in System 2
s2_smoothed = []
for fname in s2_files:
    full_path = os.path.join(data_dir, fname)
    hf = compute_helix_fraction(full_path)
    smoothed = np.convolve(hf, np.ones(window_size)/window_size, mode='valid')
    s2_smoothed.append(smoothed)

# Step 2: Compute th,m and the average t_h for System 2
s2_thms = compute_last_above_threshold(s2_smoothed)
s2_valid_thms = [t for t in s2_thms if t is not None]
s2_th_avg = np.mean(s2_valid_thms)

print("System 2 t_h,m values (ns):", s2_thms)
print(f"System 2 average t_h (ns): {s2_th_avg:.2f}")
