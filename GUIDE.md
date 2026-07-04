# 📚 The Recruit's Field Guide

Everything you need to go from zero to finishing these tasks — with the *best* resources we know, in the order we'd learn them. You don't need to read all of this. Skim to what you're stuck on.

> **Golden rule:** don't try to learn "all of ROS" first. Learn the *5%* each task needs, build the thing, and let the rest come later. Doing beats reading.

---

## 0. Foundations (do these once, ~1–2 hours total)

You need a little Linux terminal + Git before anything else.

| Skill | Why | Best resource (free) |
|---|---|---|
| **Terminal basics** | ROS lives in the terminal | [Ubuntu terminal tutorial](https://ubuntu.com/tutorials/command-line-for-beginners) — `cd`, `ls`, `mkdir`, editing files |
| **Git & GitHub** | How you submit | [GitHub "Hello World"](https://docs.github.com/en/get-started/start-your-journey/hello-world) + [Git branching visual](https://learngitbranching.js.org/) |
| **Python refresher** | All three tasks are Python | You already code — just skim [numpy quickstart](https://numpy.org/doc/stable/user/quickstart.html) |

**The only Git commands you need:**
```bash
git clone <your-fork-url>     # download your fork
git add .                     # stage changes
git commit -m "task 2 done"   # save a snapshot (do this OFTEN)
git push                      # upload to GitHub
```
Small, frequent commits with honest messages are a green flag to us.

---

## 1. ROS 2 — the crash course (for Task 1)

ROS 2 (Robot Operating System) is the plumbing robots use to talk to themselves — nodes that pass **messages** over **topics**. That's 90% of what you need.

### Start here (in order)
1. 🎥 **Articulated Robotics — "Getting Ready to Build Robots with ROS"** — the single best beginner ROS 2 series on the internet. Clear, visual, practical.
   → https://articulatedrobotics.xyz/tutorials/
2. 📖 **Official ROS 2 Humble tutorials** — do the **Beginner: CLI Tools** and **Beginner: Client Libraries** sections. Skip the rest for now.
   → https://docs.ros.org/en/humble/Tutorials.html
3. 🎥 **Robotics Back-End (Edouard Renard)** ROS 2 Python tutorials on YouTube — great for writing your first publisher/subscriber node.

### The concepts you actually need for Task 1
| Concept | One-line meaning | Where to learn |
|---|---|---|
| **Node** | One program in the robot | ROS 2 tut: "Understanding nodes" |
| **Topic** | A named channel nodes publish/subscribe to | ROS 2 tut: "Understanding topics" |
| **Message** | The data on a topic (we use `sensor_msgs/JointState`) | [JointState docs](https://docs.ros.org/en/humble/p/sensor_msgs/) |
| **Package** | A folder of related nodes/files (`vanguard_arm`) | ROS 2 tut: "Creating a package" |
| **`colcon build`** | Compiles your workspace | ROS 2 tut: "Using colcon" |
| **URDF** | XML describing a robot's links & joints | See §2 below |
| **TF / RViz** | Coordinate frames / the 3-D viewer | Articulated Robotics "URDF" videos |

### The workflow you'll repeat constantly
```bash
cd /root/ros2_ws
colcon build --symlink-install     # build your packages
source install/setup.bash          # tell ROS where they are  (do this in every new terminal!)
ros2 launch vanguard_arm display.launch.py
```
We gave you a **starter package** at `src/task1/vanguard_arm/` — read every file, it's commented to teach you. Run `display.launch.py` first to see the arm move via sliders, *then* write your IK.

---

## 2. Task 1 — Kinematics (URDF + Forward/Inverse Kinematics)

**Kinematics** = the math of *where the arm's hand is* given its joint angles (forward), and *what angles reach a point* (inverse).

| Topic | Best resource |
|---|---|
| **What is a URDF** | 🎥 Articulated Robotics "Describing a robot" (URDF) series — the clearest explanation anywhere |
| **URDF syntax** | 📖 [ROS 2 URDF tutorials](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/URDF-Main.html) |
| **Forward kinematics** | 🎥 [Angela Sodemann's robotics playlist](https://www.youtube.com/@ApexCanuck) / "Modern Robotics" Ch.3–4 |
| **Inverse kinematics (the core)** | 📖 [Analytic IK for a 3-DOF arm](https://www.alanzucconi.com/2017/04/17/robotic-arms/) — walks the exact geometry you need. Also search "2-link planar arm inverse kinematics law of cosines". |
| **Gold-standard textbook (free PDF)** | *Modern Robotics* by Kevin Lynch — http://hades.mech.northwestern.edu/index.php/Modern_Robotics (Ch. 6 = IK). Deep but definitive. |

**The mental model for our 3-DOF arm:** joint 1 spins the whole arm to *face* the target (`atan2(y, x)`). That reduces the rest to a flat **2-link arm in a vertical plane** — a classic law-of-cosines problem for the shoulder and elbow. Solve that on paper, then code it into `inverse_kinematics()`.

### 🎬 The Task 1 Video Path (watch in this order)

No single video covers our exact arm end-to-end — real robotics is assembled from pieces. This ordered path takes you from zero to a working IK node. **~3–4 hours of video total.** (All links verified July 2026; if one moved, the channel name is enough to find it.)

| Step | Watch / read | Covers | Time |
|---|---|---|---|
| 1️⃣ **Understand URDF** | 🎥📖 Articulated Robotics — [Describing robots with URDF](https://articulatedrobotics.xyz/tutorials/ready-for-ros/urdf/) | What links & joints are, how a robot is a tree | ~30 min |
| 2️⃣ **See an arm in RViz** | 📖 The Construct — [Robotic Manipulator Pt.1: Basic URDF & RViz](https://www.theconstruct.ai/ros-projects-robotic-manipulator-part-1-basic-urdf-rviz/) | An actual multi-joint arm shown in RViz with sliders | ~40 min |
| 3️⃣ **Working arm repo to copy the pattern** | 💻 [olmerg/lesson_urdf](https://github.com/olmerg/lesson_urdf) — ROS 2 arm in RViz via `robot_state_publisher` + `joint_state_publisher_gui` | The exact node setup our starter uses | ~20 min |
| 4️⃣ **Frames & TF** | 🎥📖 Articulated Robotics — [The Transform System (tf2)](https://articulatedrobotics.xyz/tutorials/ready-for-ros/tf/) | Why the gripper's position is a chain of transforms | ~25 min |
| 5️⃣ **The IK math (core!)** | 🎥 [Easy inverse kinematics for robot arms](https://www.youtube.com/watch?v=Q-UeYEpwXXU) + 🎥 [Arduino IK for a 3-DOF arm](https://www.youtube.com/watch?v=Y8ueTjqCcAg) | Deriving joint angles from an (x,y,z) target — high-school trig, no ROS needed | ~40 min |
| 6️⃣ **IK, written deep-dive** | 📝 [Alan Zucconi — Inverse Kinematics in 3D](https://www.alanzucconi.com/2020/09/14/inverse-kinematics-in-3d/) + 📝 [Automatic Addison — analytic IK guide](https://automaticaddison.com/the-ultimate-guide-to-inverse-kinematics-for-6dof-robot-arms/) | The exact geometry, in text you can re-read while coding | ~30 min |
| 7️⃣ **Publish it as a ROS node** | 📖 [ROS 2 Humble — Using URDF with robot_state_publisher](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher-cpp.html) | Writing a node that publishes `JointState` (Python equivalent of what our `ik_node.py` does) | ~30 min |
| ⭐ **Bonus: Gazebo + ros2_control** | 🎥📖 Articulated Robotics — [ros2_control Concepts & Simulation](https://articulatedrobotics.xyz/tutorials/mobile-robot/applications/ros2_control-concepts/) | Driving the arm with a real controller in Gazebo | ~35 min |

**How to actually use this:** don't binge all 7 first. Watch 1–3, then *open the starter package and play with `display.launch.py`*. Watch 5–6 with pen and paper and derive the IK yourself. Only then write `inverse_kinematics()`. Video → do → video → do beats video → video → video.

> ⚠️ Steps 5's videos use Arduino, not ROS — that's fine and intentional. **The IK math is identical everywhere**; only "where the angles get sent" changes. Our starter package already handles the ROS side, so you're really just porting the math into `inverse_kinematics()`.

---

## 3. Task 2 — The Kalman Filter

A Kalman filter blends a **prediction** (what your motion model expects) with a **measurement** (a noisy sensor) to get a better estimate than either alone.

| Resource | Why it's great |
|---|---|
| 📖 **"How a Kalman filter works, in pictures"** — https://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/ | The famous explainer. Read this **first**. Builds full intuition, minimal scary math. |
| 🎥 **MATLAB Tech Talks — "Understanding Kalman Filters"** (YouTube, 6 parts) | Short, visual, excellent. |
| 📖 **Kalman & Bayesian Filters in Python** (free book) — https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python | Interactive notebooks. Chapters 1–4 cover the 1-D case you need. |

**Don't over-reach.** You only need the **1-D scalar** version: five little equations (predict state, predict covariance, Kalman gain, update state, update covariance). Get those looping over your noisy array and plot the result. The whole `kalman_filter.py` is ~40 lines.

---

## 4. Task 3 — Image Stitching

Classical computer vision: find matching features across photos, compute the geometric transform between them, warp and blend.

| Topic | Best resource |
|---|---|
| **Big-picture intuition** | 🎥 **First Principles of Computer Vision** (Shree Nayar, Columbia) YouTube — "Image Stitching" & "Feature Detection" lectures. Beautifully explained. |
| **Features (SIFT/ORB)** | 📖 [OpenCV feature-detection tutorials](https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html) |
| **Homography & RANSAC** | 📖 [OpenCV: Feature matching + homography](https://docs.opencv.org/4.x/d1/de0/tutorial_py_feature_homography.html) |
| **Full stitching walkthrough** | 📝 [PyImageSearch "Image stitching with OpenCV"](https://pyimagesearch.com/2018/12/17/image-stitching-with-opencv-and-python/) |

**Practical wins:** shoot photos by **rotating in place** (not walking) — that's what homography assumes and it fixes most failures. Use **Lowe's ratio test** to throw out bad matches before RANSAC. Try both SIFT and ORB and *report the difference* — that comparison earns marks.

---

## 5. How to get unstuck (the real skill)

1. **Read the error message.** Actually read it. ROS errors are verbose but usually name the exact problem.
2. **Isolate.** Does `ros2 topic echo /joint_states` show data? Is your node even publishing? Test one piece at a time.
3. **Search well.** Paste the exact error into Google + "ROS 2 humble".
4. **Use AI, but understand it.** Ask Claude/ChatGPT to *explain* a concept or your error. Then write the code yourself. We'll ask you to explain it later — see the AI policy in the main README.
5. **Ask us.** A specific question ("my IK returns NaN when z is large, here's my code") is a green flag. "It doesn't work" is not.

---

## 6. Cheat sheet

```bash
# --- environment ---
docker compose up -d --build            # start (open http://localhost:8080)
docker compose exec vanguard /bin/bash  # get a terminal inside
docker compose down                     # stop

# --- ROS 2 essentials ---
source /opt/ros/humble/setup.bash       # load ROS (auto-loaded in our container)
ros2 pkg create --build-type ament_python my_pkg   # make a package
colcon build --symlink-install          # build (run from ros2_ws root)
source install/setup.bash               # load YOUR packages (every new terminal!)
ros2 run <pkg> <node>                   # run a node
ros2 launch <pkg> <file.launch.py>      # run a launch file
ros2 topic list                         # what topics exist?
ros2 topic echo /joint_states           # watch a topic's data
ros2 node list                          # what nodes are running?

# --- Python tasks ---
python3 src/task2/kalman_filter.py
python3 src/task3/stitch.py
```

Now go build something. 🚀 — *The Vanguard Arm & Autonomy team*
