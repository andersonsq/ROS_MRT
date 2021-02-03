#include "ros/ros.h"
#include <stdlib.h>
#include <stdio.h>

#include "nav_msgs/Odometry.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"

#include "mrt_312/service.h"

ros::Publisher pub; //publisher as global variable of name 'pub'

void positionCallback(const nav_msgs::Odometry::ConstPtr& msg)
{
	ROS_INFO("The robot position is: [%f, %f]", msg->pose.pose.position.x, msg->pose.pose.position.y);
	geometry_msgs::Twist vel;
	
	float b;
	
	//Robotino moviment logic
	if (msg->pose.pose.position.x < b)
	{
	vel.linear.x = 0.1;
	vel.linear.y = 0.1;
	}
		
	//To stop the robotino
	vel.linear.x = 0;
	vel.linear.y = 0;
				
	pub.publish(vel);
		
	//Logic to know if the robot walked 1 meter
	if((b - msg->pose.pose.position.x) < 0.06)
	{
	std::cout << "Your robot is on target" << std::endl;
	ros::shutdown();
	}	
}
	//Function of distance
	double distance(double a)
	{
	float c = 1;
	float d = 0;	
	//float x= c+d;
	return c+d;
	}

	//Function to pass the requested value of 1 meter to 'b'	
	bool my_distance (mrt_312::service::Request &req, mrt_312::service::Response &res)
	{
	res.b = distance(req.a);
	return true;
	}	
				
	
	/*MAIN FUNCTION*/		
int main(int argc, char **argv)
{	
	ros::init(argc, argv, "call_moviment");
	ros::NodeHandle n;
	
	/*Here I creat my service*/
	ros::ServiceServer service = n.advertiseService("setting_distance", my_distance);
	
	//ros::ServiceClient client = n.serviceClient<mrt_312::service>("receive_distance");
	
	//pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
		
	mrt_312::service srv;
	
	srv.request.a = b; //<-----------ERROR IN THIS PART
	
	//client.call(srv);
	
	ros::spin();
}
