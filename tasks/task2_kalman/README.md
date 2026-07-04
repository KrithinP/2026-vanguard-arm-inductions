# 📈 Task 2 — Taming the Noise (1-D Kalman Filter)

> **Priority: 2 of 3.** Pure Python — no ROS or GUI needed. Runs anywhere, including plain Jupyter.

## The problem
The rover is crossing rough, rocky terrain. Vibrations are intense and the raw **IMU** readings are erratic — if navigation blindly trusts them, the rover thinks it's lurching back and forth uncontrollably. We need to see past the noise to the true motion.

## Your mission
Build a **1-D discrete Kalman filter from scratch** (just `numpy` — no filter libraries) to smooth this data. By balancing a model of the rover's motion against noisy measurements — the **predict → update** cycle — you'll pull a clean state estimate out of the chaos.

## What you need to do

1. **Simulate the chaos.** With `numpy`, generate a 1-D ground-truth signal (e.g. constant velocity), then corrupt it with heavy Gaussian noise 𝒩(μ, σ²) to mimic the broken IMU.
2. **Filter the truth.** Implement the Kalman loop (predict & update) to smooth the data step by step.
3. **Show your work.** With `matplotlib`, plot three curves on one figure: **true path**, **noisy measurements**, and your **filtered estimate**. Save it as a PNG.
4. **Know your math.** Comment the key quantities — state estimate, error covariance, process noise (Q), measurement noise (R), Kalman gain (K) — and *why* the update nudges the estimate the way it does.

## Deliverables
1. A self-contained `kalman_filter.py` in `src/task2/`.
2. A screenshot / PNG of your comparison plot.
3. (Optional but liked) a couple of lines: what happens to the estimate when you make Q or R bigger/smaller? Play with it.

## 🏆 Leaderboard (optional, for fun)
We provide a fixed noisy dataset (`assets/task2/challenge_signal.npy`). Run your filter on it and report the **RMSE** between your estimate and the true signal. Lowest RMSE tops the leaderboard. This is a bonus flex, not a requirement — but tuning Q and R to beat your friends is the fastest way to *feel* what the filter does.

## Hints
- Start with the scalar equations, not matrix form — 1-D means everything is a single number.
- If your estimate just copies the noisy data, your **R** (trust in measurements) is too low relative to **Q**. If it lags badly behind reality, R is too high. That tug-of-war *is* the Kalman filter.
- Initialize your covariance high (you're unsure at t=0) and watch it settle.
