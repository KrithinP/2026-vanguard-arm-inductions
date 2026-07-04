# Evaluator's corner (private — not for recruits)

Notes for the induction panel. Nothing here is needed by recruits.

## One-time: publish the prebuilt image (do this before recruiting opens)

`docker-compose.yml` points recruits at `ghcr.io/krithinp/vanguard-inductions:latest`. Build and
push it once as **multi-arch** so both amd64 laptops and Apple-Silicon Macs pull a native image:

```bash
# from the repo root, logged in: echo $GHCR_PAT | docker login ghcr.io -u KrithinP --password-stdin
docker buildx create --use --name vanguard 2>/dev/null || docker buildx use vanguard
docker buildx build --platform linux/amd64,linux/arm64 \
  -t ghcr.io/krithinp/vanguard-inductions:latest --push .
```
Then make the GHCR package **public** (GitHub ▸ your profile ▸ Packages ▸ the package ▸ Settings ▸
Change visibility). Now recruits just run `docker compose up -d` — no build. Rebuild/push again if
you change the Dockerfile.

## Task 2 leaderboard
- `make_challenge.py` regenerates `assets/task2/challenge_signal.npy` (noisy, shipped) and `challenge_truth.npy` (hidden truth). Fixed seed → identical for everyone. Baseline RMSE of the raw noisy signal is ~2.64; a competent 1-D filter should land well under ~1.0.
- To score a submission's leaderboard entry, run their filter on `challenge_signal.npy` and compute `sqrt(mean((estimate - truth)**2))` against `challenge_truth.npy`. Watch for cheaters who just return the truth — cross-check that their filter also behaves sanely on their *own* generated data.

## Suggested rubric (per task, out of 10)
| | Correctness | Understanding | Code/commits | Honesty & report |
|---|---|---|---|---|
| Weight | 4 | 3 | 2 | 1 |

- **Task 1** is the priority — weight it ~2× the others in the final call.
- Shortlist gate: a working analytic IK in Task 1 that the recruit can *explain* in the walkthrough.
- Green flags: clean commit history, honest "what broke" notes, sensible questions in the induction channel, trying both SIFT and ORB in Task 3.
- Red flags: single giant commit dumped at the deadline, code they can't explain, `opencv-python` reinstalled over ours.

## Grading 50 forks efficiently
- Use the GitHub **Pulls** tab; PRs are titled `NAME [ID]`.
- Tasks 2 & 3 need no ROS — clone the fork, run the Python directly.
- Task 1: `docker compose up`, mount their `src/`, `colcon build`, run their launch file, watch RViz.
- Consider splitting the 50 across co-evaluators by PR order.
