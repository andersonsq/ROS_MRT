/* The first process will be in charge of:
	Calling a service for receiving a random target;
	Making the robot reach the target. */

#include "ros/ros.h"
#include "std_msgs/String.h"

#include <stdlib.h>
#include <stdio.h>

#include <iostream>
#include <sstream>

#include "nav_msgs/Odometry.h"
#include "geometry_msgs/Twist.h"
#include "sensor_msgs/LaserScan.h"

#include <math.h>

	//Declare the publisher as global variable with name "pub"
	ros::Publisher pub; 		
	
	//Created a mesage of type geometry_msgs Twist as global
	geometry_msgs::Twist vel;
	
	//Created a mesage of type sensor_msgs LaserScan as global
	sensor_msgs::LaserScan scan;
/*	
void positionCallback(const nav_msgs::Odometry::ConstPtr& msg)	//Callback is executed verytime I receive a new topic
{
	//Receive the position of my robot and print it on the shell
	ROS_INFO("The robot position is: [%f, %f]", msg->pose.pose.position.x, msg->pose.pose.position.y);	
	ros::Rate r(2);			//Declare a delay of 2 seconds with name "r
}
*/
void positionCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
{
	//Receive the position of my robot and print it on the shell
	ROS_INFO("The robot position is: [%f]", msg->ranges);	
	ros::Rate r(2);			//Declare a delay of 2 seconds with name "r
}

int main(int argc, char **argv)
{	
	ros::init(argc, argv, "closest_distance");	//third argumment is the name of the node that I'm creating

	//Declare new nodes	
	ros::NodeHandle n;

	//Initialize my publisher in /cmd_vel
	pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);

	//Subscribe and set a position in positionCall back function
	ros::Subscriber sub = n.subscribe("/odom", 1000, positionCallback); //I'm subscribing in "/odom"
	ros::Subscriber sub2 = n.subscribe("/scan", 1000, positionCallback); //I'm subscribing in "/scan"	
	
	ros::spin();

return 0;
}
