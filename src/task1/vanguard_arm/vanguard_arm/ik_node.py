#!/usr/bin/env python3
"""Task 1 starter — the inverse-kinematics node.

WHAT THIS FILE DOES (already working):
  - Spins up a ROS 2 node that publishes /joint_states.
  - Smoothly animates the arm from its HOME pose to a set of TARGET joint angles.
  - Publishes at 30 Hz so RViz shows a clean motion.

WHAT YOU MUST DO (the graded part):
  - Fill in `inverse_kinematics(x, y, z)` so it returns the three joint angles
    that put the gripper tip at the world point (x, y, z).
  - The link lengths L1, L2, L3 below MUST match your URDF.
  - Bonus: derive it on paper first, then check your code against
    `forward_kinematics()` (given angles -> where is the tip?).

Run it (after `colcon build` and sourcing the workspace):
    ros2 run vanguard_arm ik_node
Then open RViz (set Fixed Frame = base_link, add a RobotModel display) to watch.
"""
import math
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

# Link lengths — KEEP THESE IN SYNC WITH arm.urdf.
L1 = 0.20   # link1 length (base -> shoulder)
L2 = 0.20   # link2 length (shoulder -> elbow)
L3 = 0.20   # link3 length (elbow -> tip)  (0.18 link + 0.02 offsets in the starter URDF ~ tune this)

JOINT_NAMES = ['joint1', 'joint2', 'joint3']
HOME = [0.0, 0.0, 0.0]

# The rock the rover must reach (world coordinates, metres). Change to test.
TARGET_XYZ = (0.25, 0.10, 0.20)


def forward_kinematics(q):
    """Given joint angles q=[q1,q2,q3], return the (x,y,z) of the gripper tip.

    Deriving this yourself is the best way to then invert it. Fill it in as a
    warm-up — it's not graded, but it makes your IK debuggable.
    """
    # TODO (recommended): implement FK for the frame convention in arm.urdf.
    # joint1 about Z, joint2 & joint3 about Y.
    raise NotImplementedError("Optional warm-up: implement forward kinematics.")


def inverse_kinematics(x, y, z):
    """Return [q1, q2, q3] that place the gripper tip at world point (x, y, z).

    THIS IS THE GRADED PART. A 3-DOF arm reaching a *point* has an exact
    geometric solution — no optimiser needed.

    Approach that works for the URDF convention above:
      1. q1 = base yaw = atan2(y, x)              (rotate to face the target)
      2. Work in the vertical plane containing the arm. Let
             r = sqrt(x**2 + y**2)                (horizontal reach)
         and solve the remaining 2-link planar problem for (r, z) using the
         law of cosines to get q2 (shoulder) and q3 (elbow).
      3. Watch your sign conventions and the elbow-up vs elbow-down choice.

    Return the angles in radians, in the order [joint1, joint2, joint3].
    """
    # TODO: replace this stub with your derivation.
    raise NotImplementedError("Implement inverse kinematics — this is the task.")


class IKNode(Node):
    def __init__(self):
        super().__init__('ik_node')
        self.pub = self.create_publisher(JointState, 'joint_states', 10)

        # Compute the goal angles once at startup.
        try:
            self.goal = inverse_kinematics(*TARGET_XYZ)
            self.get_logger().info(f'IK solution for {TARGET_XYZ}: {self.goal}')
        except NotImplementedError:
            self.get_logger().warn('inverse_kinematics() not implemented yet — '
                                   'holding at HOME. Fill it in!')
            self.goal = HOME

        self.start = np.array(HOME, dtype=float)
        self.end = np.array(self.goal, dtype=float)
        self.t = 0.0
        self.duration = 3.0                      # seconds home -> target
        self.timer = self.create_timer(1.0 / 30.0, self.tick)

    def tick(self):
        # Linear interpolation home -> target (a real controller would do better,
        # but this is enough to *see* your IK land on the point).
        alpha = min(self.t / self.duration, 1.0)
        q = (1 - alpha) * self.start + alpha * self.end

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = JOINT_NAMES
        msg.position = [float(v) for v in q]
        self.pub.publish(msg)
        self.t += 1.0 / 30.0


def main():
    rclpy.init()
    node = IKNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
