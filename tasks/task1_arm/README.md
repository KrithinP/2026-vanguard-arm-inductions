# 🦾 Task 1 — The Art of Reach (3-DOF Arm & Inverse Kinematics)

> **Priority: 1 of 3 (highest).** This is the task we care about most. If you only finish one, finish this one.

## The problem
The rover has reached the target extraction site, and a high-priority geological sample sits just **40 cm away**. One problem: the chassis is stuck in the sand. Our only hope is the onboard **3-Degree-of-Freedom (3-DOF) manipulator arm** — but the targeting software was corrupted during descent. The arm doesn't know how to bend its joints to reach the rock.

## Your mission
Build the digital twin of this arm and write the software that tells it how to move. You'll design a 3-DOF arm, load it into a simulator, and use **Inverse Kinematics (IK)** to compute exactly how each joint must rotate to move the gripper from its home pose to a target **(X, Y, Z)** point in space.

## What you need to do

1. **Build the blueprint.** Write a **URDF** (or Xacro) describing a 3-DOF arm: a base, three links, three revolute joints. Give it sensible link lengths and joint limits.
2. **Bring it to life.** Launch the arm so you can *see* it in 3-D.
   - ✅ **Required path — RViz.** Use `robot_state_publisher` + RViz to visualize the arm. This is **lightweight and runs on any laptop.** Prove your IK by publishing joint angles to `/joint_states` and watching the gripper land on the target.
   - ⭐ **Bonus — Gazebo Classic.** Spawn the arm in Gazebo and drive it with `ros2_control` (a `JointTrajectoryController`). Heavier; only if your machine can handle it.
3. **Solve the puzzle — Inverse Kinematics.** Given the target's (X, Y, Z), compute the required joint angles.
   - ✅ **Required — write the math yourself.** A 3-DOF arm reaching a *point* is exactly 3 equations in 3 unknowns — solve it analytically/geometrically in Python. This is the whole point of the task; we want to see you derive it.
   - ⭐ **Bonus — MoveIt 2.** You may *additionally* show a MoveIt setup. (Heads up: MoveIt's default KDL solver struggles with sub-6-DOF arms — so your own analytic IK is the reliable route, and what we're grading.)
4. **Make the move.** Write a **ROS 2 node** that takes a target point, computes the angles with your IK, and publishes a joint trajectory that moves the arm from **Home → Target**.

## Deliverables
1. A complete ROS 2 package in `src/task1/` with your URDF/Xacro, launch file(s), and IK/movement node.
2. A short **screen recording** (link it in your PR — don't commit large videos) or a few **clear screenshots** of the arm reaching the target on the noVNC desktop.
3. A few comments or a short note explaining your IK derivation. Show us you understand *why* the angles are what they are.

## Hints
- Start with **forward kinematics** (given angles, where's the gripper?). Get that right, visualize it, *then* invert it. FK working = IK debuggable.
- Pick a target you *know* is reachable (inside the arm's workspace) before trying edge cases.
- `ros2 run joint_state_publisher_gui joint_state_publisher_gui` lets you drag joints by hand — great for sanity-checking your URDF before writing any IK.
- Keep link lengths simple (e.g. 0.2 m each) so your hand-math is easy to check.

## What "done" looks like
You type a target point, run your node, and the arm swings from home to put its gripper on that point — visible in RViz. Bonus points for handling unreachable targets gracefully.
