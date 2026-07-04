# Project Vanguard — Arm & Autonomy Division inductions
# Base: ROS 2 Humble desktop with a full LXDE desktop served over noVNC (browser).
#   noVNC lives on container port 6080 (mapped to 8080 on your host by docker-compose).
FROM tiryoh/ros2-desktop-vnc:humble

# ---- ROS 2 packages -------------------------------------------------------
# Everything a recruit needs for Task 1 (arm) is pre-baked so nobody burns a
# day on `apt install`. Gazebo Classic + ros2_control are here for the bonus.
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-humble-xacro \
    ros-humble-robot-state-publisher \
    ros-humble-joint-state-publisher \
    ros-humble-joint-state-publisher-gui \
    ros-humble-gazebo-ros-pkgs \
    ros-humble-gazebo-ros2-control \
    ros-humble-ros2-control \
    ros-humble-ros2-controllers \
    ros-humble-controller-manager \
    ros-humble-moveit \
    ros-humble-rviz2 \
    ros-humble-tf2-tools \
    ros-humble-turtlesim \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# ---- Python packages (Tasks 2 & 3 are pure Python) ------------------------
# opencv-CONTRIB gives SIFT *and* ORB out of the box. Do not swap for
# opencv-python — recruits will hit "module has no attribute SIFT".
RUN pip3 install --no-cache-dir \
    numpy \
    scipy \
    matplotlib \
    opencv-contrib-python \
    jupyterlab

# Source ROS in every interactive shell so `ros2 ...` just works.
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

WORKDIR /root/ros2_ws
