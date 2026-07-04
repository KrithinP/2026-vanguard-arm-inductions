import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'vanguard_arm'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install launch files, the URDF, and the RViz config so ros2 can find them.
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='recruit',
    maintainer_email='you@bitshyderabad.ac.in',
    description='Starter package for Task 1 — 3-DOF arm and inverse kinematics.',
    license='MIT',
    entry_points={
        'console_scripts': [
            # Run with:  ros2 run vanguard_arm ik_node
            'ik_node = vanguard_arm.ik_node:main',
        ],
    },
)
