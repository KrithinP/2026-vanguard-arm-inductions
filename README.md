# 🤖 Project Vanguard — Arm & Autonomy Division Inductions

> *Mission log, Sol 412.* The rover has reached the extraction site. A high-value sample sits 40 cm away — but the chassis is buried in regolith, the IMU is screaming noise, and the imaging team wants a survey panorama before we move. Everything now depends on the software **you** write.

Welcome. This is the induction for the **Arm & Autonomy** division of Project Vanguard, BITS Pilani Hyderabad's Mars Rover team. Over three tasks you'll build a robot arm and make it reach, tame a noisy sensor with a Kalman filter, and stitch a field panorama from scratch.

> 🆕 **New to ROS / robotics? Start with [`GUIDE.md`](GUIDE.md)** — a from-zero field guide with the best free resources for each task, in the order we'd learn them.

**You are not expected to finish all three.** We care far more about *how* you think than about a perfect submission. Attempt in order — **Task 1 matters most, then 2, then 3.** Get as far as you can, be honest about what broke, and show us your reasoning. As always: best of luck, and happy coding. 🚀

---

## Contents
1. [What you need](#what-you-need)
2. [Get the environment running](#get-the-environment-running)
3. [The tasks](#the-tasks)
4. [How to submit](#how-to-submit)
5. [How you'll be judged](#how-youll-be-judged)
6. [Using AI tools](#using-ai-tools)
7. [Troubleshooting](#troubleshooting)

---

## What you need

- A **GitHub account** (you'll fork this repo).
- **Git** installed locally.
- **Either** of these two paths to run the environment:
  - 🐳 **Local Docker** — [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac) or Docker Engine + Compose (Linux). ~6 GB download, wants ≥8 GB RAM free.
  - ☁️ **GitHub Codespaces** (zero install, runs in your browser) — recommended if you're on an **Apple Silicon Mac** or a low-RAM laptop. See below.

You do **not** need to dual-boot Ubuntu. That's the whole point of this repo.

---

## Get the environment running

### Step 0 — Fork & clone
Click **Fork** (top-right of this repo). Then:
```bash
git clone https://github.com/<your-username>/2026-vanguard-arm-inductions.git
cd 2026-vanguard-arm-inductions
```

### Path A — Local Docker 🐳
```bash
docker compose up -d      # pulls our prebuilt image (fast). No build needed.
```
Open **http://localhost:8080** in your browser. You now have a full Linux desktop with ROS 2 Humble, Gazebo, and RViz. Everything is pre-installed.

> The image is **multi-arch** — on an **Apple Silicon Mac** it pulls the native arm64 build, so RViz runs smoothly with no emulation. (Only add `--build` if you deliberately want to build the image yourself.)

To get a terminal *inside* the container:
```bash
docker compose exec vanguard /bin/bash
```
Your work in `src/` on your laptop shows up at `/root/ros2_ws/src` inside the container (and survives restarts). Edit files in your normal editor, run them in the container.

Shut it down with `docker compose down`.

### Path B — GitHub Codespaces ☁️ (no install)
On **your fork**: **Code ▸ Codespaces ▸ Create codespace on main**. Wait for it to build, then open the forwarded **noVNC Desktop** port (6080) preview for the GUI. VS Code runs in your browser; the ROS environment is already there.

### Sanity check (do this first!)
Inside the container terminal:
```bash
source /opt/ros/humble/setup.bash
ros2 run turtlesim turtlesim_node
```
A little turtle window should appear on the noVNC desktop. If it does, your environment works and you're ready. 🎉

---

## The tasks

| # | Task | What you'll learn | Brief |
|---|------|-------------------|-------|
| 1 | 🦾 **The Art of Reach** | URDF, TF, forward & inverse kinematics, ROS 2 nodes | [tasks/task1_arm](tasks/task1_arm/README.md) |
| 2 | 📈 **Taming the Noise** | State estimation, the 1-D Kalman filter | [tasks/task2_kalman](tasks/task2_kalman/README.md) |
| 3 | 📸 **Panorama or Bust** | Feature matching, homography, image stitching | [tasks/task3_panorama](tasks/task3_panorama/README.md) |

Put your solutions in `src/task1/`, `src/task2/`, `src/task3/` respectively.

---

## How to submit

1. Do your work on your fork, committing as you go (small, clear commits are a good sign).
2. Put each task's work in its `src/taskN/` folder.
3. When you're done (or out of time), open a **Pull Request** to this repository's `main`.
4. **PR title:** `NAME [ID_NUMBER]` — e.g. `Ada Lovelace [2026A7PS0042H]`.
5. Fill in the PR template (name, ID, institute email, what you built, links to any recordings).

One PR per person. You can keep pushing to it until the deadline.

---

## How you'll be judged

We're not grading you on completion. Roughly:

- **Correctness** — does it do the thing? (arm reaches the point, filter tracks truth, panorama stitches)
- **Understanding** — your code comments and report show you know *why* it works, not just that it runs.
- **Engineering** — clean, readable code and commits. A working 80% you understand beats a copied 100% you don't.
- **Honesty** — a clear "here's what failed and why" is worth more than pretending it all worked.

Shortlisted recruits will have a short **walkthrough chat** where we ask you to explain your own code. Build things you can defend.

---

## Using AI tools

You **may** use ChatGPT / Claude / Copilot — we're an AI-leveraged team and pretending otherwise is silly. But: **you must understand every line you submit.** In the walkthrough we'll ask you to explain and modify your code live. If you can't, it doesn't count. Use AI to learn faster, not to think less.

---

## Troubleshooting

**`http://localhost:8080` won't load** — give the container a minute after `up`. Check `docker compose ps`. On Codespaces, use the forwarded port preview, not localhost.

**Gazebo/RViz is super slow or crashes** — you're likely on limited hardware. For Task 1, **use RViz, not Gazebo** (it's much lighter — see the Task 1 brief). If it still struggles, switch to **Codespaces**. If you see shared-memory errors, make sure `shm_size` is set (it is, in our compose file).

**`ros2: command not found`** — run `source /opt/ros/humble/setup.bash` (or open a fresh terminal; it's in `.bashrc`).

**Apple Silicon Mac** — the image is multi-arch, so RViz (the required Task 1 path) runs *natively* and smoothly. Only the **Gazebo bonus** may be heavy; if so, skip it (RViz is all you need) or use **Codespaces**. Tasks 2 and 3 are pure Python and run fine locally anyway.

**"cv2 has no attribute SIFT_create"** — you have plain `opencv-python` somewhere shadowing ours. Inside our container it's `opencv-contrib-python` and works. Don't `pip install opencv-python` over it.

Still stuck? Open an issue on your fork or ask in the induction channel. Asking good questions is a skill we're looking for.
