#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry

def odom_callback(data):
    rospy.loginfo(
        "Robot position : [%f, %f]", 
        data.pose.pose.position.x, 
        data.pose.pose.position.y)

def odom_subscriber():
    # rospy.init_node('name of the node')
    rospy.init_node('odom_subscriber')

    # rospy.Subscriber('name of the topic', TypeOfTheTopic, callback_func)
    rospy.Subscriber('odom', Odometry, odom_callback)

    # prevent python to stop, until we stop it manually
    rospy.spin()


if __name__ == '__main__':
    odom_subscriber()
    
