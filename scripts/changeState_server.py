#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_srvs.srv import SetBool,SetBoolResponse

g_state = False

def changeState_handler(req):
    global g_state
    rospy.loginfo("Service called with data = %d", req.data)

    response = SetBoolResponse()
    
    if req.data == g_state:
         response.success = False
         response.message = "Incorrect call of the service"
    else : 
         g_state = req.data
         response.success = True
         response.message = "Service succesfully called"

    return response


def changeState_server():
    global g_state

    rospy.init_node("changeState_server")

    # rospy.Service("name of the service", TypeOfService, handle_function)
    state_server = rospy.Service("changeState", SetBool, changeState_handler)

    rate = rospy.Rate(1) # 1Hz
    
    while not rospy.is_shutdown():
         rospy.loginfo("State = %d", g_state)
         rate.sleep()


if __name__ == '__main__':
    changeState_server()
