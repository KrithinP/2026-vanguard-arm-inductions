"""Visualize the arm in RViz and drag its joints by hand.

    ros2 launch vanguard_arm display.launch.py

This starts robot_state_publisher (turns your URDF + joint angles into TF frames),
the joint_state_publisher_gui (sliders to move each joint), and RViz.

Use this to sanity-check your URDF FIRST. Once your IK node works, close this and
run `ros2 run vanguard_arm ik_node` instead (don't run both — they'd fight over
/joint_states).
"""
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    pkg = get_package_share_directory('vanguard_arm')
    urdf = os.path.join(pkg, 'urdf', 'arm.urdf')
    with open(urdf, 'r') as f:
        robot_description = f.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', os.path.join(pkg, 'rviz', 'arm.rviz')],
        ),
    ])
