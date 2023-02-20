# Disclaimer

This work was carried out during a master's thesis, using and modifying open-source Robot Web Tools (RWT) files, libraries, or directories, and was tested on a real model of the UR3 robotic manipulator from Universal Robots and other simulated models.

# Setup

This application was developed using Ubuntu 18.04 and ROS Melodic.

# Installation

1) In your workspace, add all files except for the 'application' file. If you haven't already, also add the drivers for the desired robot (you can find them on GitHub).

2) Execute the 'catkin_make' command or equivalent in your terminal.

3) In the 'application' folder, you will find the 'index.html' file of the web application. Add the 'description' directory of the desired robot to this folder.

# Initializing (UR3 example)

## With a simulated robot

1) roslaunch ur_gazebo ur3_bringup.launch

2) roslaunch ur3_moveit_config ur3_moveit_planning_execution.launch sim:=true

3) roslaunch rwt_moveit sim_demo.launch

4) Run "index.html" on Live Server

## With a real robot

1) roslaunch ur_robot_driver ur3_bringup.launch limited:=true robot_ip:=ROBOT_IP kinematics_config:=$HOME/ur_ws/src/fmauch_universal_robot/ur_description/urdf/calibration1.yaml

2) roslaunch ur3_moveit_config ur3_moveit_planning_execution.launch limited:=true

3) roslaunch ur3_moveit_config moveit_rviz.launch config:=true

4) roslaunch rwt_moveit demo.launch

5) Run "index.html" on Live Server
