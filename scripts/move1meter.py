#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

g_robotPosition = Odometry()
g_positionReceived = False

def odom_callback(data):
    global g_robotPosition
    global g_positionReceived
    
    rospy.loginfo(
        "Robot position : [%f, %f]", 
        data.pose.pose.position.x, 
        data.pose.pose.position.y)
    
    g_robotPosition = data
    g_positionReceived = True


def move1meter():
    global g_robotPosition
    global g_positionReceived
    rospy.init_node("move1meter")

    rospy.Subscriber('odom', Odometry, odom_callback)

    cmdvel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)

    rate = rospy.Rate(10) # 10Hz

    # Wait receiving robot Odometry at least one time 
    while (not rospy.is_shutdown()) and (not g_positionReceived):
         rospy.loginfo("Waiting Odometry data")
         rospy.loginfo("position received = %d", g_positionReceived)
         rate.sleep()

    # Get the actual position of the robot
    initRobotPosition = g_robotPosition


    # Set velocity of the robot to 0.1m/s forward
    velocity_data = Twist()
    velocity_data.linear.x = 0.1
    cmdvel_pub.publish(velocity_data)
    rospy.loginfo("Move the robot")

    positionReached = False
    while (not rospy.is_shutdown()) and (not positionReached):
        cmdvel_pub.publish(velocity_data)

        # Our code to monitor position of the robot
        # If the robot reach 1 meter at least then stop the robot
        # This test only work if the robot is oriented along x axis 
        # Try to modify the condition to make the script work for any orientation
        if g_robotPosition.pose.pose.position.x > (initRobotPosition.pose.pose.position.x + 1):
             rospy.loginfo("Robot reach final position")
	     velocity_data.linear.x = 0
             cmdvel_pub.publish(velocity_data)
             positionReached = True
  
        rate.sleep()
        


if __name__ == '__main__':
    move1meter()



