#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

def cmdvel_publisher():
    # rospy.Publisher('name of the topic', TypeOfTheTopic)
    cmdvel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)

    # rospy.init_node('name of the node')
    rospy.init_node('cmdvel_publisher')

    rate = rospy.Rate(10) # 10Hz

    # While we didn't request to shutdown the node (ctrl-c)
    try:
        while not rospy.is_shutdown():
           print("Loop is running");

           # We create a variable of type Twist
           velocity_data = Twist()

           # Set linear velocity
           velocity_data.linear.x = 0.05 # m/s

           # publish
           cmdvel_pub.publish(velocity_data)

           # Sleep until next iteration 
           rate.sleep()
        
    except rospy.ROSInterruptException:
        pass

    # Stop the robot at the end of the script
    velocity_null = Twist() 
    cmdvel_pub.publish(velocity_null) 


if __name__ == '__main__':
    cmdvel_publisher()
    








