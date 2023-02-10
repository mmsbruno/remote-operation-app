#!/usr/bin/python

import roslib
import rospy
from geometry_msgs.msg import PoseStamped

scene = moveit_commander.PlanningSceneInterface()
robot = moveit_commander.RobotCommander()

rospy.sleep(2)

p = PoseStamped()
p.header.frame_id = robot.get_planning_frame()
p.pose.position.x = 0.
p.pose.position.y = 0.
p.pose.position.z = 0.
scene.add_box("table", p, (0.5, 1.5, 0.6))