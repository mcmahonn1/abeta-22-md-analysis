# System 1
indices_s1 = np.where(s1_avg > 0.4)[0]
if len(indices_s1) > 0:
    th_avg_s1 = indices_s1[-1] * frame_interval_ps / 1000
    print(f"System 1 ⟨t_h⟩ from ⟨H(t)⟩: {th_avg_s1:.2f} ns")
else:
    print("System 1 ⟨H(t)⟩ never exceeds 0.4")

# System 2
indices_s2 = np.where(s2_avg > 0.4)[0]
if len(indices_s2) > 0:
    th_avg_s2 = indices_s2[-1] * frame_interval_ps / 1000
    print(f"System 2 ⟨t_h⟩ from ⟨H(t)⟩: {th_avg_s2:.2f} ns")
else:
    print("System 2 ⟨H(t)⟩ never exceeds 0.4")
