"""Generate the Task 2 leaderboard dataset.

Produces two files:
  - assets/task2/challenge_signal.npy   -> NOISY measurements (ship to recruits)
  - grading/challenge_truth.npy         -> ground truth (evaluators only)

Recruits run their filter on the noisy signal and report RMSE vs truth.
Run once from the repo root:  python3 grading/make_challenge.py
"""
import numpy as np

RNG = np.random.default_rng(42)          # fixed seed -> everyone gets the same challenge
N = 200
dt = 1.0

# Ground truth: constant-velocity motion with a couple of gentle accel changes.
v = 0.5
x = 0.0
truth = []
for k in range(N):
    if k == 80:
        v = -0.3
    if k == 140:
        v = 0.6
    x += v * dt
    truth.append(x)
truth = np.array(truth)

# Heavy Gaussian measurement noise (the "broken IMU").
noisy = truth + RNG.normal(0.0, 3.0, size=N)

np.save("assets/task2/challenge_signal.npy", noisy)
np.save("grading/challenge_truth.npy", truth)
print(f"Wrote {N} samples. Baseline RMSE (raw noisy vs truth): "
      f"{np.sqrt(np.mean((noisy - truth) ** 2)):.3f}")
